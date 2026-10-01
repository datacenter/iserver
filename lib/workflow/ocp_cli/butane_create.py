from lib import output_helper
from lib.workflow import ocp_common
from lib.workflow.ocp_cli import common as local_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['url', True, 'https://mirror.openshift.com/pub/openshift-v4/clients/butane/latest/butane-amd64', 'str', None, None, None, None],
        ['overwrite', False, False, 'bool', None, None, None, None]
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

    ocp_common.print_title(params, my_output, 'Add butane')
    params = ocp_common.workflow_init(params, my_output, log_id, ssh_required=True)
    if params is None:
        return False
    
    success = params['ssh_handler'].upload_binary_from_source(
        'butane', 
        params['url'], 
        target_path='/usr/local/bin', 
        chmod=True, 
        test='butane --version',
        overwrite=params['overwrite'],
        my_output=my_output
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- butane installed')
    return True