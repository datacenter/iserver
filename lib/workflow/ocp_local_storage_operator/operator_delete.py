import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow.ocp_local_storage_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'

    allowed_keys = [
        'cluster',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None

def check_resources(params, my_output):
    my_output.default('Check Local Storage Operator Resources', before_newline=True, underline=True)
    subscription = params['k8s_handler'].get_subscription_by_package(
        params['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('- skipping as there is lso')
        return True
    
    my_output.default('- checking local volume...')
    objects = params['k8s_handler'].get_local_volumes(cache_enabled=False)
    if objects is None:
        my_output.error('Unexpected error in getting information')
        return False
    if len(objects) > 0:
        my_output.error('Unexpected local volumes')
        return False
    
    my_output.default('- checking local volume set...')
    objects = params['k8s_handler'].get_local_volume_sets(cache_enabled=False)
    if objects is None:
        my_output.error('Unexpected error in getting information')
        return False
    if len(objects) > 0:
        my_output.error('Unexpected local volume sets')
        return False

    my_output.default('- checking local volume discovery...')
    objects = params['k8s_handler'].get_local_volume_discoveries(cache_enabled=False)
    if objects is None:
        my_output.error('Unexpected error in getting information')
        return False
    if len(objects) > 0:
        my_output.error('Unexpected local volume discoveries')
        return False

    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Local Storage Operator - Delete Operator', before_newline=True, after_newline=True, double_underline=True)
    
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not check_resources(params, my_output):
        return False
    
    success = params['k8s_handler'].delete_local_storage_subscription(
        params['namespace'], 
        params['name'],
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
    my_output.default('- No volumes checked')
    my_output.default('- Subscription and csv deleted')
    my_output.default('- Operator Group deleted')
    my_output.default('- Namespace deleted')

    return True
