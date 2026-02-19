from lib import output_helper
from lib.workflow import ocp_common as workflow_common
from lib.workflow.ocp_sriov_operator import policy
from lib.workflow.ocp_sriov_operator import config
from lib.workflow.ocp_access import check as ocp_check


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'namespace' not in params:
        params['namespace'] = 'openshift-sriov-network-operator'

    if 'name' not in params:
        params['name'] = 'sriov-network-operator'

    if 'channel' not in params:
        params['channel'] = 'stable'

    if 'confirmation' not in params:
        params['confirmation'] = False

    if 'wait_ready' not in params:
        params['wait_ready'] = 600

    if 'wait_not_ready' not in params:
        params['wait_not_ready'] = 180

    if 'config' not in params:
        params['config'] = {}
        params['config']['name'] = 'default'
        params['config']['injector'] = True
        params['config']['webhook'] = True

    if 'policy' not in params:
        params['policy'] = []

    if 'flags' not in params:
        params['flags'] = {}
        params['flags']['intel'] = False
        params['flags']['vfio'] = False
        params['flags']['netdevice'] = False

    if 'intel' not in params['flags']:
        params['flags']['intel'] = False

    if 'vfio' not in params['flags']:
        params['flags']['vfio'] = False

    if 'netdevice' not in params['flags']:
        params['flags']['netdevice'] = False

    if len(params['policy']) == 0:
        if params['flags']['intel']:
            if params['flags']['vfio'] and params['flags']['netdevice']:
                policy_mo = {
                    'vendor': 'intel',
		            'driver': '!ixgbe',
                    'type': 'netdevice',
                    'name': '${IFNAME}net',
                    'resource': '${IFNAME}net',
                    'vfs': '64',
                    'range': '0-31'
                }
                params['policy'].append(policy_mo)

                policy_mo = {
                    'vendor': 'intel',
		            'driver': '!ixgbe',
                    'type': 'vfio-pci',
                    'name': '${IFNAME}dpdk',
                    'resource': '${IFNAME}dpdk',
                    'vfs': '64',
                    'range': '32-63'
                }
                params['policy'].append(policy_mo)

            if params['flags']['vfio'] and not params['flags']['netdevice']:
                policy_mo = {
                    'vendor': 'intel',
		            'driver': '!ixgbe',
                    'type': 'vfio-pci',
                    'name': '${IFNAME}dpdk',
                    'resource': '${IFNAME}dpdk',
                    'vfs': '64',
                    'range': '0-31'
                }
                params['policy'].append(policy_mo)

            if not params['flags']['vfio'] and params['flags']['netdevice']:
                policy_mo = {
                    'vendor': 'intel',
		            'driver': '!ixgbe',
                    'type': 'netdevice',
                    'name': '${IFNAME}net',
                    'resource': '${IFNAME}net',
                    'vfs': '64',
                    'range': '0-31'
                }
                params['policy'].append(policy_mo)

    for policy_mo in params['policy']:
        if 'interface' not in policy_mo and 'vendor' not in policy_mo:
            return None, 'sriov.policy.interface or sriov.policy.vendor required'

        if 'interface' in policy_mo and policy_mo['interface'] is not None:
            policy_mo['vendor'] = None
            policy_mo['driver'] = None

        if 'vendor' in policy_mo and policy_mo['vendor'] is not None:
            policy_mo['interface'] = None

        if 'driver' not in policy_mo:
            policy_mo['driver'] = None

        if policy_mo['interface'] is None and policy_mo['vendor'] is None:
            return None, 'sriov.policy.interface or sriov.policy.vendor value required'

        if 'type' not in policy_mo:
            return None, 'sriov.policy.type required'

        if policy_mo['type'] not in ['netdevice', 'vfio-pci']:
            return None, 'sriov.policy.type must be one of netdevice, vfio-pci'

        if 'name' not in policy_mo:
            if policy_mo['type'] == 'netdevice':
                if 'interface' in policy_mo:
                    policy_mo['name'] = '%snet' % (policy_mo['interface'])
                else:
                    policy_mo['name'] = '${IFNAME}net'

            if policy_mo['type'] == 'vfio-pci':
                if 'interface' in policy_mo:
                    policy_mo['name'] = '%sdpdk' % (policy_mo['interface'])
                else:
                    policy_mo['name'] = '${IFNAME}net'

        if 'resource' not in policy_mo:
            if policy_mo['type'] == 'netdevice':
                if 'interface' in policy_mo:
                    policy_mo['resource'] = '%snet' % (policy_mo['interface'])
                else:
                    policy_mo['resource'] = '${IFNAME}net'

            if policy_mo['type'] == 'vfio-pci':
                if 'interface' in policy_mo:
                    policy_mo['resource'] = '%sdpdk' % (policy_mo['interface'])
                else:
                    policy_mo['resource'] = '${IFNAME}net'

        if 'vfs' not in policy_mo:
            return None, 'sriov.policy.vfs required'

        try:
            vfs = int(policy_mo['vfs'])
        except BaseException:
            vfs = None

        if vfs is None:
            return None, 'sriov.policy.vfs required'

        if 'range' not in policy_mo:
            policy_mo['range'] = None

    return params, None

def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['mgmt-fixup'] = True
    ocp_check_params['verbose'] = True
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return False
    
    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler
    params['linux_handler'] = ocp_params['data']['management_linux_handler']

    params = workflow_common.add_operator(
        params,
        my_output=my_output
    )
    if not params['success']:
        my_output.error(params['error'])
        return False

    success = params['k8s_handler'].wait_subscription_sriov_ready(configured=False, my_output=my_output)
    if not success:
        return False

    success, error = config.run(params, my_output)
    if not success:
        my_output.error(error)
        return False

    success = params['k8s_handler'].wait_subscription_sriov_ready(configured=True, my_output=my_output)
    if not success:
        return False

    success, created, error = policy.run(params, my_output)
    if not success:
        my_output.error(error)
        return False

    if created:
        my_output.default('Wait for node reload due to sriov network node policy created')

        success = params['k8s_handler'].wait_nodes_not_ready(
            max_time=params['wait_not_ready'],
            my_output=my_output
        )
        if success:
            my_output.default('Wait for all nodes ready')
            success = params['k8s_handler'].wait_nodes_ready(
                max_time=params['wait_ready'],
                my_output=my_output
            )
            if not success:
                return False

            success = params['k8s_handler'].wait_subscription_sriov_ready(ds_enable=True, my_output=my_output)
            if not success:
                return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- SR-IOV Operator installed')
    if len(params['policy']) > 0:
        my_output.default('- SR-IOV Node Network Policy defined')

    return True
