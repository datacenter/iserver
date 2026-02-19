from lib import output_helper
from lib.workflow.ocp_mtv_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'provider' not in params or params['provider'] is None:
        return None, 'Provider name required'

    if 'vc-url' not in params:
        params['vc-url'] = None

    if 'vc-user' not in params:
        params['vc-user'] = None

    if 'vc-pass' not in params:
        params['vc-pass'] = None

    if 'vc-ssl' not in params:
        params['vc-ssl'] = False

    if 'vddk' not in params:
        params['vddk'] = None

    if params['vc-url'] is not None:
        if params['vc-user'] is None:
            return None, 'vcetner username required'
        
        if params['vc-pass'] is None:
            return None, 'vcetner password required'

    if 'confirmation' not in params:
        params['confirmation'] = True

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
        'provider',
        'vc-url',
        'vc-user',
        'vc-pass',
        'vc-ssl',
        'vddk',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Migration Toolkit for Virtualization Operator - Create Provider', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_subscription_ready(params, my_output, details=True):
        return False
    
    if not local_common.is_instance_ready(params, my_output):
        return False

    if params['k8s_handler'].is_provider(params['namespace'], params['provider']):
        my_output.default('Provider %s already defined' %  (params['provider']), before_newline=True)
        return True
    
    if params['vc-url'] is not None:
        success = params['k8s_handler'].create_provider_vcenter(
            params['namespace'],
            params['provider'],
            params['vc-url'],
            params['vc-user'],
            params['vc-pass'],
            params['vc-ssl'],
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
