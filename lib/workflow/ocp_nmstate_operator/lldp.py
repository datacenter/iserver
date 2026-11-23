from lib import output_helper
from lib.k8s import output as k8s_output
from lib import linux_helper
from lib.workflow import ocp_common as workflow_common
from lib.workflow import netshoot_helper


def get_interfaces(params, my_output, node_name_filter=None):
    my_output.default('Get interface details', before_newline=True, underline=True)

    interfaces = {}

    for node_name in params['netshoot']:
        if node_name_filter is not None and node_name != node_name_filter:
            continue

        interfaces[node_name], error = get_node_ethernet_details(
            params,
            node_name,
            my_output
        )

        if interfaces[node_name] is None:
            return None, error

    return interfaces, None


def get_node_ethernet_details(params, node_name, my_output):
    success = params['k8s_handler'].wait_node_network_state(node_name)
    if not success:
        return None, 'Node network state collection failed: %s' % (node_name)

    nns = params['k8s_handler'].get_node_network_state(node_name)
    if nns is None:
        return None, 'Node network state collection failed: %s' % (node_name)
    
    ethernet_ifs = []

    for interface in nns['interface']:
        my_output.default('\tinterface: %s' % (interface['name']))
        if interface['type'] != 'ethernet':
            continue

        if interface['state'] == 'ignore':
            continue

        ethernet_if = {}
        ethernet_if['name'] = interface['name']
        ethernet_if['lldp_configurable'] = False
        ethernet_if['lldp_enabled'] = False
        if 'lldp_enabled' in interface:
            ethernet_if['lldp_configurable'] = True
            ethernet_if['lldp_enabled'] = interface['lldp_enabled']

        my_output.default('\t\tethtool')
        output = netshoot_helper.get_netshoot_cli(
            params,
            'ethtool -i %s' % (interface['name']),
            node_name=node_name
        )
        if output is None:
            my_output.default('aaa')
            return None, 'Ethtool failed on %s' % (ethernet_if['name'])

        ethernet_if['params'] = {}

        for line in output[node_name].strip().split('\n'):
            key = line.split(':')[0].strip()
            value = ':'.join(line.split(':')[1:]).strip()
            ethernet_if['params'][key] = value

        my_output.default('\t\tpriv flags')

        ethernet_if['flags'] = None
        output = netshoot_helper.get_netshoot_cli(
            params,
            'ethtool --show-priv-flags %s' % (ethernet_if['name']),
            node_name=node_name,
        )
        if output is not None and 'Operation not supported' not in output:
            ethernet_if['flags'] = {}
            for line in output[node_name].strip().split('\n'):
                key = line.split(':')[0].strip()
                value = ':'.join(line.split(':')[1:]).strip()
                ethernet_if['flags'][key] = value
                    
        my_output.default('\t\tstate')

        output = netshoot_helper.get_netshoot_cli(
            params,
            'ip a l %s' % (ethernet_if['name']),
            node_name=node_name,
        )
        if output is None:
            my_output.default('aaa')
            return None, 'interface state failed on %s' % (ethernet_if['name'])

        try:
            istate = linux_helper.analyze_ip_link_show_output(output[node_name])
        except BaseException:
            return None, 'interface state parse failed on %s: %s' % (ethernet_if['name'], output[node_name])

        if istate is None or len(istate) != 1:
            return None, 'interface state parse failed on %s: %s' % (ethernet_if['name'], output[node_name])
        
        ethernet_if['state'] = istate[0]

        ethernet_ifs.append(
            ethernet_if
        )

    return ethernet_ifs, None


