import json
import copy
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow import ocp_common


def initialize(params, my_output, log_id):
    params = augment_params(params)

    my_output.default('Workflow Parameters', underline=True)
    display_params = copy.deepcopy(params)
    my_output.default(json.dumps(display_params, indent=4), after_newline=True)

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['mgmt-required'] = True
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return None

    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler
    params['ssh_handler'] = ocp_common.get_management_node_ssh_handler(params['cluster'], log_id=log_id)
    return params


def get_default_params():
    params = {}
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
