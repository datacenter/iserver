from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_minio_operator import common as local_common


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
    my_output.default('OpenShift Workflow - MinIO Operator - Get Information', before_newline=True, after_newline=True, double_underline=True)

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
    
    items = params['k8s_handler'].get_admin_jobs(cache_enabled=False)
    if items is None:
        my_output.error('Failed to get admin jobs')
    else:
        k8s_output_handler.print_admin_jobs(items)

    items = params['k8s_handler'].get_policy_bindings(cache_enabled=False)
    if items is None:
        my_output.error('Failed to get policy bindings')
    else:
        k8s_output_handler.print_policy_bindings(items)

    items = params['k8s_handler'].get_object_stores(cache_enabled=False)
    if items is None:
        my_output.error('Failed to get object stores')
    else:
        k8s_output_handler.print_object_stores(items)

    return True
