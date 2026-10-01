from lib import output_helper
from lib.workflow.ocp_cilium_registry import common as local_common
from lib.workflow import ocp_common



def validate(params):
    rules = [
        ['registry', False, None, 'str', None, None, None, None],
        ['token', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Isovalent registry access settings')

    success = local_common.check_identity_token(
        params['registry'], 
        params['token'],
        my_output=my_output
    )
    if not success:
        return False

    success = local_common.set_identity_token(
        params['registry'], 
        params['token'],
        my_output=my_output,
        log_id=log_id
    )
    if not success:
        return False
    
    return True