def configure_node(params, node_name, interfaces, my_output):
    # https://edc.intel.com/content/www/us/en/design/products/ethernet/adapters-and-devices-user-guide/firmware-link-layer-discovery-protocol-fw-lldp/

    my_output.default('Disable lldp on ethernet interface fw level [%s]' % (node_name))

    for interface in interfaces:
        my_output.default('Interface state %s' % (interface['name']))
        my_output.default('- driver: %s' % (interface['params']['driver']))
        my_output.default('- version: %s' % (interface['params']['version']))
        my_output.default('- pci: %s' % (interface['params']['bus-info']))

        is_action = False
        if interface['flags'] is not None:
            if 'fw-lldp-agent' in interface['flags']:
                my_output.default('- fw-lldp-agent: %s' % (interface['flags']['fw-lldp-agent']))
                if interface['flags']['fw-lldp-agent'] == 'on':
                    is_action = True
                    my_output.default('Action: set fw-lldp-agent to off')
                    output = netshoot_helper.get_netshoot_cli(
                        params,
                        'ethtool --set-priv-flags %s %s %s' % (interface['name'], 'fw-lldp-agent', 'off'),
                        node_name=node_name
                    )
                    my_output.default(output, wrap='~~~')

            if 'disable-fw-lldp' in interface['flags']:
                my_output.default('- disable-fw-lldp: %s' % (interface['flags']['disable-fw-lldp']))
                if interface['flags']['disable-fw-lldp'] == 'off':
                    is_action = True
                    my_output.default('Action: set disable-fw-lldp to on')
                    output = netshoot_helper.get_netshoot_cli(
                        params,
                        'ethtool --set-priv-flags %s %s %s' % (interface['name'], 'disable-fw-lldp', 'on'),
                        node_name=node_name
                    )
                    my_output.default(output, wrap='~~~')

        if is_action:
            my_output.default('Interface %s [%s] - fw lldp disabled' % (interface['name'], interface['params']['bus-info']))
        else:
            my_output.default('Interface %s [%s] - no change' % (interface['name'], interface['params']['bus-info']))


def configure_nic(params, my_output):
    for node_name in params['netshoot']:
        configure_node(
            params,
            node_name,
            params['interfaces'][node_name],
            my_output
        )


def enable_nns(params, my_output, log_id=None):
    params['success'] = True
    params['error'] = None
    policy_names = []
    for node_name in params['interfaces']:
        my_output.default('Enable lldp on nmstate level [%s]' % (node_name))

        for interface in params['interfaces'][node_name]:
            if not params['include-down'] and not interface['state']['up']:
                my_output.default('Interface %s - skip on interface oper down' % (interface['name']))
                continue

            if not interface['lldp_configurable']:
                my_output.default('Interface %s - lldp not configurable' % (interface['name']))
                continue

            if interface['lldp_enabled']:
                my_output.default('Interface %s - already enabled' % (interface['name']))
                continue

            success, policy_name = params['k8s_handler'].set_nncp_interface_lldp_enabled(
                interface['name'],
                node_name=node_name,
                wait=False
            )
            if not success:
                params['success'] = False
                params['error'] = 'Failed to create nncp for %s:%s' % (node_name, interface['name'])
                return params

            my_output.default('Interface %s - enabling with nncp (%s)' % (interface['name'], policy_name))
            policy_names.append(
                policy_name
            )

    if len(policy_names) == 0:
        return params

    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    object_filter = ['names:%s' % (','.join(policy_names))]
    policies = params['k8s_handler'].get_node_network_configuration_policys(object_filter=object_filter, cache_enabled=False)
    if policies is not None:
        k8s_output_handler.print_node_network_configuration_policys_state(policies)

    success = params['k8s_handler'].wait_node_network_configuration_policies_status(
        policy_names=policy_names,
        my_output=my_output
    )
    if not success:
        my_output.error('Not all nncp finished in time')

    policies = params['k8s_handler'].get_node_network_configuration_policys(object_filter=object_filter, cache_enabled=False)
    if policies is not None:
        k8s_output_handler.print_node_network_configuration_policys_state(policies)

    if not params['delete-nncp']:
        my_output.default('Node network policies not deleted (based on user flag)')

    if params['delete-nncp']:
        my_output.default('All policies are deleted (except for progressing if any)...')
        for policy in policy_names:
            policy_info = params['k8s_handler'].get_node_network_configuration_policy(policy)
            if policy_info is None or policy_info['status'] == 'Progressing':
                my_output.default('- %s [Skipping]' % policy)
            else:
                success = params['k8s_handler'].delete_node_network_configuration_policy_mo(policy)
                if success:
                    my_output.default('- %s [Deleted]' % policy)
                else:
                    my_output.default('- %s [ERROR]' % policy)

    return params