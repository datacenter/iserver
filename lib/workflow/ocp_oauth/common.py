import copy
import json
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
    params['default'] = {}
    params['default']['auth-namespace'] = 'openshift-authentication'
    params['default']['operator-namespace'] = 'openshift-authentication-operator'
    params['default']['apiserver-namespace'] = 'openshift-oauth-apiserver'
    params['default']['co'] = 'authentication'
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


def get_state_co(params, cache_enabled=False):
    params['state']['co'] = params['k8s_handler'].get_cluster_operator(
        params['default']['co'],
        cache_enabled=cache_enabled
    )
    return params


def get_state(params, scope=None, cache_enabled=False):
    if scope is None:
        scope = ['co', 'group']

    if 'state' not in params:
        params['state'] = {}

    get_map = {}
    get_map['group'] = 'get_groups'

    for item in scope:
        if item in get_map:
            params['state'][item] = getattr(params['k8s_handler'], get_map[item])(cache_enabled=cache_enabled)
            continue

        func_name = 'get_state_%s' % (item)
        params = globals()[func_name](params, cache_enabled=cache_enabled)

    return params


def print_state(params, my_output, k8s_output_handler, scope=None, summary=False):
    print_map = {}
    print_map['co'] = 'print_cluster_operator'
    print_map['group'] = 'print_groups_state'

    if scope is None:
        scope = list(print_map.keys())

    for item in scope:
        if item not in params['state']:
            my_output.error('Exception: %s not collected' % (item))
            continue

        if params['state'][item] is None:
            my_output.error('%s get failed' % (item))
            continue

        getattr(k8s_output_handler, print_map[item])(params['state'][item])
        