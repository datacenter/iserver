import copy
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.k8s import common as local_common
from menu.common import get_confirmation
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['__id__', True, None, None, None, None, None, None],
        ['namespace', False, None, 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
        ['type', False, None, 'str', None, None, None, None],
        ['bridge', True, None, 'str', None, None, None, None],
        ['nncp-on-delete', True, False, 'bool', None, None, None, None]
    ]

    success, params, allowed_keys = ocp_common.check_parameters(params, rules, extras=['__type__'])
    if not success:
        return None, params

    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('Kubernetes Workflow - Network Attachment Definition - Delete', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    nads = local_common.get_nads(
        params['k8s_handler'],
        namespace=params['namespace'], 
        name=params['name']
    )
    if nads is None:
        my_output.error('Failed to get nads')
        return False
    
    if len(nads) == 0:
        my_output.default('Nad %s/%s already deleted' % (params['namespace'], params['name']))
    else:
        k8s_output_handler.print_nads(nads)

        if params['confirmation']:
            if not get_confirmation():
                return False

        success = True
        for nad_info in nads:
            nad_success = params['k8s_handler'].delete_nad(
                nad_info['namespace'],
                nad_info['name'],
                my_output=my_output, 
                wait=True
            )
            success = success and nad_success

        if not success:
            my_output.error('Some delete api calls failed', before_newline=True)
            return False

    if params['type'] == 'bridge' and params['nncp-on-delete']:
        my_output.default('Checking linux bridge [%s] existence...' % (params['bridge']))
        states = params['k8s_handler'].get_node_network_states(cache_enabled=False)
        if states is None:
            my_output.default('- failed to get nmstate instance')
        else:
            for item in states:
                for interface in item['interface']:
                    if interface['type'] != 'linux-bridge':
                        continue

                    if interface['name'] == params['bridge']:
                        to_print = copy.deepcopy(item)
                        to_print['interface'] = [interface]
                        k8s_output_handler.print_node_network_states_lb([to_print])

                        if len(interface['bridge_port']) > 0:
                            my_output.default('Skipping as it has members', before_newline=True)
                            continue

                        my_output.default('Deleting bridge via nncp', before_newline=True)

                        params['k8s_handler'].delete_bridge_via_node_network_configuration_policy(
                            interface['name'],
                            node=item['name'],
                            my_output=my_output,
                            confirmation=params['confirmation']
                        )

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- nad deleted')
    return True
