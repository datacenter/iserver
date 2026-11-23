from lib import output_helper
from lib.workflow.ocp_ntp import common as local_common
from lib.workflow.ocp_ntp import output as local_output
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['view', True, ['state'], 'view', None, None, ['state'], None]
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

    ocp_common.print_title(params, my_output, 'Get ntp configuration and state')
    params = ocp_common.workflow_init(params, my_output, log_id, linux_required=True)
    if params is None:
        return False

    my_output.default('Collecting data...', before_newline=True, after_newline=True)
    info = local_common.get_ocp_chrony_info(params['k8s_handler'], params['linux_handler'])
    local_output.print_ocp_chrony_info(info, my_output)

    return True
