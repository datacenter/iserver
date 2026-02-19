from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_node import common as local_common
from lib.workflow import ocp_common as global_common
from lib.workflow.ocp_node import reboot
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'node' not in params or len(params['node']) == 0:
        return None, 'nodes required'

    if 'pre' not in params:
        params['pre'] = True

    if not isinstance(params['pre'], bool):
        return None, 'pre param must be true or false'

    if 'post' not in params:
        params['post'] = True

    if not isinstance(params['post'], bool):
        return None, 'post param must be true or false'
        
    if 'confirmation' not in params:
        params['confirmation'] = True

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'node',
        'pre',
        'post',
        'confirmation',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Graceful node restart (reload)', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
    if len(params['node']) == 1 and params['node'] == '*':
        params['node'] = params['k8s_handler'].get_nodes_name()
        
    for node in params['node']:
        if not params['k8s_handler'].is_node(node):
            my_output.error('Node not found: %s' % (node))
            return False

    for node_name in params['node']:
        if params['pre']:
            if not global_common.is_cluster_ready(params['cluster']):
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
        
        child_params = {}
        child_params['cluster'] = params['cluster']
        child_params['node'] = [node_name]
        child_params['check-verbose'] = False
        child_params['confirmation'] = params['confirmation']
        success = reboot.run(child_params, log_id=log_id)
        if not success:
            return False

        success = params['k8s_handler'].set_node_uncordon(node_name, my_output)
        if not success:
            return False
        
        k8s_output_handler.print_nodes_state([params['k8s_handler'].get_node(node_name)])

        if params['post']:
            my_output.default('Wait for mcp ready...')
            if not params['k8s_handler'].wait_machine_config_pool_ready(max_time=600):
                my_output.error('Timed out')
                return False
            
            my_output.default('Wait for cluster operators available...')
            if not params['k8s_handler'].wait_cluster_operators_available(max_time=600):
                my_output.error('Timed out')
                return False
            
            if not global_common.is_cluster_ready(params['cluster']):
                return False
                
    return True
