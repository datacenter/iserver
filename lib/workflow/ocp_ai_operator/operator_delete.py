from lib import output_helper
from lib.workflow.ocp_ai_operator import common as local_common
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
        if params['k8s_handler'].is_any_data_science_cluster(cache_enabled=False):
            my_output.error('Data science cluster must be deleted first')
            return False
        
        success = params['k8s_handler'].delete_data_science_cluster_initializations(
            my_output=my_output,
            wait=True
        )
        if not success:
            return False
        
        success = params['k8s_handler'].delete_auths(
            my_output=my_output,
            wait=True
        )
        if not success:
            return False
        
        success = params['k8s_handler'].delete_image_streams(
            object_filter=['namespace:%s' % (params['__default__']['application-namespace'])], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

        success = params['k8s_handler'].delete_ods_subscription(
            subscription['namespace'],
            subscription['name'],
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

    success = params['k8s_handler'].delete_build_configs(
        object_filter=['namespace:%s' % (params['__default__']['application-namespace'])], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_services(
        object_filter=['namespace:%s' % (params['__default__']['application-namespace'])], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].delete_operator_group(
        params['__default__']['namespace'],
        params['__default__']['operator-group-name'],
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

        success = params['k8s_handler'].delete_namespace(
            params['__default__']['application-namespace'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

        success = params['k8s_handler'].delete_namespace(
            params['__default__']['monitoring-namespace'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

        success = params['k8s_handler'].delete_namespace(
            params['__default__']['notebook-namespace'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

        success = params['k8s_handler'].delete_namespace(
            params['__default__']['model-namespace'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False
                        
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Data science cluster initializations deleted')
    my_output.default('- Data auths deleted')
    my_output.default('- Data image streams deleted')
    my_output.default('- Subscription and csv deleted')
    my_output.default('- Operator Group deleted')
    my_output.default('- Namespaces deleted')

    return True