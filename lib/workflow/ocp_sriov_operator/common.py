import json
import copy
from lib.workflow.ocp_access import check as ocp_check


def initialize(params, my_output, log_id):
    params = augment_params(params)

    my_output.default('Workflow Parameters', underline=True)
    display_params = copy.deepcopy(params)
    if 'instance' in display_params and display_params['instance'] is not None:
        display_params['instance'] = 'user-defined'

    my_output.default(json.dumps(display_params, indent=4), after_newline=True)

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
    params['namespace'] = 'openshift-sriov-network-operator'
    params['name'] = 'sriov-network-operator'
    params['operator-group-name'] = 'sriov-operator-group'
    params['config'] = {}
    params['config']['name'] = 'default'
    params['config']['injector'] = True
    params['config']['webhook'] = True
    params['delete-namespace'] = True
    return params

def augment_params(params):
    defaults = get_default_params()
    for key in defaults:
        params[key] = defaults[key]
    return params
