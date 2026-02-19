import os
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_cnv_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'channel' not in params:
        params['channel'] = 'stable'

    if 'instance' not in params:
        params['instance'] = None

    if 'filename' in params:
        try:
            if not os.path.isabs(params['filename']):
                params['filename'] = os.path.join(
                    params['base_directory'],
                    params['filename']
                )
        except BaseException:
            return None, 'Policy file path detection failed'
        
        params['instance'] = file_helper.get_file_yaml(
            params['filename']
        )
        if params['instance'] is None:
            return None, 'Yaml file read failed: %s' % (params['filename'])
        
        if 'kind' not in params['instance']:
            return None, 'Invalid yaml file content: %s' % (params['filename'])

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
        'channel',
        'instance',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Container Virtualization Operator - Create HyperConverged Instance', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    subscription = params['k8s_handler'].get_subscription_by_package(
        params['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('Cnv Operator not installed')
        return False

    my_output.default('Operator', underline=True)
    my_output.default('- subscription: %s' % (subscription['namespace_name']))
    my_output.default('- channel: %s' % (subscription['channel']))
    my_output.default('- csv: %s' % (subscription['installed_csv']))

    if not params['k8s_handler'].is_subscription_cnv_ready():
        my_output.error('Cnv Operator not ready')
        return False
        
    my_output.default('Cnv operator ready', before_newline=True)

    if params['k8s_handler'].is_hyperconverged(cache_enabled=False):
        my_output.default('HyperConverged instance already defined')

        if not params['k8s_handler'].is_hyperconverged_ready():
            my_output.error('HyperConverged not ready')
            return False
            
        my_output.default('HyperConverged instance ready', before_newline=True)
        return True
    
    if params['instance'] is None:
        subscription = params['k8s_handler'].get_subscription_by_package(
            params['name'],
            return_mo=False,
            cache_enabled=False
        )
        params['instance'] = params['k8s_handler'].get_cnv_package_channel_example(
            subscription['spec']['channel'],
            'HyperConverged'
        )
        if params['instance'] is None:
            my_output.error('Failed to get HyperConverged reference example in channel %s' % (subscription['spec']['channel']))
            return False
    
    success = params['k8s_handler'].create_hyperconverged(
        params['instance'],
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True            
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- HyperConverged instance created and ready')

    return True
