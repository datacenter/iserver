from lib import output_helper
from lib.workflow.ocp_cilium_registry import common as local_common
from lib.workflow import ocp_common



def validate(params):
    rules = []
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

    success = local_common.check_registry_access(
        my_output=my_output, 
        log_id=log_id
    )

    return success