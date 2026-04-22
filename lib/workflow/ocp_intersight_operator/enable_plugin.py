from lib import filter_helper
from lib import output_helper
from lib.workflow.ocp_intersight_operator import common as local_common
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
    my_output.default('OpenShift Workflow - Cisco Intersight Operator - Enable UI plugin', before_newline=True, after_newline=True, double_underline=True)

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
        my_output.error('Create CiscoIntersight instance first')
        return False
    
    console = params['k8s_handler'].get_operator_console('cluster', return_mo=True, cache_enabled=False)
    if console is None:
        my_output.error('Failed to get operator console information')
        return False
    
    plugins = filter_helper.get(console, 'spec:plugins', on_error=[], on_none=[])
    if 'intersight-plugin' in plugins:
        my_output.default('Intersight ui plugin %s' % (my_output.add_color('already enabled', 'Green')))
        return True
    
    body = params['k8s_handler'].copy_managed_object_base(console)
    body['spec']['plugins'] = filter_helper.get(console, 'spec:plugins', on_error=[], on_none=[])
    body['spec']['plugins'].append('intersight-plugin')

    success = params['k8s_handler'].update_operator_console(
        body,
        my_output=my_output,
        confirmation=params['confirmation']
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Cisco intersight ui plugin enabled')    
    return True
