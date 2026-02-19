from lib import output_helper
from lib.workflow.ocp_gpu_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
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
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def check_resources(params, my_output):
    policies = params['k8s_handler'].get_cluster_policies(cache_enabled=False)
    if policies is None:
        my_output.error('Failed to get nvidia cluster policies - not sure if delete workflow can proceed')
        return False
    
    if len(policies) > 0:
        my_output.error('Delete nvidia cluster policies first')
        return False
    
    my_output.default('No nvidia cluster policy found')
    return True

def delete_subscription(params, my_output):
    subscription = params['k8s_handler'].get_subscription_by_package(
        params['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('Subscription already deleted: %s' % (params['name']))
        return True

    if not check_resources(params, my_output):
        return False

    success = params['k8s_handler'].delete_gpu_subscription(
        subscription['namespace'],
        subscription['name'],
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - GPU Operator - Delete Operator', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not delete_subscription(params, my_output):
        return False
    
    success = params['k8s_handler'].delete_operator_group(
        params['namespace'],
        params['operator-group-name'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    if params['delete-namespace']:
        success = params['k8s_handler'].delete_namespace(
            params['namespace'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- GPU Operator removed')

    return True
