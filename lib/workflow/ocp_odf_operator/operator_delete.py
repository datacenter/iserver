from lib import output_helper
from lib.workflow.ocp_odf_operator import common as local_common
from lib.workflow import ocp_common
from menu.common import get_confirmation


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params

    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def check_resources(params, my_output):
    my_output.default('Check OpenShift Data Foundation (ODF) Operator Resources', before_newline=True, underline=True)
    subscription = params['k8s_handler'].get_subscription_by_package(
        params['__default__']['name'],
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
            
    if not check_resources(params, my_output):
        return False

    success = params['k8s_handler'].delete_namespaced_storage_systems(
        params['__default__']['namespace'],
        my_output=my_output,
        wait=True,
        finalizers=True,
        optional=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].delete_namespaced_ocs_initialization(
        params['__default__']['namespace'],
        my_output=my_output,
        wait=True,
        optional=True
    )
    if not success:
        return False
    
    success = ocp_common.delete_operator(
        params, 
        my_output, 
        wipe_namespace=True
    )
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