import time
from lib import output_helper
from lib.workflow.ocp_node import common as local_common
from lib.workflow import ocp_common as global_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'node' not in params or len(params['node']) == 0:
        return None, 'nodes required'

    if 'wait' not in params:
        params['wait'] = True

    if 'sequential' not in params:
        params['sequential'] = True

    if 'max-time' not in params:
        params['max-time'] = 600

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'node',
        'wait',
        'sequential',
        'max-time',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Node reboot', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
    for node_name in params['node']:
        if not params['k8s_handler'].is_node(node_name):
            my_output.error('Node not found: %s' % (node_name))
            return False
        
    for node_name in params['node']:
        success = global_common.run_node_cli(
            params['k8s_handler'], 
            params['cluster'], 
            node_name, 
            'sudo reboot', 
            my_output=my_output, 
            log_id=log_id
        )
        if not success:
            return False

        if params['sequential']:
            if params['wait']:
                time.sleep(10)
                success = global_common.wait_node(
                    params['k8s_handler'], 
                    params['cluster'], 
                    node_name, 
                    my_output=my_output, 
                    max_time=params['max-time']
                )
                if not success:
                    return False

    if not params['sequential'] and params['wait']:
        time.sleep(10)
        for node_name in params['node']:
            success = global_common.wait_node(
                params['k8s_handler'], 
                params['cluster'], 
                node_name, 
                my_output=my_output, 
                max_time=params['max-time']
            )
            if not success:
                return False

    return True
