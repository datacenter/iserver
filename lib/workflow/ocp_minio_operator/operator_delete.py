from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_minio_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'wipe' not in params:
        params['wipe'] = False

    if not isinstance(params['wipe'], bool):
        return None, 'wipe param must be true or false'
    
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
        'wipe',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - MinIO Operator - Delete Operator', before_newline=True, after_newline=True, double_underline=True)

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
        my_output.default('Checking MinIO related objects', before_newline=True)

        items = params['k8s_handler'].get_admin_jobs(cache_enabled=False)
        if items is None:
            my_output.error('Failed to get admin jobs')
            return False
        
        if len(items) == 0:
            my_output.default('No AdminJob', before_newline=True)
        else:
            k8s_output_handler.print_admin_jobs(items)

            if params['wipe']:
                success = params['k8s_handler'].delete_admin_jobs(
                    my_output=my_output,
                    wait=True
                )
                if not success:
                    return False
            
            if not params['wipe']:
                my_output.error('Delete admin jobs first')
                return False
        
        items = params['k8s_handler'].get_policy_bindings(cache_enabled=False)
        if items is None:
            my_output.error('Failed to get policy bindings')
            return False

        if len(items) == 0:
            my_output.default('No PolicyBinding', before_newline=True)
        else:
            k8s_output_handler.print_policy_bindings(items)

            if params['wipe']:
                success = params['k8s_handler'].delete_policy_bindings(
                    my_output=my_output,
                    wait=True
                )
                if not success:
                    return False
            
            if not params['wipe']:
                my_output.error('Delete policy bindings first')
                return False
            
        items = params['k8s_handler'].get_object_stores(cache_enabled=False)
        if items is None:
            my_output.error('Failed to get object stores')
            return False

        if len(items) == 0:
            my_output.default('No ObjectStore', before_newline=True)
        else:
            k8s_output_handler.print_object_stores(items)

            if params['wipe']:
                success = params['k8s_handler'].delete_object_stores(
                    my_output=my_output,
                    wait=True
                )
                if not success:
                    return False
            
            if not params['wipe']:
                my_output.error('Delete object stores first')
                return False

        success = params['k8s_handler'].delete_minio_subscription(
            subscription['namespace'],
            subscription['name'],
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

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Subscription and csv deleted')
    my_output.default('- Operator Group deleted')
    my_output.default('- Namespace deleted')

    return True
