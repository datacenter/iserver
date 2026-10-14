def get_default_params():
    params = {}
    params['namespace'] = 'openshift-console'
    params['deployment'] = 'console'
    params['title'] = 'OpenShift Workflow - Console REST API'
    params['state_output'] = [
        ['management mode', 'management'],
        ['enabled plugins', 'plugin'],
        ['deployment', 'deployment'],
        ['pod', 'pod'],
        ['url', 'url']
    ]
    return params

def collect_state_info(params):
    params['resource'] = {}
    params['state'] = {}
    params['state']['__Output'] = {}

    # route

    object_filter = []
    object_filter.append('namespace:%s' % (params['__default__']['namespace']))
    object_filter.append('name:console')

    params['resource']['route'] = None
    params['state']['url'] = '---'

    routes = params['k8s_handler'].get_routes(
        object_filter=object_filter
    )
    if routes is not None and len(routes) == 1:
        params['resource']['route'] = routes[0]
        params['state']['url'] = params['resource']['route']['routeT']

    # deployment

    params['resource']['deployment'] = params['k8s_handler'].get_deployment(
        params['__default__']['namespace'],
        params['__default__']['deployment']
    )

    params['state']['deployment'] = '---'
    if params['resource']['deployment'] is not None:
        params['state']['deployment'] = params['resource']['deployment']['readyT']
        params['state']['__Output']['deployment'] = params['resource']['deployment']['__Output']['readyT']

    # deployment resources

    resources = params['k8s_handler'].get_deployment_resources(
        params['__default__']['namespace'],
        params['__default__']['deployment'],
        details=True
    )
    for key in resources:
        params['resource'][key] = resources[key]

    pod_summary = params['k8s_handler'].get_pods_summary(params['resource']['pod'])
    params['state']['pod'] = '%s/%s' % (pod_summary['ready'], pod_summary['count'])
    params['state']['__Output']['pod'] = 'Green'
    if pod_summary['count'] == 0 or pod_summary['count'] != pod_summary['ready']:
        params['state']['__Output']['pod'] = 'Red'
    
    # console.operator

    params['resource']['operator'] = None
    params['state']['management'] = '---'
    params['state']['plugin'] = '---'

    params['resource']['operator'] = params['k8s_handler'].get_operator_console(
        'cluster'
    )
    if params['resource']['operator'] is not None:
        params['state']['management'] = params['resource']['operator']['management']
        params['state']['plugin'] = params['resource']['operator']['pluginT']

    return params


def print_state(params, my_output):
    my_output.dictionary_ng(
        'Web Console State',
        params['state'],
        params['__default__']['state_output']
    )   


def print_resources(params, k8s_output_handler):
    k8s_output_handler.print_deployment(params['resource']['deployment'])
    k8s_output_handler.print_replica_sets_state(params['resource']['rs'])
    k8s_output_handler.print_pods_state(params['resource']['pod'])
    k8s_output_handler.print_operator_consoles_state(params['resource']['operator'])