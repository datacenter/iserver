import copy
import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.k8s import output as k8s_output
from lib.workflow.ocp_nmstate_operator import common as local_common
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
        
        nmstates = params['k8s_handler'].get_nmstates(cache_enabled=False)
        if nmstates is None:
            my_output.error('Failed to nmstate instance')
            continue
        
        if len(nmstates) == 0:
            my_output.error('No nmstate instance')
            continue
        
        if len(nmstates) > 1:
            my_output.error('Multiple nmstate instances')
            continue

        my_output.default('- instance: %s' % (nmstates[0]['name']))

        my_output.default('Operator functional readiness', underline=True, before_newline=True)
        if params['k8s_handler'].is_subscription_nmstate_ready():
            my_output.default(my_output.add_color('ready', 'Green'))
        else:
            my_output.default(my_output.add_color('not ready', 'Red'))
            params['k8s_handler'].check_namespace_usage(
                subscription['namespace'],
                my_output=my_output,
                k8s_output_handler=k8s_output_handler,
                show_details=True
            )

        my_output.default('Node Network State', underline=True, before_newline=True)
        nodes = params['k8s_handler'].get_nodes_name()
        if nodes is None:
            my_output.error('Failed to get kubernetes nodes')
            continue

        for node in nodes:
            if params['k8s_handler'].is_node_network_state(node):
                my_output.default('- %s: %s' % (node, my_output.add_color('found', 'Green')))
            else:
                my_output.default('- %s: %s' % (node, my_output.add_color('not found', 'Red')))


        k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
        nncps = params['k8s_handler'].get_node_network_configuration_policys()
        if nncps is None:
            my_output.error('Failed to get nncp')
            continue
        
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
