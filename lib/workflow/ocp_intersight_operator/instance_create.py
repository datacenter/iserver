from lib import output_helper
from lib.workflow.ocp_intersight_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['ucs-tool', True, False, 'bool', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cisco Intersight Operator - Define Instance', before_newline=True, after_newline=True, double_underline=True)

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
        return False
    
    instances = params['k8s_handler'].get_intersights(cache_enabled=False)
    if instances is None:
        my_output.error('Failed to get CiscoIntersight objects')
        return False
    
    if len(instances) > 1:
        my_output.error('Unsupported CiscoIntersight objects count: %s' % (len(instances)))
        return False
    
    if len(instances) == 0:
        body = params['k8s_handler'].get_intersight_body(
            params['__default__']['namespace'],
            params['__default__']['instance'],
            ucs_tool=params['ucs-tool']
        )
        success = params['k8s_handler'].create_intersight(
            body, 
            my_output=my_output, 
            confirmation=params['confirmation'], 
            wait=params['wait']
        )
        if not success:
            return False
        
    if len(instances) == 1:
        body = params['k8s_handler'].get_intersight_body(
            instances[0]['namespace'],
            instances[0]['name'],
            ucs_tool=params['ucs-tool'],
            resource_version=instances[0]['resource_version'],
        )
        success = params['k8s_handler'].update_intersight(
            body, 
            my_output=my_output, 
            confirmation=params['confirmation']
        )
        if not success:
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Cisco intersight ready')
    return True