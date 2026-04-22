import json
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_cni import common as cilium_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['view', False, None, 'list-of-str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=cilium_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium Private Network - Get', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
    if params is None:
        return False
    
    info = params['k8s_handler'].get_clusterwide_private_network_state(cache_enabled=False)
    if info is None:
        my_output.error('Failed to get clusterwide private network state')
        return False
    
    k8s_output_handler.print_cilium_private_network_state(info)
    if not info['enabled']:
        return True

    if 'details' not in params['view']:
        networks = params['k8s_handler'].get_clusterwide_private_networks(pod_info=False, cache_enabled=False)
        if networks is None:
            my_output.error('ClusterwidePrivateNetwork CRD not found')
        else:
            k8s_output_handler.print_clusterwide_private_networks(networks)

    if 'details' in params['view']:
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

        agent_dbs = params['k8s_handler'].get_cilium_private_network_dbs(cache_enabled=True)
        my_output.default('Private network database', before_newline=True)
        my_output.default(json.dumps(agent_dbs, indent=4), wrap='~~~')

    return True
