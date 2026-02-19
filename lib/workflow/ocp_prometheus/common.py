import json
import yaml
import copy
from lib import filter_helper
from lib.workflow.ocp_access import check as ocp_check


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
    params['mon-namespace'] = 'openshift-monitoring'
    params['mon-name'] = 'cluster-monitoring-config'
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


def check_user_workload_monitoring(params, my_output):
    my_output.default('Check User Workload Monitoring', before_newline=True, underline=True)
    my_output.default('- config map namespace: %s' % (params['mon-namespace']))
    my_output.default('- config map name: %s' % (params['mon-name']))

    config_map_mo = params['k8s_handler'].get_config_map(
        params['mon-namespace'], 
        params['mon-name'], 
        cache_enabled=False, 
        return_mo=True
    )
    if config_map_mo is None:
        my_output.default('- not found <=> user workload monitoring disabled')
        return False

    data_mo = filter_helper.get(config_map_mo, 'data:config.yaml')
    if data_mo is None:
        my_output.error('Unsupported config map body')
        my_output.default(config_map_mo, before_newline=True, wrap='~~~')
        return False

    try:
        data_json = yaml.safe_load(data_mo)
    except BaseException:
        my_output.error('Unexpected failure in yaml to json cast of cm data')
        return False

    if 'enableUserWorkload' not in data_json or not data_json['enableUserWorkload']:
        my_output.default('- enableUserWorkload disabled')
        return False
    
    my_output.default('- enableUserWorkload enabled')
    return True

