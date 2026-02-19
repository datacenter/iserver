from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_service_mesh_operator import common as local_common


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
        'check-verbose',
        'verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Service Mesh Operator - Get Information', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    subscription_v2 = params['k8s_handler'].get_subscription_by_package(
        params['name_v2'],
        return_mo=False,
        cache_enabled=False
    )

    subscription_v3 = params['k8s_handler'].get_subscription_by_package(
        params['name_v3'],
        return_mo=False,
        cache_enabled=False
    )

    if subscription_v2 is None and subscription_v3 is None:
        my_output.default('Operator (v2) not found: %s' % (params['name_v2']))
        my_output.default('Operator (v3) not found: %s' % (params['name_v3']))
        return True
    
    if subscription_v2 is not None:
        my_output.default('Operator (v2)', underline=True, before_newline=True)
        my_output.default('- subscription: %s' % (subscription_v2['namespace_name']))
        my_output.default('- channel: %s' % (subscription_v2['channel']))
        my_output.default('- csv: %s' % (subscription_v2['installed_csv']))
        
        csv = params['k8s_handler'].get_cluster_service_version(
            subscription_v2['namespace'],
            subscription_v2['installed_csv'],
            return_mo=False,
            cache_enabled=False
        )
        if csv is None:
            my_output.debug('[WARNING] CSV not found: %s/%s' % (subscription_v2['namespace'], subscription_v2['installed_csv']))

        items = params['k8s_handler'].get_service_mesh_control_planes(
            deployment_info=True, 
            service_info=True,
            member_info=True,
            cache_enabled=False
        )
        if items is None:
            my_output.error('Failed to get service mesh control planes')
        else:
            k8s_output_handler.print_service_mesh_control_planes(items)

    if subscription_v3 is not None:
        my_output.default('Operator (v3)', underline=True, before_newline=True)
        my_output.default('- subscription: %s' % (subscription_v3['namespace_name']))
        my_output.default('- channel: %s' % (subscription_v3['channel']))
        my_output.default('- csv: %s' % (subscription_v3['installed_csv']))
        
        csv = params['k8s_handler'].get_cluster_service_version(
            subscription_v3['namespace'],
            subscription_v3['installed_csv'],
            return_mo=False,
            cache_enabled=False
        )
        if csv is None:
            my_output.debug('[WARNING] CSV not found: %s/%s' % (subscription_v3['namespace'], subscription_v3['installed_csv']))

    return True
