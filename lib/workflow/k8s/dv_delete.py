from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.k8s import common as local_common
from menu.common import get_confirmation
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['__id__', True, None, None, None, None, None, None],
        ['namespace', False, None, 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
        ['unused', True, False, 'bool', None, None, None, None],
        ['force', True, False, 'bool', None, None, None, None]
    ]

    success, params, allowed_keys = ocp_common.check_parameters(params, rules, extras=['__type__'])
    if not success:
        return None, params

    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Data Volume - Delete', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    dvs = local_common.get_dvs(
        params['k8s_handler'],
        namespace=params['namespace'], 
        name=params['name'],
        unused=params['unused']
    )
    if dvs is None:
        my_output.error('Failed to get dvs')
        return False
    
    if len(dvs) == 0:
        my_output.default('No data volume found')
        return True
    
    k8s_output_handler.print_data_volumes(dvs)

    if params['confirmation']:
        if not get_confirmation():
            return False

    if not params['force']:
        used = []
        for dv_info in dvs:
            if dv_info['used']:
                used.append(dv_info)

        if len(used) > 0:
            my_output.default('Skipped (used) delete data volume', before_newline=True)
            for item in used:
                my_output.default('- %s/%s' % (item['namespace'], item['name']))

    for dv_info in dvs:
        if dv_info['used'] and not params['force']:
            continue

        success = params['k8s_handler'].delete_data_volume(
            dv_info['namespace'], 
            dv_info['name'], 
            my_output=my_output, 
            wait=True, 
            force=params['force']
        )
        if not success:
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- dv deleted')
    return True
