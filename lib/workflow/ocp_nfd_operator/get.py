import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow.ocp_nfd_operator import common as local_common


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
    my_output.default('OpenShift Workflow - Node Feature Discover Operator - Get Information', before_newline=True, after_newline=True, double_underline=True)

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
    
    my_output.default('Operator', underline=True, before_newline=True)
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
    
    nfds = params['k8s_handler'].get_node_feature_discoveries(
        cache_enabled=False
    )
    if nfds is None:
        my_output.error('Failed to get nfd instances')
        return False

    if len(nfds) > 0:
        instances = []
        for nfd in nfds:
            instances.append(
                nfd['name']
            )

        my_output.default('- instance: %s' % (','.join(instances)))

    if params['k8s_handler'].is_subscription_nfd_ready():
        my_output.default('- %s' % (my_output.add_color('ready', 'Green')))
    else:
        my_output.default('- %s' % (my_output.add_color('not ready', 'Red')))
        params['k8s_handler'].check_namespace_usage_and_state(
            subscription['namespace'],
            my_output=my_output,
            show_details=True
        )

    nodes = params['k8s_handler'].get_nodes(cache_enabled=False)
    if nodes is None:
        my_output.error('Failed to get kubernetes nodes')
        return False
    
    my_output.default('NFD node annotations', underline=True, before_newline=True)
    for node in nodes:
        if 'nfd.node.kubernetes.io/feature-labels' not in node['annotations']:
            my_output.error('No nfd annotations on node [%s]' % (node['name']))
        else:
            if not params['verbose']:
                my_output.default('- %s' % (node['name']))

            if params['verbose']:
                my_output.default('- node [%s]' % (node['name']))
                for annotation in node['annotations']['nfd.node.kubernetes.io/feature-labels'].split(','):
                    my_output.default('\t%s' % (annotation))

    return True
