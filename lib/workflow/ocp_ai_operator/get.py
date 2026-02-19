from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_ai_operator import common as local_common


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
    my_output.default('OpenShift Workflow - Data Science (AI) - Get Information', before_newline=True, after_newline=True, double_underline=True)

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
    
    clusters = params['k8s_handler'].get_data_science_clusters(
        cache_enabled=False
    )
    if clusters is None:
        my_output.error('Failed to get data science clusters')
        return False

    initializations = params['k8s_handler'].get_data_science_cluster_initializations(
        cache_enabled=False
    )
    if initializations is None:
        my_output.error('Failed to get data science cluster initializations')
        return False

    auths = params['k8s_handler'].get_auths(
        cache_enabled=False
    )
    if auths is None:
        my_output.error('Failed to get auths')
        return False

    k8s_output_handler.print_auths(auths)

    k8s_output_handler.print_data_science_cluster_initializations(initializations)

    k8s_output_handler.print_data_science_clusters(clusters)

    if len(clusters) > 0:
        my_output.default('Dashboard', before_newline=True)
        for cluster in clusters:
            if cluster['url'] is not None:
                my_output.default('- %s: https://%s' % (cluster['name'], cluster['url']))

    return True
