from lib import output_helper
from lib.k8s import output as k8s_output
from menu.common import get_confirmation
from lib.workflow.ocp_cnv_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['wipe', True, False, 'bool', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Disable Data Import Cron')
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
        success = params['k8s_handler'].disable_hyperconverged_boot_image_import(
            confirmation=params['confirmation'],
            my_output=my_output,
            feature_gates=params['summary']['import_enabled_fg']
        )
        if not success:
            return False
    else:
        my_output.default('Data import cron already disabled', before_newline=True)
    
    if not params['wipe']:
        return True
    
    data_volumes = params['k8s_handler'].get_data_volumes(
        object_filter=['cron:true'],
        cache_enabled=False
    )
    if data_volumes is None:
        my_output.error('DataVolume crd failed')

    if len(data_volumes) == 0:
        my_output.default('No cron related data volumes found', before_newline=True)
        return True
    
    k8s_output_handler.print_data_volumes(data_volumes)

    if params['confirmation']:
        if not get_confirmation():
            return False
    
    success = True
    for data_volume in data_volumes:
        delete_success = params['k8s_handler'].delete_data_volume(
            data_volume['namespace'],
            data_volume['name'],
            my_output=my_output,
            wait=True,
            force=True
        )
        success = success and delete_success

    return success