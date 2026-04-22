from lib import output_helper
from lib.workflow.ocp_intersight_operator import common as local_common
from lib.workflow.ocp_intersight_operator import disable_plugin
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
    my_output.default('OpenShift Workflow - Cisco Intersight Operator - Delete Instance', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    if params['initialize']:
        params = ocp_common.workflow_init(params, my_output, log_id)
        if params is None:
            return False

    subscription = ocp_common.get_subscription(
        params['k8s_handler'],
        params['__default__']['name'],
        my_output=my_output,
        brief=True
    )
    if subscription is None:
        return True

    if not params['k8s_handler'].is_any_intersight(cache_enabled=False):
        my_output.default('CiscoIntersight instance %s' % (my_output.add_color('already deleted', 'Green')))
        return True
    
    cparams = {}
    cparams['cluster'] = params['cluster']
    cparams['k8s_handler'] = params['k8s_handler']
    cparams['initialize'] = False
    cparams['silent'] = True
    response = disable_plugin.run(cparams, log_id=log_id)
    if response is None:
        my_output.error('Failed to disable ui plugin')
        return False
    
    success = params['k8s_handler'].delete_intersights(
        my_output=my_output,
        wait=params['wait']
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Cisco intersight instance deleted')
    return True
