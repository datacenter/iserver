import json
from lib import ip_helper
from lib import iaccount_helper
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.intersight import helper as intersight_helper
from lib.workflow.ocp_imm import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'iaccount' not in params or params['iaccount'] is None:
        return None, 'Intersight account name required'

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    iaccount_handler = iaccount_helper.IntersightAccount()
    iaccount_configuration = iaccount_handler.get_iaccount_configuration(params['iaccount'])
    if iaccount_configuration is None:
        return None, 'Intersight account not found'

    params['iaccount_key'] = iaccount_configuration['keyid']
    
    allowed_keys = [
        'cluster',
        'iaccount',
        'iaccount_key',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def get_server_with_mac(servers, mac):
    for server in servers:
        for server_mac in server['MacAddressInfo']:
            if ip_helper.is_mac_equal(mac, server_mac['MacAddress']):
                return server
            
    return None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Intersight Hardware - Discovery', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    success = params['k8s_handler'].is_subscription_nmstate_ready(with_instance=True)
    if not success:
        my_output.error('NMState not ready')
        return False
    
    my_output.default('NMState ready')

    states = params['k8s_handler'].get_node_network_states(cache_enabled=False)
    if states is None:
        my_output.error('Failed to get nmstate')
        return False
    
    my_output.default('Cluster node physical interfaces', before_newline=True, after_newline=True)
    k8s_output_handler.print_node_network_state_ethernet(states, brief=True)

    my_output.default('Collect Intersight servers information', before_newline=True, underline=True)
    servers = intersight_helper.get_all_servers_net(
        params['iaccount'],
        1,
        log_id=log_id,
        silent=False
    )
    if servers is None:
        my_output.error(
            'Failed to collect servers info'
        )
        return False

    my_output.default('Derive Node to Server Mapping', before_newline=True, underline=True)
    node_to_server = {}
    node_names = params['k8s_handler'].get_nodes_name()
    if node_names is None:
        my_output.error('Failed to get nodes name')
        return False
    
    for node_name in node_names:
        my_output.default('Node [%s]' % (node_name))
        for state in states:
            if state['name'] != node_name:
                continue

            for interface in state['interface']:
                if interface['type'] != 'ethernet':
                    continue

                if interface['state'] == 'ignore':
                    continue

                server = get_server_with_mac(servers, interface['mac'])
                if server is not None:
                    node_to_server[node_name] = server
                    my_output.default('- Moid: %s' % (server['Moid']))
                    my_output.default('- RegDevId: %s' % (server['RegisteredDeviceMoid']))
                    my_output.default('- Name: %s' % (server['Name']))
                    my_output.default('- Model: %s' % (server['Model']))
                    my_output.default('- Serial: %s' % (server['Serial']))
                    my_output.default('- CIMC IP: %s' % (server['ManagementIp']))
                    break

            if state['name'] in node_to_server:
                break

    my_output.default('Set Kubernetes Annotation', before_newline=True, underline=True)
    for node_name in node_to_server:
        annotation_key = 'intersight-%s' % (ip_helper.get_string_md5(params['iaccount_key']))
        annotation_value = node_to_server[node_name]['Moid']

        if not params['k8s_handler'].add_node_annotation(node_name, annotation_key, annotation_value):
            my_output.error('Node [%s] annotation failed' % (node_name))
            return False

        my_output.default('- node [%s] annotation key [%s] value [%s]' % (node_name, annotation_key, annotation_value))

        if node_to_server[node_name]['RegisteredDeviceMoid'] is not None:
            annotation_key = 'intersight-dev-%s' % (ip_helper.get_string_md5(params['iaccount_key']))
            annotation_value = node_to_server[node_name]['RegisteredDeviceMoid']

            if not params['k8s_handler'].add_node_annotation(node_name, annotation_key, annotation_value):
                my_output.error('Node [%s] annotation failed' % (node_name))
                return False

            my_output.default('- node [%s] annotation key [%s] value [%s]' % (node_name, annotation_key, annotation_value))

        annotation_key = 'server-imc'
        annotation_value = node_to_server[node_name]['ManagementIp']

        if not params['k8s_handler'].add_node_annotation(node_name, annotation_key, annotation_value):
            my_output.error('Node [%s] annotation failed' % (node_name))
            return False

        my_output.default('- node [%s] annotation key [%s] value [%s]' % (node_name, annotation_key, annotation_value))

        annotation_key = 'server-name'
        annotation_value = node_to_server[node_name]['Name']

        if not params['k8s_handler'].add_node_annotation(node_name, annotation_key, annotation_value):
            my_output.error('Node [%s] annotation failed' % (node_name))
            return False

        my_output.default('- node [%s] annotation key [%s] value [%s]' % (node_name, annotation_key, annotation_value))

        annotation_key = 'server-serial'
        annotation_value = node_to_server[node_name]['Serial']

        if not params['k8s_handler'].add_node_annotation(node_name, annotation_key, annotation_value):
            my_output.error('Node [%s] annotation failed' % (node_name))
            return False

        my_output.default('- node [%s] annotation key [%s] value [%s]' % (node_name, annotation_key, annotation_value))

        annotation_key = 'server-model'
        annotation_value = node_to_server[node_name]['Model']

        if not params['k8s_handler'].add_node_annotation(node_name, annotation_key, annotation_value):
            my_output.error('Node [%s] annotation failed' % (node_name))
            return False

        my_output.default('- node [%s] annotation key [%s] value [%s]' % (node_name, annotation_key, annotation_value))

    return True
