from lib import output_helper
from lib.workflow.ocp_sriov_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    new_params = {}
    allowed_keys = [
        'cluster',
        'check-verbose'
    ]
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - SRIOV - Delete Operator', before_newline=True, after_newline=True, double_underline=True)

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
        my_output.default('Subscription already deleted: %s' % (params['name']))
    else:
        if params['k8s_handler'].is_sriov_operator_config(cache_enabled=False):
            my_output.error('Delete sriov instance first')
            return False
        
        success = params['k8s_handler'].delete_sriov_subscription(
            subscription['namespace'],
            subscription['name'],
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

    success = params['k8s_handler'].delete_operator_group_in_namespace(
        params['namespace'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_pods(
        object_filter=['namespace:%s' % (params['namespace'])],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_namespace(
        params['namespace'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- SRIOV Operator subscription and csv deleted')
    my_output.default('- Operator Group deleted')
    my_output.default('- Namespace deleted')

    return True
