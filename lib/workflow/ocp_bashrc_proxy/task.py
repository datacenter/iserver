from lib.workflow.ocp_bashrc_proxy import configure


def validate_create(task, cluster_name, confirmation, cluster_settings=None, k8s_handler=None):
    task['cluster'] = cluster_name
    task['confirmation'] = confirmation

    if not task['enabled']:
        return task, None

    # Proxy settings explicitly user provided

    all_keys = True
    keys = [
        'http_proxy',
        'https_proxy',
        'no_proxy'
    ]
    for key in keys:
        if key not in task:
            all_keys = False
            break

    if all_keys:
        return task, None
    
    # Proxy settings from cluster or cluster settings required

    if k8s_handler is None and cluster_settings is None:
        return None, 'Cluster handler or settings required'

    # Proxy settings from cluster settings    
    if cluster_settings is not None:
        keys = [
            'http_proxy',
            'https_proxy',
            'no_proxy'
        ]
        for key in keys:
            if key not in task:
                task[key] = None
                if key in cluster_settings:
                    task[key] = cluster_settings[key]

        return task, None
    
    # Proxy settings from cluster state

    proxy = k8s_handler.get_proxy()
    if proxy is None:
        return None, 'Failed to get proxy settings'
    
    task['http_proxy'] = proxy['http_proxy']
    task['https_proxy'] = proxy['https_proxy']
    task['no_proxy'] = proxy['no_proxy']
    
    return task, None
    
def run(params, log_id=None):
    if params['enabled']:
        return configure.run(params, log_id=log_id)
    
    return True