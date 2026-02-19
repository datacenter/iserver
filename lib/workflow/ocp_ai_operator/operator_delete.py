from lib import output_helper
from lib.workflow.ocp_ai_operator import common as local_common


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


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Data Science (AI) - Delete Operator', before_newline=True, after_newline=True, double_underline=True)

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
            object_filter=['namespace:%s' % (params['application-namespace'])], 
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
        object_filter=['namespace:%s' % (params['application-namespace'])], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_services(
        object_filter=['namespace:%s' % (params['application-namespace'])], 
        my_output=my_output, 
        wait=True
    )
    if not success:
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

        success = params['k8s_handler'].delete_namespace(
            params['application-namespace'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

        success = params['k8s_handler'].delete_namespace(
            params['monitoring-namespace'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

        success = params['k8s_handler'].delete_namespace(
            params['notebook-namespace'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

        success = params['k8s_handler'].delete_namespace(
            params['model-namespace'],
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
