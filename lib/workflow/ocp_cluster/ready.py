from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cluster import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'mcp' not in params:
        params['mcp'] = True

    if not isinstance(params['mcp'], bool):
        return None, 'mcp param must be true or false'
    
    if 'node' not in params:
        params['node'] = True

    if not isinstance(params['node'], bool):
        return None, 'node param must be true or false'

    if 'co' not in params:
        params['co'] = True

    if not isinstance(params['co'], bool):
        return None, 'co param must be true or false'

    if 'break-on-error' not in params:
        params['break-on-error'] = True

    if not isinstance(params['break-on-error'], bool):
        return None, 'co param must be true or false'

    if 'verbose' not in params:
        params['verbose'] = True

    if 'check-verbose' not in params:
        params['check-verbose'] = False

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'mcp',
        'node',
        'co',
        'break-on-error',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    if params['verbose']:
        my_output.default('OpenShift Workflow - Cluster readiness check', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
    ready = True

    if params['mcp']:
        if params['verbose']:
            my_output.default('Checking machine config pool')

        mcp = params['k8s_handler'].get_machine_config_pools(cache_enabled=False)
        if mcp is None:
            ready = False
            if params['verbose']:
                my_output.error('Failed to get machine config pools')

            if params['break-on-error']:
                return False

        if mcp is not None:
            if params['k8s_handler'].is_machine_config_pools_ready(machine_config_pools=mcp):
                if params['verbose']:
                    my_output.default('All updated')
            else:
                ready = False
                if params['verbose']:
                    k8s_output_handler.print_machine_config_pools(mcp)
                    my_output.error('Machine config pools not ready')

                if params['break-on-error']:
                    return False
                
    if params['node']:
        if params['verbose']:
            my_output.default('Checking nodes')

        nodes = params['k8s_handler'].get_nodes(cache_enabled=False)
        if nodes is None:
            ready = False
            if params['verbose']:
                my_output.error('Failed to get nodes')

            if params['break-on-error']:
                return False

        if nodes is not None:      
            if params['k8s_handler'].are_nodes_ready(cache_enabled=True):
                if params['verbose']:
                    my_output.default('All ready')
            else:
                ready = False
                if params['verbose']:
                    k8s_output_handler.print_nodes_state(nodes)
                    my_output.error('Not all nodes are ready')

                if params['break-on-error']:
                    return False            
            
    if params['co']:
        if params['verbose']:
            my_output.default('Checking cluster operators')

        operators = params['k8s_handler'].get_cluster_operators(cache_enabled=False)
        if operators is None:
            ready = False
            if params['verbose']:
                my_output.error('Failed to get cluster operators')

            if params['break-on-error']:
                return False

        if operators is not None:      
            if params['k8s_handler'].are_cluster_operators_available(operators=operators):
                if params['verbose']:
                    my_output.default('All available')
            else:
                ready = False
                if params['verbose']:
                    k8s_output_handler.print_cluster_operators(operators)

                if params['break-on-error']:
                    return False     
                
    return ready
