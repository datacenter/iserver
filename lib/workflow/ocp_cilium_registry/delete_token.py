from lib import output_helper
from lib.workflow.ocp_cilium_registry import common as local_common
from lib.workflow import ocp_common



def validate(params):
    rules = [
        ['token_id', False, None, 'str', None, None, None, None]
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

    registry_settings = local_common.get_registry_settings(my_output=my_output, log_id=log_id)
    if registry_settings is None:
        if my_output is not None:
            my_output.error('Isovalent registry settings not defined')
        return False

    my_output.default('Registry: %s' % registry_settings['registry'])
    my_output.default('Identity token: %s' % registry_settings['identity_token'])

    success = local_common.revoke_access_token(
        registry_settings['registry'],
        registry_settings['identity_token'],
        params['token_id'],
        my_output=my_output
    )    
    return success