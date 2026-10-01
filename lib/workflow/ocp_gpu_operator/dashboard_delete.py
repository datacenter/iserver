from lib import output_helper
from lib.workflow.ocp_gpu_operator import common as local_common
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

    ocp_common.print_title(params, my_output, 'Delete DCGM Dashboard')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    subscription = params['k8s_handler'].get_subscription_by_package(
        params['__default__']['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('GPU Operator not installed')
        return True

    if not params['k8s_handler'].is_any_cluster_policy(cache_enabled=False):
        my_output.default('No NVIDIA Cluster Policy found')
        return True

    is_config_map = params['k8s_handler'].is_config_map(
        params['__default__']['monitoring']['dashboard_namespace'],
        params['__default__']['monitoring']['dashboard_name'],
        cache_enabled=False
    )
    if not is_config_map:
        my_output.default('Monitoring dashboard not found')
        return True

    success = params['k8s_handler'].delete_config_map(
        params['__default__']['monitoring']['dashboard_namespace'],
        params['__default__']['monitoring']['dashboard_name'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- GPU Monitoring Dashboard deleted')

    return True
