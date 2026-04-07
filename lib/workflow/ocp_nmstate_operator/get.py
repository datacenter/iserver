import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.k8s import output as k8s_output
from lib.workflow.ocp_nmstate_operator import common as local_common


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
    
    new_params = {}
    allowed_keys = [
        'cluster',
        'verbose',
        'check-verbose'
    ]
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - NMState Operator - Get Information', before_newline=True, after_newline=True, double_underline=True)

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
    
    nmstates = params['k8s_handler'].get_nmstates(cache_enabled=False)
    if nmstates is None:
        my_output.error('Failed to nmstate instance')
        return False
    
    if len(nmstates) == 0:
        my_output.error('No nmstate instance')
        return False
    
    if len(nmstates) > 1:
        my_output.error('Multiple nmstate instances')
        return False

    my_output.default('- instance: %s' % (nmstates[0]['name']))

    my_output.default('Operator functional readiness', underline=True, before_newline=True)
    if params['k8s_handler'].is_subscription_nmstate_ready():
        my_output.default(my_output.add_color('ready', 'Green'))
    else:
        my_output.default(my_output.add_color('not ready', 'Red'))
        params['k8s_handler'].check_namespace_usage_and_state(
            subscription['namespace'],
            my_output=my_output,
            show_details=True
        )

    my_output.default('Node Network State', underline=True, before_newline=True)
    nodes = params['k8s_handler'].get_nodes_name()
    if nodes is None:
        my_output.error('Failed to get kubernetes nodes')
        return False
    for node in nodes:
        if params['k8s_handler'].is_node_network_state(node):
            my_output.default('- %s: %s' % (node, my_output.add_color('found', 'Green')))
        else:
            my_output.default('- %s: %s' % (node, my_output.add_color('not found', 'Red')))


    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    nncps = params['k8s_handler'].get_node_network_configuration_policies()
    if nncps is None:
        my_output.error('Failed to get nncp')
        return False
    
    k8s_output_handler.print_node_network_configuration_policys_state(nncps)
    nnces = params['k8s_handler'].get_node_network_configuration_enactments()
    if nnces is None:
        my_output.error('Failed to get nnce')
        return False

    k8s_output_handler.print_node_network_configuration_enactment(
        nnces,
        title=True
    )        

    return True
