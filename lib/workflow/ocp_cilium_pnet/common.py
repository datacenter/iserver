import json
import copy
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow.ocp_cilium_cni import common as cilium_common


def initialize(params, my_output, log_id):
    params = augment_params(params)

    if params['verbose']:
        my_output.default('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        my_output.default(json.dumps(display_params, indent=4), after_newline=True)
    else:
        my_output.debug('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        my_output.debug(json.dumps(display_params, indent=4), after_newline=True)

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return None

    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler
    return params


def get_default_params():
    params = {}
    params['namespace'] = 'cilium'
    params['package'] = 'clife'
    params['operator-name'] = 'cilium-operator'
    params['agent-name'] = 'cilium'
    return params


def augment_params(params):
    defaults = get_default_params()
    for key in defaults:
        params[key] = defaults[key]
    return params


def sanitize_params(params, allowed_keys):
    new_params = {}
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params


def is_pnet_crd(params, my_output=None):
    if my_output is not None:
        my_output.default('Check private network crd', underline=True, before_newline=True)
    
    if params['k8s_handler'].get_clusterwide_private_networks(cache_enabled=False) is None:
        if my_output is not None:
            my_output.error('ClusterwidePrivateNetwork CRD not found')
        return False
    
    if my_output is not None:
        my_output.default('- ClusterwidePrivateNetwork')

    if params['k8s_handler'].get_private_network_endpoint_slices(cache_enabled=False) is None:
        if my_output is not None:
            my_output.error('PrivateNetworkEndpointSlice CRD not found')
        return False
    
    if my_output is not None:
        my_output.default('- PrivateNetworkEndpointSlice')

    if params['k8s_handler'].get_private_network_external_endpoints(cache_enabled=False) is None:
        if my_output is not None:
            my_output.error('PrivateNetworkExternalEndpoint CRD not found')
        return False
    
    if my_output is not None:
        my_output.default('- PrivateNetworkExternalEndpoint')

    return True

def is_pnet_ready(params, my_output):
    if not cilium_common.is_cilium(params, my_output):
        return False

    if params['k8s_handler'].is_cilium_private_network_enabled(cache_enabled=False):
        my_output.default('Private network %s' % (my_output.add_color('enabled', 'Green')))
    else:
        my_output.default('Private network %s' % (my_output.add_color('disabled', 'Red')))
        return False

    if is_pnet_crd(params):
        my_output.default('Private network crds %s' % (my_output.add_color('found', 'Green')))
    else:
        my_output.default('Private network crds %s' % (my_output.add_color('not found', 'Red')))
        return False

    return True
