from lib import filter_helper
from lib import output_helper
from lib.workflow.ocp_vast_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['filename', True, None, 'file-k8s', None, None, 'VastCSIDriver', None],
        ['name', True, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules, allow_kwargs=True)
    if not success:
        return None, params

    success, error = ocp_common.check_param_options(params, ['filename'], ['name'])
    if not success:
        return None, error
            
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Delete Driver')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    state = local_common.check_state(
        params, 
        my_output,
        check_ready=True
    )
    if not state['installed']:
        return True

    if not state['ready']:
        my_output.error('VAST operator not ready')
        return False
    
    if params['filename'] is not None:
        body = ocp_common.get_k8s_body(params['filename'], 'VastCSIDriver', my_output)
        if body is None:
            return False
        
        params['name'] = filter_helper.get(body, 'metadata:name')

    success = params['k8s_handler'].delete_vast_driver(
        params['__default__']['namespace'],
        params['name'],
        my_output=my_output, 
        wait=params['wait']
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- VAST CSI driver deleted')

    return True
