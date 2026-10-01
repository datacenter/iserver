from lib import output_helper
from lib.workflow.ocp_mtv_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['namespace', True, 'openshift-mtv', 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
        ['url', False, None, 'str', None, None, None, None],
        ['username', False, None, 'str', None, None, None, None],
        ['password', False, None, 'str', None, None, None, None],
        ['ssl', True, False, 'bool', None, None, None, None],
        ['vddk', True, None, 'str', None, None, None, None]
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

    ocp_common.print_title(params, my_output, 'Create vCenter Provider')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    if not local_common.is_subscription_ready(params, my_output, details=True):
        return True

    if params['k8s_handler'].is_provider(params['namespace'], params['name']):
        my_output.default('Provider %s already defined' %  (params['name']), before_newline=True)
        return True
    
    if params['url'] is not None:
        success = params['k8s_handler'].create_provider_vcenter(
            params['namespace'],
            params['name'],
            params['url'],
            params['username'],
            params['password'],
            params['ssl'],
            vddk=params['vddk'],
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True            
        )
        if not success:
            return False        

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- provider created and ready')

    return True
