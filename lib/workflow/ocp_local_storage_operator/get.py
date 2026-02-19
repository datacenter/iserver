import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.k8s import output as k8s_output
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


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Local Storage Operator - Get Information', before_newline=True, after_newline=True, double_underline=True)

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
        my_output.default('Operator not found: %s' % (params['name']))
        return True
    
    my_output.default('Operator', underline=True)
    my_output.default('- subscription: %s' % (subscription['namespace_name']))
    my_output.default('- channel: %s' % (subscription['channel']))
    my_output.default('- csv: %s' % (subscription['installed_csv']))
    
    csv = params['k8s_handler'].get_cluster_service_version(
        subscription['namespace'],
        subscription['installed_csv'],
        return_mo=False,
        cache_enabled=False
    )
    if csv is None:
        my_output.debug('[WARNING] CSV not found: %s/%s' % (subscription['namespace'], subscription['installed_csv']))
    
    my_output.default('Operator functional readiness', underline=True, before_newline=True)
    if params['k8s_handler'].is_subscription_local_storage_ready():
        my_output.default(my_output.add_color('ready', 'Green'))
    else:
        my_output.default(my_output.add_color('not ready', 'Red'))
        params['k8s_handler'].check_namespace_usage_and_state(
            subscription['namespace'],
            my_output=my_output,
            show_details=True
        )

    lvd = params['k8s_handler'].get_local_volume_discoveries(
        cache_enabled=False
    )
    if lvd is None:
        my_output.error('Failed to run api call')
        return False
    
    k8s_output_handler.print_local_volume_discoveries(lvd, title=True)

    lvdr = params['k8s_handler'].get_local_volume_discovery_results(
        cache_enabled=False
    )
    if lvdr is None:
        my_output.error('Failed to run api call')
        return False
    
    k8s_output_handler.print_local_volume_discovery_results(lvdr, title=True)

    lvset = params['k8s_handler'].get_local_volume_sets(
        cache_enabled=False
    )
    if lvset is None:
        my_output.error('Failed to run api call')
        return False
    
    k8s_output_handler.print_local_volume_sets(lvset, title=True)

    vol = params['k8s_handler'].get_local_volumes(
        cache_enabled=False
    )
    if vol is None:
        my_output.error('Failed to run api call')
        return False
    
    k8s_output_handler.print_local_volumes(vol, title=True)

    if lvset is not None:
        for item in lvset:
            storage_class = params['k8s_handler'].get_storage_class(item['storage_class'], pv_info=True)
            if storage_class is not None:
                k8s_output_handler.print_storage_classes_with_resources([storage_class], title=True)

    if vol is not None:
        sc_names = []
        for item in vol:
            for device in item['device']:
                if device['sc'] not in sc_names:
                    sc_names.append(device['sc'])

        for item in sc_names:
            storage_class = params['k8s_handler'].get_storage_class(item, pv_info=True)
            if storage_class is not None:
                k8s_output_handler.print_storage_classes_with_resources([storage_class], title=True)
        
    return True
