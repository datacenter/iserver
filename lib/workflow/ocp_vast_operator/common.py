import json
import copy
from lib.workflow.ocp_access import check as ocp_check


def initialize(params, my_output, log_id, ssh_check=False, ssh_required=False):
    params = augment_params(params)

    if params['verbose']:
        my_output.default('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        if 'instance' in display_params and display_params['instance'] is not None:
            display_params['instance'] = 'user-defined'
        my_output.default(json.dumps(display_params, indent=4), after_newline=True)
    else:
        my_output.debug('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        my_output.debug(json.dumps(display_params, indent=4), after_newline=True)
        
    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['ssh-check'] = ssh_check
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
    params['namespace'] = 'vast-csi'
    params['name'] = 'vast-csi-operator'
    params['operator-group-name'] = 'vast-operator-group'
    params['delete-namespace'] = True
    return params


def augment_params(params):
    defaults = get_default_params()
    for key in defaults:
        params[key] = defaults[key]
    return params


def sanitize_params(params, allowed_keys, allow_kwargs=False):
    new_params = {}
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    if allow_kwargs:
        new_params['kwargs'] = {}
        for key in params:
            if key not in allowed_keys:
                new_params['kwargs'][key] = params[key]

    return new_params

def check_state(params, my_output, check_ready=True, check_resources=False):
    state = {}

    state['installed'] = params['k8s_handler'].check_vast_subscription(
        params['name'], 
        my_output=my_output,
        check_ready=False
    )

    if not check_ready or not state['installed']:
        return state
    
    state['ready'] = params['k8s_handler'].is_subscription_vast_ready(my_output=my_output)

    if not check_resources:
        return state
    
    state['dependants'] = False

    state['driver'] = params['k8s_handler'].get_vast_drivers(cache_enabled=False)
    if state['driver'] is None:
        my_output.default('- %s driver' % (my_output.add_color('failed to get', 'Red')))
    else:
        my_output.default('- %s driver' % (len(state['driver'])))
        if len(state['driver']) > 0:
            state['dependants'] = True

    state['cluster'] = params['k8s_handler'].get_vast_clusters(cache_enabled=False)
    if state['cluster'] is None:
        my_output.default('- %s cluster' % (my_output.add_color('failed to get', 'Red')))
    else:
        my_output.default('- %s cluster' % (len(state['cluster'])))
        if len(state['cluster']) > 0:
            state['dependants'] = True

    state['storage'] = params['k8s_handler'].get_vast_storages(cache_enabled=False)
    storage_names = []
    if state['storage'] is None:
        my_output.default('- %s storage' % (my_output.add_color('failed to get', 'Red')))
    else:
        my_output.default('- %s storage' % (len(state['storage'])))
        if len(state['storage']) > 0:
            state['dependants'] = True

        for item in state['storage']:
            storage_names.append(
                item['name']
            )

    if len(storage_names) == 0:
        my_output.default('- 0 storage class')
        my_output.default('- 0 pvc')
        return state
    
    state['sc'] = []
    storage_class_names = []
    storage_classes = params['k8s_handler'].get_storage_classes(cache_enabled=False)
    if storage_classes is not None:
        for storage_class in storage_classes:
            if storage_class['name'] in storage_names:
                state['sc'].append(
                    storage_class
                )
                storage_class_names.append(
                    storage_class['name']
                )

    my_output.default('- %s storage class' % (len(state['sc'])))
    
    if len(state['sc']) == 0:
        my_output.default('- 0 pvc')
        return state

    state['pvc'] = []
    pvcs = params['k8s_handler'].get_pvcs(cache_enabled=False)
    if pvcs is not None:
        for pvc in pvcs:
            if pvc['storage_class_name'] in storage_class_names:
                state['pvc'].append(
                    pvc
                )

    my_output.default('- %s pvc' % (len(state['pvc'])))
    if len(state['pvc']) > 0:
        state['dependants'] = True

    return state
