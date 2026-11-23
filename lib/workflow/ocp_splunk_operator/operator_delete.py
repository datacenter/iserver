from lib import output_helper
from lib.workflow.ocp_splunk_operator import common as local_common
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

    if params['k8s_handler'].is_deployment(params['__default__']['namespace'], params['__default__']['deployment'], cache_enabled=False):
        params = local_common.collect_state_info(params)

        my_output.dictionary_ng(
            'Splunk Custom Resources',
            params['summary'],
            [
                ['standalone', 'standalone'],
                ['cluster master', 'cluster_master'],
                ['cluster manager', 'cluster_manager'],
                ['indexer cluster', 'indexer_cluster'],
                ['license manager', 'license_manager'],
                ['license master', 'license_master'],
                ['monitoring console', 'monitoring_console'],
                ['search head cluster', 'search_head_cluster']
            ]
        )
    
        if params['summary']['resources']:
            my_output.error('Delete splunk operator resources first')
            return False

    success = params['k8s_handler'].delete_namespaced_deployments(
        params['__default__']['namespace'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_labeled_custom_resource_definitions(
        dict(name='splunk-operator'),
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_namespaced_config_maps(
        params['__default__']['namespace'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_namespaced_services(
        params['__default__']['namespace'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_namespaced_pvcs(
        params['__default__']['namespace'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_namespaced_routes(
        params['__default__']['namespace'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_namespaced_role_bindings(
        params['__default__']['namespace'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_labeled_cluster_role_bindings(
        dict(name='splunk-operator'),
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_namespaced_roles(
        params['__default__']['namespace'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_labeled_cluster_roles(
        dict(name='splunk-operator'),
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_namespaced_service_accounts(
        params['__default__']['namespace'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_namespace(
        params['__default__']['namespace'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Splunk operator deleted')
    return True