def get_default_params():
    params = {}
    params['namespace'] = 'openshift-local-storage'
    params['name'] = 'local-storage-operator'
    params['operator-group-name'] = 'local-operator-group'
    params['delete-namespace'] = True
    params['create_subscription'] = 'create_local_storage_subscription'
    params['delete_subscription'] = 'delete_local_storage_subscription'
    params['title'] = 'OpenShift Workflow - Local Storage'
    return params


def check_state(params, my_output, check_ready=True, check_resources=False):
    state = {}

    state['installed'] = params['k8s_handler'].check_local_storage_subscription(
        params['__default__']['name'], 
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
