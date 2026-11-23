from menu.common import get_confirmation


def get_default_params():
    params = {}
    params['title'] = 'OpenShift Workflow - Pod'
    return params


def select_pods(params, my_output, k8s_output_handler):
    object_filter = []
    if params['namespace'] is not None:
        object_filter.append('namespace:%s' % (params['namespace']))
    if params['name'] is not None:
        object_filter.append('name:%s' % (params['name']))

    pods = params['k8s_handler'].get_pods(
        object_filter=object_filter,
        cache_enabled=False
    )

    if pods is None:
        my_output.error('Failed to get pods')
        return False, None
    
    if len(pods) == 0:
        my_output.default('No pod found')
        return True, None
    
    k8s_output_handler.print_pods_state(pods)

    if params['confirmation']:
        if not get_confirmation():
            return False, None

    return True, pods


def get_pod(params, namespace, name, my_output, k8s_output_handler=None):
    info = params['k8s_handler'].get_pod(
        namespace,
        name,
        cache_enabled=False
    )
    if info is None:
        my_output.error('POD %s/%s not found' % (namespace, name))
        return None
    
    if k8s_output_handler is not None:
        k8s_output_handler.print_pods_state([info])

    return info


def add_params(params, content):
    if params['node'] is not None:
        content['spec']['nodeName'] = params['node']

    return content