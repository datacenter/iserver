from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_nmstate_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['filename', True, None, 'file-k8s', None, None, None, None]
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

    ocp_common.print_title(params, my_output, 'Create Instance')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    subscription = ocp_common.get_subscription(
        params['k8s_handler'],
        params['__default__']['name'],
        my_output=my_output
    )
    if subscription is None:
        return False
            
    if params['k8s_handler'].is_any_nmstate(cache_enabled=False):
        my_output.default('NMState instance already defined')
        return True

    instance_body = None
    if params['filename'] is not None:
        instance_body = file_helper.get_file_yaml(
            params['filename']
        )
        if instance_body is None:
            my_output.error('Failed to get nmstate instance: %s' % (params['filename']))
            return False

    if instance_body is None:
        subscription = params['k8s_handler'].get_subscription_by_package(
            params['__default__']['name'],
            return_mo=False,
            cache_enabled=False
        )
        instance_body = params['k8s_handler'].get_nmstate_package_channel_example(
            subscription['spec']['channel'],
            'NMState'
        )
        if instance_body is None:
            my_output.error('Failed to get NMState reference example in channel %s' % (subscription['spec']['channel']))
            return False
    
    success = params['k8s_handler'].create_nmstate(
        instance_body,
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True            
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- NMState instance created')
    return True