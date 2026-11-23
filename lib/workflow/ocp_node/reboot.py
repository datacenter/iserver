import time
from lib import output_helper
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['node', False, None, 'list-of-str', 1, None, None, None],
        ['sequential', True, True, 'bool', None, None, None, None],
        ['max-time', True, 600, 'int', 1, 1800, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Node reboot', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id, ssh_required=True)
    if params is None:
        return False
    
    for node_name in params['node']:
        if not params['k8s_handler'].is_node(node_name):
            my_output.error('Node not found: %s' % (node_name))
            return False
        
    for node_name in params['node']:
        success = ocp_common.run_node_cli(
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
                success = ocp_common.wait_node(
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
            success = ocp_common.wait_node(
                params['k8s_handler'], 
                params['cluster'], 
                node_name, 
                my_output=my_output, 
                max_time=params['max-time']
            )
            if not success:
                return False

    return True
