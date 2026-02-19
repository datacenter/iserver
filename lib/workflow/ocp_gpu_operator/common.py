import json
import copy
from lib.workflow.ocp_access import check as ocp_check


def initialize(params, my_output, log_id):
    params = augment_params(params)

    if params['verbose']:
        my_output.default('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        if 'policy' in display_params and display_params['policy'] is not None:
            display_params['policy'] = 'user-defined'
        my_output.default(json.dumps(display_params, indent=4), after_newline=True)
    else:
        my_output.debug('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        if 'policy' in display_params and display_params['policy'] is not None:
            display_params['policy'] = 'user-defined'
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
    params['namespace'] = 'nvidia-gpu-operator'
    params['name'] = 'gpu-operator-certified'
    params['operator-group-name'] = 'gpu-operator-group'
    params['delete-namespace'] = True
    params['ds-dcgm'] = 'nvidia-dcgm'
    params['ds-dcgm-exporter'] = 'nvidia-dcgm-exporter'
    params['monitoring'] = {}
    params['monitoring']['dashboard_url'] = 'https://github.com/NVIDIA/dcgm-exporter/raw/main/grafana/dcgm-exporter-dashboard.json'
    params['monitoring']['dashboard_namespace'] = 'openshift-config-managed'
    params['monitoring']['dashboard_name'] = 'nvidia-dcgm-exporter-dashboard'
    params['monitoring']['admin'] = True
    params['monitoring']['developer'] = False
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