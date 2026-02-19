import yaml
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_pnet import common as local_common
from lib.workflow.ocp_cilium_cni import common as cilium_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
        
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'check-verbose',
        'verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium Private Network - Get', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    my_output.default('')
    if not cilium_common.is_cilium(params, my_output):
        return False

    info = params['k8s_handler'].get_clusterwide_private_network_state(cache_enabled=False)
    if not info['enabled']:
        my_output.default('Private network %s' % (my_output.add_color('disabled', 'Red')))
        return False

    my_output.default('Private network %s' % (my_output.add_color('enabled', 'Green')))

    my_output.default('Webhook')
    if info['webhook']['enabled']:
        my_output.default('- %s' % (my_output.add_color('enabled', 'Green')))
        if info['webhook']['configured']:
            my_output.default('- mutating webhook %s %s' % (info['webhook']['name'], my_output.add_color('found', 'Green')))
        else:
            my_output.default('- mutating webhook %s %s' % (info['webhook']['name'], my_output.add_color('not found', 'Red')))

        if info['webhook']['service_found']:
            my_output.default('- service %s %s' % (info['webhook']['service_name'], my_output.add_color('found', 'Green')))
        else:
            my_output.default('- service %s %s' % (info['webhook']['service_name'], my_output.add_color('not found', 'Red')))

        if len(info['webhook']['service_endpoints']) > 0:
            my_output.default('- service endpoints: %s' % (', '.join(info['webhook']['service_endpoints'])))
        else:
            my_output.default('- service endpoints %s' % (my_output.add_color('not found', 'Red')))
    else:
        my_output.default('- %s' % (my_output.add_color('disabled', 'Red')))
        if info['webhook']['configured']:
            my_output.default('- mutating webhook %s %s' % (info['webhook']['name'], my_output.add_color('found', 'Red')))
        if info['webhook']['service_found']:
            my_output.default('- service %s %s' % (info['webhook']['service_name'], my_output.add_color('found', 'Red')))

    my_output.default(yaml.dump(info['configuration']), wrap='~~~', before_newline=True)

    networks = params['k8s_handler'].get_clusterwide_private_networks(pod_info=True, cache_enabled=False)
    if networks is None:
        my_output.error('ClusterwidePrivateNetwork CRD not found')
    else:
        k8s_output_handler.print_clusterwide_private_networks(networks)

    pods = params['k8s_handler'].get_pods_cilium_private_networks(cache_enabled=True)
    if pods is None:
        my_output.error('Failed to get pods')
    else:
        if len(pods) > 0:
            k8s_output_handler.print_pods_clusterwide_private_networks(pods)

    # agent_dbs = params['k8s_handler'].get_cilium_private_network_dbs(cache_enabled=True)
    # print(json.dumps(agent_dbs, indent=4))

    return True
