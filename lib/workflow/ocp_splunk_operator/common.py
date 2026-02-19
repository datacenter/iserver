import json
from lib.workflow.ocp_access import check as ocp_check


def initialize(params, my_output, log_id, silent=False):
    params = augment_params(params)

    if not silent:
        my_output.default('Workflow Parameters', underline=True)
        my_output.default(json.dumps(params, indent=4), after_newline=True)

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
    # https://github.com/splunk/splunk-operator/blob/main/docs/OpenShift.md
    params = {}
    params['namespace'] = 'splunk-operator'
    params['name'] = 'splunk-operator'
    params['operator-group-name'] = 'splunk-operator-group'
    params['license-at-splunk'] = True
    params['role-binding'] = True
    params['role-binding-name'] = 'system:openshift:scc:nonroot-v2'
    params['pvc-finalizers'] = True
    params['delete-namespace'] = False
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
