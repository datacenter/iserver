def get_default_params():
    params = {}
    params['namespace'] = 'splunk-operator'
    params['name'] = 'splunk-operator'
    params['operator-group-name'] = 'splunk-operator-group'
    params['operator-target-namespaces'] = ['splunk-operator']
    params['license-at-splunk'] = True
    params['role-binding'] = True
    params['role-binding-name'] = 'system:openshift:scc:nonroot-v2'
    params['pvc-finalizers'] = True
    params['delete-namespace'] = True
    params['create_subscription'] = 'create_splunk_subscription'
    params['delete_subscription'] = 'delete_splunk_subscription'
    params['title'] = 'OpenShift Workflow - Splunk Operator'
    params['resource_keys'] = [
        'standalone',
        'cluster_master',
        'cluster_manager',
        'indexer_cluster',
        'license_manager',
        'license_master',
        'monitoring_console',
        'search_head_cluster'
    ]
    params['resource_output'] = [
        ['standalone', 'standalone'],
        ['cluster master', 'cluster_master'],
        ['cluster manager', 'cluster_manager'],
        ['indexer cluster', 'indexer_cluster'],
        ['license manager', 'license_manager'],
        ['license master', 'license_master'],
        ['monitoring console', 'monitoring_console'],
        ['search head cluster', 'search_head_cluster']
    ]
    return params


def collect_state_info(params, my_output):
    params['summary']['resources'] = False

    my_output.debug('- standalone')
    params['standalone'] = params['k8s_handler'].get_splunk_standalones(
        pod_info=True,
        pvc_info=True,
        service_info=True,
        route_info=True,
        secret_info=True
    )

    for key in params['__default__']['resource_keys']:
        if key == 'standalone':
            continue

        my_output.debug('- %s' % (key.replace('_', ' ')))
        params[key] = getattr(params['k8s_handler'], 'get_splunk_%ss' % (key))(cache_enabled=False)

    for key in params['__default__']['resource_keys']:
        params['summary'][key] = '---'
        if params[key] is not None:
            params['summary'][key] = len(params[key])
            if len(params[key]) > 0:
                params['summary']['resources'] = True

    return params