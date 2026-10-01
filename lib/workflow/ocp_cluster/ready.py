from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cluster import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['mcp', True, True, 'bool', None, None, None, None],
        ['node', True, True, 'bool', None, None, None, None],
        ['co', True, True, 'bool', None, None, None, None],
        ['break-on-error', True, True, 'bool', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Cluster readiness check')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    ready = True

    if params['mcp']:
        my_output.default('Checking machine config pool')

        mcp = params['k8s_handler'].get_machine_config_pools(cache_enabled=False)
        if mcp is None:
            ready = False
            my_output.error('Failed to get machine config pools')

            if params['break-on-error']:
                return False

        if mcp is not None:
            if params['k8s_handler'].is_machine_config_pools_ready(machine_config_pools=mcp):
                my_output.default('All updated')
            else:
                ready = False
                k8s_output_handler.print_machine_config_pools(mcp)
                my_output.error('Machine config pools not ready')

                if params['break-on-error']:
                    return False
                
    if params['node']:
        my_output.default('Checking nodes')

        nodes = params['k8s_handler'].get_nodes(cache_enabled=False)
        if nodes is None:
            ready = False
            my_output.error('Failed to get nodes')

            if params['break-on-error']:
                return False

        if nodes is not None:      
            if params['k8s_handler'].are_nodes_ready(cache_enabled=True):
                my_output.default('All ready')
            else:
                ready = False
                k8s_output_handler.print_nodes_state(nodes)
                my_output.error('Not all nodes are ready')

                if params['break-on-error']:
                    return False            
            
    if params['co']:
        my_output.default('Checking cluster operators')

        operators = params['k8s_handler'].get_cluster_operators(cache_enabled=False)
        if operators is None:
            ready = False
            my_output.error('Failed to get cluster operators')

            if params['break-on-error']:
                return False

        if operators is not None:      
            if params['k8s_handler'].are_cluster_operators_available(operators=operators):
                my_output.default('All available')
            else:
                ready = False
                k8s_output_handler.print_cluster_operators(operators)

                if params['break-on-error']:
                    return False     
                
    return ready