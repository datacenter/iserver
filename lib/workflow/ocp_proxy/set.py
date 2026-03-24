from lib import ip_helper
from lib import output_helper
from lib import filter_helper
from lib.workflow import ocp_common
from lib.workflow.ocp_proxy import common as local_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['noproxy', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
    
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - HTTP Proxy Settings', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if params['noproxy'] is not None:
        found = params['k8s_handler'].is_noproxy(params['noproxy'], my_output=my_output)
        if not found:
            success = params['k8s_handler'].add_noproxy(
                params['noproxy'],
                confirmation=params['confirmation'], 
                my_output=my_output,
                wait=params['wait']
            )
            if not success:
                return False
            
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- cluster http proxy settings configured')
    return True
