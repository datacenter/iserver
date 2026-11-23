import copy
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_ai_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'list-of-str', None, None, None, None],
        ['view', True, ['state'], 'view', None, None, ['state', 'res'], None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(mparams, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    mparams, error = validate(mparams)
    if error is not None:
        my_output.error(error)
        return False
    
    for cluster in mparams['cluster']:
        params = copy.deepcopy(mparams)
        params['cluster'] = cluster
        
        ocp_common.print_title(params, my_output, 'Get Information')
        params = ocp_common.workflow_init(params, my_output, log_id)
        if params is None:
            continue

        subscription = params['k8s_handler'].get_subscription_by_package(
            params['__default__']['name'],
            return_mo=False,
            cache_enabled=False
        )
        if subscription is None:
            my_output.default('Operator not found: %s' % (params['__default__']['name']))
            continue
        
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
            continue

        auths = params['k8s_handler'].get_auths(
            cache_enabled=False
        )
        if auths is None:
            my_output.error('Failed to get auths')
            continue

        k8s_output_handler.print_auths(auths)

        k8s_output_handler.print_data_science_cluster_initializations(initializations)

        k8s_output_handler.print_data_science_clusters(clusters)

        if len(clusters) > 0:
            my_output.default('Dashboard', before_newline=True)
            for cluster in clusters:
                if cluster['url'] is not None:
                    my_output.default('- %s: https://%s' % (cluster['name'], cluster['url']))

    return True
