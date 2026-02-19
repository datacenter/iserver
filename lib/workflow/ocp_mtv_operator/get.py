from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_mtv_operator import common as local_common


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
    
    allowed_keys = [
        'cluster',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Migration Toolkit for Virtualization Operator - Get Information', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_subscription_ready(params, my_output, details=True):
        return True
    
    if not local_common.is_instance_ready(params, my_output):
        return True
    
    providers = params['k8s_handler'].get_providers(
        storage_info=True, 
        network_info=True,
        plan_info=True,
        cache_enabled=False
    )
    if providers is None:
        my_output.default('Failed to get provider', before_newline=True)
        return False

    k8s_output_handler.print_providers(providers)

    maps = params['k8s_handler'].get_network_maps(
        plan_info=True, 
        cache_enabled=False
    )
    if maps is None:
        my_output.error('Failed to get network maps')
        return False
    
    k8s_output_handler.print_network_maps(maps)

    maps = params['k8s_handler'].get_storage_maps(
        plan_info=True, 
        cache_enabled=False
    )
    if maps is None:
        my_output.error('Failed to get storage maps')
        return False
    
    k8s_output_handler.print_storage_maps(maps)

    plans = params['k8s_handler'].get_plans(
        smap_info=True, 
        nmap_info=True, 
        cache_enabled=False
    )
    if plans is None:
        my_output.error('Failed to get migration plans')
        return False

    k8s_output_handler.print_plans(plans)

    migrations = params['k8s_handler'].get_migrations(
        vm_info=True, 
        vmi_info=True, 
        pvc_info=True, 
        dv_info=True, 
        pod_info=True,
        cache_enabled=False
    )
    if migrations is None:
        my_output.default('Failed to get migrations')
        return False
    
    k8s_output_handler.print_migrations(migrations)

    return True
