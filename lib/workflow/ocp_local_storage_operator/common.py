import copy
import json
from lib.workflow.ocp_access import check as ocp_check


def initialize(params, my_output, log_id, ssh_required=False):
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
    ocp_check_params['ssh-required'] = ssh_required
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return None

    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler

    params['ssh-ready'] = False
    if 'ssh_public_key' in ocp_check_params['data']:
        params['ssh-ready'] = True

    return params


def get_default_params():
    params = {}
    params['namespace'] = 'openshift-local-storage'
    params['name'] = 'local-storage-operator'
    params['operator-group-name'] = 'local-operator-group'
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


def check_state(params, my_output, check_ready=True, check_resources=False):
    state = {}

    state['installed'] = params['k8s_handler'].check_local_storage_subscription(
        params['name'], 
        my_output=my_output,
        check_ready=False
    )

    if not check_ready or not state['installed']:
        return state
    
    state['ready'] = params['k8s_handler'].is_subscription_local_storage_ready(my_output=my_output)

    if not check_resources:
        return state
    
    state['dependants'] = False

    state['local_volume'] = params['k8s_handler'].get_local_volumes(cache_enabled=False)
    if state['local_volume'] is None:
        my_output.default('- %s local volume' % (my_output.add_color('failed to get', 'Red')))
    else:
        my_output.default('- %s local volume' % (len(state['local_volume'])))
        if len(state['local_volume']) > 0:
            state['dependants'] = True

    state['local_volume_set'] = params['k8s_handler'].get_local_volume_sets(cache_enabled=False)
    if state['local_volume_set'] is None:
        my_output.default('- %s local volume set' % (my_output.add_color('failed to get', 'Red')))
    else:
        my_output.default('- %s local volume set' % (len(state['local_volume_set'])))
        if len(state['local_volume_set']) > 0:
            state['dependants'] = True

    state['local_volume_discovery'] = params['k8s_handler'].get_local_volume_discoveries(cache_enabled=False)
    if state['local_volume_discovery'] is None:
        my_output.default('- %s local volume discovery' % (my_output.add_color('failed to get', 'Red')))
    else:
        my_output.default('- %s local volume discovery' % (len(state['local_volume_discovery'])))
        if len(state['local_volume_discovery']) > 0:
            state['dependants'] = True

    state['local_volume_discovery_result'] = params['k8s_handler'].get_local_volume_discovery_results(cache_enabled=False)
    if state['local_volume_discovery_result'] is None:
        my_output.default('- %s local volume discovery result' % (my_output.add_color('failed to get', 'Red')))
    else:
        my_output.default('- %s local volume discovery result' % (len(state['local_volume_discovery_result'])))
        if len(state['local_volume_discovery_result']) > 0:
            state['dependants'] = True

    return state
