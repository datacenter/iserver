def get_default_params():
    params = {}
    params['namespace'] = 'vast-csi'
    params['name'] = 'vast-csi-operator'
    params['operator-group-name'] = 'vast-operator-group'
    params['catalog'] = 'certified-operators'
    params['delete-namespace'] = True
    params['create_subscription'] = 'create_vast_subscription'
    params['delete_subscription'] = 'delete_vast_subscription'
    params['title'] = 'OpenShift Workflow - VAST CSI Operator'
    return params

def check_state(params, my_output, check_ready=True, check_resources=False):
    state = {}

    state['installed'] = params['k8s_handler'].check_vast_subscription(
        params['__default__']['name'], 
        my_output=my_output,
        check_ready=False
    )

    if not check_ready or not state['installed']:
        return state
    
    state['ready'] = params['k8s_handler'].is_subscription_vast_ready(my_output=my_output)

    if not check_resources:
        return state
    
    state['dependants'] = False

    my_output.default('VAST CSI Custom Resources', before_newline=True)

    state['driver'] = params['k8s_handler'].get_vast_drivers(cache_enabled=False)
    params['k8s_handler'].get_vast_drivers_summary(
        state['driver'],
        my_output=my_output,
        prefix='- '
    )

    if state['driver'] is not None and len(state['driver']) > 0:
        state['dependants'] = True

    state['cluster'] = params['k8s_handler'].get_vast_clusters(cache_enabled=False)
    params['k8s_handler'].get_vast_clusters_summary(
        state['cluster'],
        my_output=my_output,
        prefix='- '
    )

    if state['cluster'] is not None and len(state['cluster']) > 0:
        state['dependants'] = True

    state['storage'] = params['k8s_handler'].get_vast_storages(cache_enabled=False)
    params['k8s_handler'].get_vast_storages_summary(
        state['cluster'],
        my_output=my_output,
        prefix='- '
    )

    storage_names = []
    if state['storage'] is not None:
        if len(state['storage']) > 0:
            state['dependants'] = True

        for item in state['storage']:
            storage_names.append(
                item['name']
            )

    my_output.default('Kubernetes Resources', before_newline=True)

    state['dep'] = params['k8s_handler'].get_deployments(object_filter=['namespace:%s' % (params['__default__']['namespace'])])
    params['k8s_handler'].get_deployments_summary(
        state['dep'],
        my_output=my_output,
        prefix='- '
    )

    state['ds'] = params['k8s_handler'].get_daemon_sets(object_filter=['namespace:%s' % (params['__default__']['namespace'])])
    params['k8s_handler'].get_daemon_sets_summary(
        state['ds'],
        my_output=my_output,
        prefix='- '
    )

    state['pod'] = params['k8s_handler'].get_pods(namespace=params['__default__']['namespace'])
    params['k8s_handler'].get_pods_summary(
        state['pod'],
        my_output=my_output,
        prefix='- '
    )

    if len(storage_names) == 0:
        my_output.default('- 0/0 default StorageClass')
        my_output.default('- 0/0 PersistentVolumeClaim')
        return state
    
    state['sc'] = params['k8s_handler'].get_storage_classes(object_filter=['names:%s' % (','.join(storage_names))], cache_enabled=False)
    params['k8s_handler'].get_storage_classes_summary(
        state['sc'],
        my_output=my_output,
        prefix='- '
    )

    if state['sc'] is None or len(state['sc']) == 0:
        my_output.default('- 0 PersistentVolumeClaim')
        return state

    state['pvc'] = params['k8s_handler'].get_pvcs(object_filter=['scs:%s' % (','.join(storage_names))], cache_enabled=False)
    params['k8s_handler'].get_pvcs_summary(
        state['pvc'],
        my_output=my_output,
        prefix='- '
    )
        
    if state['pvc'] is not None and len(state['pvc']) > 0:
        state['dependants'] = True

    return state