from lib import output_helper
from lib.workflow.ocp_local_storage_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params

    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def check_resources(params, my_output):
    my_output.default('Check Local Storage Operator Resources', before_newline=True, underline=True)
    subscription = params['k8s_handler'].get_subscription_by_package(
        params['__default__']['name'],
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
    
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Delete Operator')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    state = local_common.check_state(
        params, 
        my_output,
        check_ready=True,
        check_resources=True
    )
    if not state['installed']:
        my_output.default('')
        my_output.default('Completed tasks')
        my_output.default('- Local Storage Operator already %s' % (
            my_output.add_color('uninstalled', 'Green')
        ))
        return True

    if state['dependants']:
        my_output.default('Cleanup local storage configuration first', before_newline=True)
        return False
    
    success = ocp_common.delete_operator(
        params,
        my_output
    )
    if not success:
        return False
    
    return True
