from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.k8s import common as local_common
from menu.common import get_confirmation
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['__id__', True, None, None, None, None, None, None],
        ['name', True, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules, extras=['__type__'])
    if not success:
        return None, params

    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params(), copy_handler=False), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'PV - Delete released')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    pvs = local_common.get_pvs(
        params['k8s_handler'],
        name=params['name'],
        released=True
    )
    if pvs is None:
        my_output.error('Failed to get pvs')
        return False
    
    if len(pvs) == 0:
        my_output.default('No pv found')
        return True
    
    k8s_output_handler.print_pvs(pvs)

    if params['confirmation']:
        if not get_confirmation():
            return False

    my_output.default('Delete pv', before_newline=True)

    success = True
    for pv_info in pvs:
        pv_success = params['k8s_handler'].delete_pv(
            pv_info['name'],
            my_output=my_output,
            wait=True
        )
        success = success and pv_success

    if not success:
        my_output.error('Some delete api calls failed', before_newline=True)
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- pv deleted')
    return True
