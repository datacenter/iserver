from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_mtv_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'provider' not in params:
        return None, 'Provider name required'

    if 'url' not in params:
        return None, 'Url required'

    if 'username' not in params:
        return None, 'Username required'

    if 'password' not in params:
        return None, 'Password required'

    if 'ssl' not in params:
        params['ssl'] = False

    if 'vddk' not in params:
        params['vddk'] = None

    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'wait' not in params:
        params['wait'] = True

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'type',
        'provider',
        'url',
        'username',
        'password',
        'ssl',
        'vddk',
        'wait',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Migration Toolkit for Virtualization Operator - Create vCenter Provider', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_subscription_ready(params, my_output, details=True):
        return True

    if params['k8s_handler'].is_provider(params['namespace'], params['provider']):
        my_output.default('Provider %s already defined' %  (params['provider']), before_newline=True)
        return True
    
    if params['url'] is not None:
        success = params['k8s_handler'].create_provider_vcenter(
            params['namespace'],
            params['provider'],
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
