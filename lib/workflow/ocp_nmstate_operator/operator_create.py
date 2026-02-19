import os
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_nmstate_operator import common as local_common


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
            return None, 'Instance file path detection failed'
        
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
    my_output.default('OpenShift Workflow - NMState Operator - Create Operator', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if params['k8s_handler'].is_nmstate_subscription(params['namespace'], params['name']):
        my_output.default('NMState Operator already created')
    else:
        success = params['k8s_handler'].create_namespace(
            params['namespace'],
            confirmation=params['confirmation'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

        success = params['k8s_handler'].create_operator_group(
            params['namespace'], 
            name=params['operator-group-name'],
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

        success = params['k8s_handler'].create_nmstate_subscription(
            params['namespace'], 
            params['name'], 
            channel=params['channel'],
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True            
        )
        if not success:
            return False

    if params['k8s_handler'].is_any_nmstate(cache_enabled=False):
        my_output.default('NMState instance already defined')
        return True
    
    if params['instance'] is None:
        subscription = params['k8s_handler'].get_subscription_by_package(
            params['name'],
            return_mo=False,
            cache_enabled=False
        )
        params['instance'] = params['k8s_handler'].get_nmstate_package_channel_example(
            subscription['spec']['channel'],
            'NMState'
        )
        if params['instance'] is None:
            my_output.error('Failed to get NMState reference example in channel %s' % (subscription['spec']['channel']))
            return False
    
    success = params['k8s_handler'].create_nmstate(
        params['instance'],
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True            
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Namespace created')
    my_output.default('- Operator Group created')
    my_output.default('- NMState Operator installed and configured')

    return True
