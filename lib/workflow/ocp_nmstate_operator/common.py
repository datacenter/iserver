from lib.workflow import ocp_common


def get_default_params():
    params = {}
    params['namespace'] = 'openshift-nmstate'
    params['name'] = 'kubernetes-nmstate-operator'
    params['operator-group-name'] = 'nmstate-operator-group'
    params['delete-namespace'] = True
    params['create_subscription'] = 'create_nmstate_subscription'
    params['delete_subscription'] = 'delete_nmstate_subscription'
    params['title'] = 'OpenShift Workflow - NMState Operator'
    return params

def print_nmstate_state(params, my_output, k8s_output_handler):
    subscription = ocp_common.get_subscription(
        params['k8s_handler'],
        params['__default__']['name'],
        my_output=my_output
    )
    if subscription is None:
        return
    
    nmstates = params['k8s_handler'].get_nmstates(cache_enabled=False)
    if nmstates is None:
        my_output.error('Failed to nmstate instance')
        return
    
    if len(nmstates) == 0:
        my_output.default('No nmstate instance')
        return
    
    if len(nmstates) > 1:
        my_output.error('Multiple nmstate instances')
        return

    if params['k8s_handler'].is_subscription_nmstate_ready(with_instance=True):
        my_output.default('Nmstate instance: %s (%s)' % (nmstates[0]['name'], my_output.add_color('ready', 'Green')))
    else:
        my_output.default('Nmstate instance: %s (%s)' % (nmstates[0]['name'], my_output.add_color('not ready', 'Red')))

    my_output.default('Node Network State', underline=False, before_newline=True)
    nodes = params['k8s_handler'].get_nodes_name()
    if nodes is None:
        my_output.error('Failed to get kubernetes nodes')
        return

    for node in nodes:
        if params['k8s_handler'].is_node_network_state(node):
            my_output.default('- %s: %s' % (node, my_output.add_color('found', 'Green')))
        else:
            my_output.default('- %s: %s' % (node, my_output.add_color('not found', 'Red')))

    nncps = params['k8s_handler'].get_node_network_configuration_policys()
    if nncps is None:
        my_output.error('Failed to get nncp')
        return
    
    my_output.default('Node network configuration policy: %s' % (len(nncps)))

    nnces = params['k8s_handler'].get_node_network_configuration_enactments()
    if nnces is None:
        my_output.error('Failed to get nnce')
        return

    my_output.default('Node network configuration enactment: %s' % (len(nnces)))

def print_nmstate_res(params, my_output, k8s_output_handler):
    nncps = params['k8s_handler'].get_node_network_configuration_policys()
    if nncps is None:
        my_output.default('No nncp')
    else:            
        k8s_output_handler.print_node_network_configuration_policys_state(nncps)

    nnces = params['k8s_handler'].get_node_network_configuration_enactments()
    if nnces is None:
        my_output.default('No nnce')
    else:
        k8s_output_handler.print_node_network_configuration_enactments_state(nnces)        

    ocp_common.print_namespace_resources(params, params['__default__']['namespace'], k8s_output_handler)