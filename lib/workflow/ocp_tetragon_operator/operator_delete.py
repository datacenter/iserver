from lib import output_helper
from lib.workflow.ocp_tetragon_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def pre_delete_operator(params, my_output):
    success = params['k8s_handler'].delete_catalog_source(
        params['__default__']['catalog-namespace'],
        params['__default__']['catalog-name'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].delete_config_map(
        params['__default__']['cm-namespace'],
        params['__default__']['cm-name'],
        my_output=my_output,
        wait=True
    )

    success = params['k8s_handler'].delete_config_map(
        params['__default__']['operator-cm-namespace'],
        params['__default__']['operator-cm-name'],
        my_output=my_output,
        wait=True
    )

    success = params['k8s_handler'].delete_service_monitor(
        params['__default__']['sm-namespace'],
        params['__default__']['sm-name'],
        my_output=my_output,
        wait=True
    )

    success = params['k8s_handler'].delete_service(
        params['__default__']['sm-namespace'],
        params['__default__']['sm-name'],
        my_output=my_output,
        wait=True
    )

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

    resources = local_common.get_resources(params)
    if local_common.is_any_resource(resources):
        local_common.print_resource_brief(resources, my_output)
        my_output.error('Delete tetragon policy resources first')
        return False

    success = ocp_common.delete_operator(
        params,
        my_output,
        subscription_only=True,
    )
    if not success:
        return False
    
    success = pre_delete_operator(
        params,
        my_output
    )
    if not success:
        return False

    success = ocp_common.delete_operator(
        params,
        my_output,
        skip_subscription=True
    )
    if not success:
        return False

    return True