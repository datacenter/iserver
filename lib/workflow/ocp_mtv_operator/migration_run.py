from lib import output_helper
from lib.workflow.ocp_mtv_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['action', False, None, 'str', None, None, ['run'], None],
        ['plan', False, None, 'str', None, None, None, None],
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params

    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Run Migration')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    if not local_common.is_subscription_ready(params, my_output, details=True):
        return True
    
    if params['action'] == 'run':
        success = params['k8s_handler'].create_migration(
            params['__default__']['namespace'],
            params['plan'],
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True            
        )
        if not success:
            return False  
            
    my_output.default('')
    my_output.default('Completed tasks')
    if params['action'] == 'run':
        my_output.default('- migration completed successfully')

    return True