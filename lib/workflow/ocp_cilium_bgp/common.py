import json
import copy
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow import ocp_common


def initialize(params, my_output, log_id, mgmt_required=False, api_check=True):
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
    ocp_check_params['kube-api-check'] = api_check
    ocp_check_params['mgmt-required'] = mgmt_required
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return None

    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler
    params['kubeconfig_filename'] = ocp_params['data']['kubeconfig_filename']
    params['ssh_handler'] = ocp_common.get_management_node_ssh_handler(params['cluster'], log_id)
    if mgmt_required:
        if params['ssh_handler'] is None:
            my_output.error('Management access required and fails')
            return None

    return params


def get_default_params():
    params = {}
    params['namespace'] = 'cilium'
    params['package'] = 'clife'
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

def is_bgp_crd(params, my_output=None):
    clusters = params['k8s_handler'].get_isovalent_bgp_cluster_configs(cache_enabled=False)
    if clusters is None:
        if my_output is not None:
            my_output.default('BGP Control Plane CRDs %s' % (my_output.add_color('not found', 'Red')))
        return False
    
    my_output.default('BGP Control Plane CRDs %s' % (my_output.add_color('found', 'Green')))
    return True