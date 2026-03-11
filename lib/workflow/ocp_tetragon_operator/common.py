import json
import yaml
import copy
from lib import filter_helper
from lib.workflow.ocp_access import check as ocp_check


def initialize(params, my_output, log_id):
    params = augment_params(params)

    my_output.default('Workflow Parameters', underline=True)
    display_params = copy.deepcopy(params)
    if 'image' in display_params and display_params['image'] is not None:
        display_params['image'] = 'user-defined'

    if 'crd' in display_params and display_params['crd'] is not None:
        display_params['crd'] = 'user-defined'

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
    params['namespace'] = 'tetragon'
    params['name'] = 'tetragon-operator'
    params['operator-group-name'] = 'tetragon'
    params['catalog-namespace'] = 'tetragon'
    params['catalog-name'] = 'tetragon-catalog'
    params['operator-cm-namespace'] = 'tetragon'
    params['operator-cm-name'] = 'tetragon-operator-config'
    params['cm-namespace'] = 'tetragon'
    params['cm-name'] = 'tetragon-config'
    params['sm-namespace'] = 'tetragon'
    params['sm-name'] = 'tetragon'
    params['delete-namespace'] = True
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


def is_tetragon_crd(kind):
    crds = [
        'AlertRule',
        'SandboxPolicy',
        'SandboxPolicyNamespaced',
        'TetragonNetworkPolicy',
        'TetragonNetworkPolicyNamespaced',
        'TracingPolicy',
        'TracingPolicyNamespaced'
    ]
    if kind in crds:
        return True
    return False


def get_operator_config(params, my_output):
    config_map_mo = params['k8s_handler'].get_config_map(params['operator-cm-namespace'], params['operator-cm-name'], cache_enabled=False, return_mo=True)
    if config_map_mo is None:
        my_output.error('Config map [%s/%s] not found' % (params['operator-cm-namespace'], params['operator-cm-name']))
        return None, None

    my_output.default('Config map [%s/%s] found' % (params['operator-cm-namespace'], params['operator-cm-name']))

    data_mo = filter_helper.get(config_map_mo, 'data:agentDaemonSet')
    if data_mo is None:
        my_output.error('Unsupported config map body: agentDaemonSet missing')
        return None, None

    my_output.default('agentDaemonSet found in config map data')
    try:
        config = yaml.safe_load(data_mo)
    except BaseException:
        my_output.error('Unexpected failure in yaml to json cast of cm data')
        return None, None

    return config_map_mo, config


def update_operator_config(data, params, my_output):
    success = params['k8s_handler'].update_config_map(
        params['operator-cm-namespace'],
        params['operator-cm-name'],
        data,
        confirmation=params['confirmation'],
        my_output=my_output
    )
    if not success:
        return False

    if not params['k8s_handler'].restart_deployment(params['namespace'], params['name']):
        my_output.error('Failed to restart deployment [%s/%s]' % (params['namespace'], params['name']))
        return False

    my_output.default('Deployment [%s/%s] restarted' % (params['namespace'], params['name']))
    return True