from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_mtv_operator import common as local_common
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
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Delete Operator')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    subscription = params['k8s_handler'].get_subscription_by_package(
        params['__default__']['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('Subscription already deleted: %s' % (params['__default__']['name']))
    else:
        if params['k8s_handler'].is_any_forklift_controller(cache_enabled=False):
            my_output.error('Delete forklift controller instance first')
            return False

        if not local_common.is_mtv_unconfigured(params, my_output, k8s_output_handler):
            return False
        
        success = params['k8s_handler'].delete_mtv_subscription(
            subscription['namespace'],
            subscription['name'],
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

    object_filter = []
    object_filter.append('namespace:%s' % (params['__default__']['namespace']))
    object_filter.append('owner:Job/*')
    pods = params['k8s_handler'].get_pods(
        object_filter=object_filter
    )
    if pods is None:
        my_output.error('Failed to get pods information')
        return False
    
    for pod in pods:
        success = params['k8s_handler'].delete_pod(
            pod['namespace'], 
            pod['name'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False
            
    success = params['k8s_handler'].delete_operator_group_in_namespace(
        params['__default__']['namespace'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    if params['__default__']['delete-namespace']:
        success = params['k8s_handler'].delete_namespace(
            params['__default__']['namespace'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Subscription and csv deleted')
    my_output.default('- Operator Group deleted')
    my_output.default('- Namespace deleted')

    return True