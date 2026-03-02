import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow.ocp_odf_operator import common as local_common


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
    
    new_params = {}
    allowed_keys = [
        'cluster',
        'verbose',
        'check-verbose'
    ]
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params, None


def check_resources(params, my_output):
    my_output.default('Check OpenShift Data Foundation (ODF) Operator Resources', before_newline=True, underline=True)
    subscription = params['k8s_handler'].get_subscription_by_package(
        params['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('- skipping as there is odf')
        return True
    
    my_output.default('- checking storage cluster...')
    objects = params['k8s_handler'].get_storage_clusters(cache_enabled=False)
    if objects is None:
        my_output.error('Unexpected error in getting information')
        return False
    if len(objects) > 0:
        my_output.error('Unexpected storage clusters')
        return False
    
    return True


def delete_subscription(params, my_output):
    my_output.default('Check Subscription', before_newline=True, underline=True)

    subscription = params['k8s_handler'].get_subscription_by_package(
        params['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('- already deleted: %s' % (params['name']))
        return True

    my_output.default('- subscription found and will be deleted: %s' % (params['name']))

    csv = params['k8s_handler'].get_cluster_service_version(
        subscription['namespace'],
        subscription['installed_csv'],
        return_mo=False,
        cache_enabled=False
    )
    if csv is not None:
        my_output.default('- csv found and will be deleted: %s/%s' % (subscription['namespace'], subscription['installed_csv']))
    if csv is None:
        my_output.default('- [WARNING] csv not found: %s/%s' % (subscription['namespace'], subscription['installed_csv']))

    success = params['k8s_handler'].delete_subscription_mo(
        subscription['namespace'], 
        subscription['name']
    )
    if not success:
        my_output.error('Delete subscription api failed')
        return False
        
    my_output.default('- subscription deleted: %s/%s' % (subscription['namespace'], subscription['name']))
    my_output.default('- wait for no subscription')
    if not params['k8s_handler'].wait_no_subscription(subscription['namespace'], subscription['name']):
        my_output.error('Timed out')
        return False

    if params['k8s_handler'].is_cluster_service_version(subscription['namespace'], subscription['installed_csv']):
        success = params['k8s_handler'].delete_cluster_service_version_mo(
            subscription['namespace'], 
            subscription['installed_csv']
        )
        if not success:
            my_output.error('Delete csv api failed')
            return False
            
        my_output.default('- csv deleted: %s/%s' % (subscription['namespace'], subscription['installed_csv']))
        my_output.default('- wait for no csv')
        if not params['k8s_handler'].wait_no_cluster_service_version(subscription['namespace'], subscription['name']):
            my_output.error('Timed out')
            return False

    if not params['k8s_handler'].wait_no_subscription_odf(my_output=my_output):
        return False

    return True


def delete_operator_group(params, my_output):
    my_output.default('Check Operator Group', before_newline=True, underline=True)
    if not params['k8s_handler'].is_operator_group(params['namespace'], params['operator-group-name']):
        my_output.default('- already deleted: %s/%s' % (params['namespace'], params['operator-group-name']))
        return True
    
    if not params['k8s_handler'].delete_operator_group_mo(params['namespace'], params['operator-group-name']):
        my_output.error('Failed to delete operator group')
        return False
    
    my_output.default('- operator group deleted: %s/%s' % (params['namespace'], params['operator-group-name']))
    my_output.default('- wait for no operator group')
    if not params['k8s_handler'].wait_no_operator_group(params['namespace'], params['operator-group-name']):
        my_output.error('Timed out')
        return False
        
    return True
     
        
def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - OpenShift Data Foundation (ODF) Operator - Delete Operator', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.augment_params(params)
    
    my_output.default('Workflow Parameters', underline=True)
    my_output.default(json.dumps(params, indent=4), after_newline=True)

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return False
    
    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler

    if not check_resources(params, my_output):
        return False
    
    if not delete_subscription(params, my_output):
        return False

    if not delete_operator_group(params, my_output):
        return False

    success = params['k8s_handler'].delete_namespaced_jobs(
        params['namespace'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_services(
        object_filter=['namespace:%s' % (params['namespace'])],
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
    
    success = params['k8s_handler'].delete_namespaced_storage_systems(
        params['namespace'],
        my_output=my_output,
        wait=True,
        finalizers=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].delete_namespaced_ocs_initialization(
        params['namespace'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].delete_namespace(params['namespace'], my_output=my_output, wait=True, finalizers=True)
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- ODF resources checked')
    my_output.default('- Subscription and csv deleted')
    my_output.default('- Operator Group deleted')
    my_output.default('- Resources deleted')
    my_output.default('- Namespace deleted')

    return True
