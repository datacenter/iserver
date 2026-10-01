from lib import output_helper
from lib.workflow.ocp_cnv_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
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

    ocp_common.print_title(params, my_output, 'Enable Data Import Cron')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    params = ocp_common.get_operator(params, my_output)
    if params['subscription'] is None:
        my_output.default('Operator not found: %s' % (params['name']))
        return True

    params = local_common.collect_state_info(params)
    local_common.print_state_summary(params, my_output)

    if params['summary']['import_enabled']:
        my_output.default('Data import cron already enabled', before_newline=True)
        return True
    
    success = params['k8s_handler'].enable_hyperconverged_boot_image_import(
        confirmation=params['confirmation'],
        my_output=my_output,
        feature_gates=params['summary']['import_enabled_fg']
    )
    if not success:
        return False
    
    return True