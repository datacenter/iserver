import os
from lib import file_helper
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_gpu_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'policy' not in params:
        params['policy'] = None

    if 'filename' in params and params['filename'] is not None:
        try:
            if not os.path.isabs(params['filename']):
                params['filename'] = os.path.join(
                    params['base_directory'],
                    params['filename']
                )
        except BaseException:
            return None, 'Policy file path detection failed'
        
        params['policy'] = file_helper.get_file_yaml(
            params['filename']
        )
        if params['policy'] is None:
            return None, 'Yaml file read failed: %s' % (params['filename'])
        
        if 'kind' not in params['policy']:
            return None, 'Invalid yaml file content: %s' % (params['filename'])

    if 'confirmation' not in params:
        params['confirmation'] = False

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
        'policy',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - GPU Operator - Create NVIDIA Cluster Policy', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if params is None:
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
        my_output.error('GPU Operator not installed')
        return False

    if params['k8s_handler'].is_any_cluster_policy(cache_enabled=False):
        my_output.default('NVIDIA Cluster Policy already defined')
        return True

    if params['policy'] is None:
        params['policy'] = params['k8s_handler'].get_gpu_package_channel_example(
            subscription['spec']['channel'],
            'ClusterPolicy'
        )
        if params['policy'] is None:
            my_output.error('Failed to get Cluster Policy reference example in channel %s' % (subscription['spec']['channel']))
            return False
    
    success = params['k8s_handler'].create_cluster_policy(
        params['policy'],
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    policies = params['k8s_handler'].get_cluster_policies()
    if policies is None:
        my_output.error('Failed to get nvidia cluster policy')
        return True
    
    k8s_output_handler.print_cluster_policies(policies)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- NVIDIA Cluster Policy created')

    return True
