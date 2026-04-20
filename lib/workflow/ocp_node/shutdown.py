from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow import ocp_common
from menu.common import get_confirmation


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['node', False, None, 'str', 1, None, None, None],
        ['checks', True, True, 'bool', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Graceful node shutdown', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id, ssh_required=True)
    if params is None:
        return False
    
    if len(params['node']) == 1 and params['node'] == '*':
        params['node'] = params['k8s_handler'].get_nodes_name()
        
    for node in params['node']:
        if not params['k8s_handler'].is_node(node):
            my_output.error('Node not found: %s' % (node))
            return False

    for node_name in params['node']:
        if params['checks']:
            if not ocp_common.is_cluster_ready(params['cluster']):
                return False
            
        k8s_output_handler.print_nodes_state([params['k8s_handler'].get_node(node_name)])
        success = params['k8s_handler'].set_node_cordon(node_name, my_output)
        if not success:
            return False
        
        object_filter = []
        object_filter.append('node:%s' % (node_name))
        object_filter.append('owner:!DaemonSet/*,!Node/*,!ReplicaSet/*')
        pods = params['k8s_handler'].get_pods(object_filter=object_filter, cache_enabled=False)
        if pods is None:
            my_output.error('Failed to get pods')
            return False

        success = params['k8s_handler'].evict_pods(
            pods, 
            delete_fallback=True, 
            my_output=my_output, 
            wait=True
        )
        if not success:
            my_output.default('Not all pods evicted', before_newline=True)
            if params['confirmation']:
                if not get_confirmation():
                    return False
        
        success = ocp_common.run_node_cli(
            params['k8s_handler'], 
            params['cluster'], 
            node_name, 
            'sudo shutdown -h now', 
            my_output=my_output, 
            log_id=log_id
        )
        if not success:
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Node shut down gracefully')
    return True
