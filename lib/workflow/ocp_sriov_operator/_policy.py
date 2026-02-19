import json
import yaml
from menu import common


def expand_policy(policies, interfaces, my_output):
    success = True
    new_policies = []

    for policy in policies:
        if policy['interface'] is not None:
            found = False
            for interface in interfaces:
                if interface['name'] == policy['interface']:
                    found = True
                    break

            if not found:
                my_output.error('Interface [%s] not found' % (interface['name']))
                success = False
                continue

            new_policies.append(
                policy
            )
            continue

        if policy['vendor'] is not None:
            pattern = '${IFNAME}'
            for interface in interfaces:
                if interface['lspci'] is not None and policy['vendor'].lower() in interface['lspci'].lower():
                    if policy['driver'] is not None:
                        match = False
                        for driver in policy['driver'].split(','):
                            if interface['ethtool'] is not None:
                                if len(driver.split('!')) > 1:
                                    if interface['ethtool']['driver'] != driver.split('!')[1]:
                                        match = True
                                else:
                                    if interface['ethtool']['driver'] == driver:
                                        match = True

                        if not match:
                            continue

                    new_policy = {}
                    new_policy['interface'] = interface['name']
                    new_policy['type'] = policy['type']
                    new_policy['name'] = policy['name'].replace(pattern, interface['name'])
                    new_policy['resource'] = policy['resource'].replace(pattern, interface['name'])
                    new_policy['vfs'] = policy['vfs']
                    new_policy['range'] = policy['range']
                    new_policies.append(
                        new_policy
                    )

    return success, new_policies


def run(params, my_output):
    if len(params['policy']) == 0:
        return True, False, None

    my_output.default('Collecting interface details...')

    interfaces = params['linux_handler'].get_interfaces(
        phys_only=True,
        ethtool=True,
        lspci=True,
        verbose=True
    )

    success, policies = expand_policy(
        params['policy'],
        interfaces,
        my_output
    )
    if not success:
        return False, False, 'Input policy analysis failure'

    my_output.default('SRIOV Policies', underline=True)
    my_output.default(json.dumps(policies, indent=4))
    if 'confirmation' in params and params['confirmation']:
        if not common.get_confirmation():
            return False, False, 'User break'

    created = False

    for policy in policies:
        exists = params['k8s_handler'].is_sriov_network_node_policy(
            policy['name'],
            namespace=params['namespace'],
            cache_enabled=False
        )
        if exists:
            my_output.default('SriovNetworkNodePolicy %s already exists' % (policy['name']))
            continue

        body = {}
        body['apiVersion'] = 'sriovnetwork.openshift.io/v1'
        body['kind'] = 'SriovNetworkNodePolicy'
        body['metadata'] = {}
        body['metadata']['namespace'] = params['namespace']
        body['metadata']['name'] = policy['name']
        body['spec'] = {}
        body['spec']['deviceType'] = policy['type']
        body['spec']['isRdma'] = False
        body['spec']['nicSelector'] = {}
        body['spec']['nicSelector']['pfNames'] = []

        if policy['range'] is None:
            pf_mo = policy['interface']
        else:
            pf_mo = '%s#%s' % (policy['interface'], policy['range'])
        body['spec']['nicSelector']['pfNames'].append(pf_mo)

        body['spec']['nodeSelector'] = {}
        body['spec']['nodeSelector']['feature.node.kubernetes.io/network-sriov.capable'] = 'true'

        body['spec']['numVfs'] = int(policy['vfs'])
        body['spec']['resourceName'] = policy['resource']

        try:
            body_yaml = yaml.dump(body)
        except BaseException:
            return False, False, 'Body preparation failed'

        my_output.default(body_yaml)

        if not params['k8s_handler'].create_sriov_network_node_policy(body):
            return False, False, 'SRIOV policy create failed'

        created = True

    return True, created, None
