def get_default_params():
    params = {}
    params['namespace'] = 'cert-manager'
    params['helm'] = 'cert-manager'
    params['repo_name'] = 'jetstack'
    params['repo_url'] = 'https://charts.jetstack.io'
    params['repo'] = '%s %s' % (params['repo_name'], params['repo_url'])
    params['title'] = 'OpenShift Workflow - Certificate Manager'
    params['resource_keys'] = [
        'cluster issuer',
        'issuer',
        'certificate request',
        'certificate'
    ]
    params['resource_output'] = [
        ['cluster issuer', 'cluster issuer'],
        ['issuer', 'issuer'],
        ['certificate request', 'certificate request'],
        ['certificate', 'certificate']
    ]
    return params


def collect_state_info(params, resource=True):
    params['state'] = {}
    params['state']['repo'] = params['mgmt_linux_handler'].get_helm_repo(object_filter=['name:%s' % (params['__default__']['repo_name'])], cache_enabled=False)
    params['state']['chart'] = params['mgmt_linux_handler'].get_helm_chart(object_filter=['name:%s' % (params['__default__']['helm'])], cache_enabled=False)
    if resource:
        params = collect_resource_info(params)
    return params


def collect_resource_info(params):
    params['state']['resources'] = False
    params['resource'] = {}  
    params['state']['crd'] = True
    for key in params['__default__']['resource_keys']:
        if key in ['certificate request']:
            params['resource'][key] = getattr(params['k8s_handler'], 'get_%ss' % (key.replace(' ', '_')))(cache_enabled=False)
        else:
            params['resource'][key] = getattr(params['k8s_handler'], 'get_%ss' % (key.replace(' ', '_')))(secret_info=True, cache_enabled=False)
        if params['resource'][key] is None:
            print(key)
            params['state']['crd'] = False

    params['resource_summary'] = {}
    for key in params['__default__']['resource_keys']:
        params['resource_summary'][key] = '---'
        if params['resource'][key] is not None:
            params['resource_summary'][key] = len(params['resource'][key])
            if len(params['resource'][key]) > 0:
                params['state']['resources'] = True

    return params


def print_state(params, my_output, linux_output_handler):
    if params['state']['repo'] is None:
        my_output.default('Repository %s %s' % (
            params['__default__']['repo_name'],
            my_output.add_color('not found', 'Red')
        ))
        return

    if params['state']['chart'] is None:
        my_output.default('Package %s %s' % (
            params['__default__']['helm'],
            my_output.add_color('not found', 'Red')
        ))
        return
    
    linux_output_handler.print_helm_charts_state([params['state']['chart']])
    print_resource_summary(params, my_output)


def print_resource_summary(params, my_output):
    my_output.dictionary_ng(
        'Certificate Manager Resources',
        params['resource_summary'],
        params['__default__']['resource_output']
    )   


def print_resources(params, k8s_output_handler):
    for key in params['__default__']['resource_keys']:
        if params['resource'][key] is None:
            continue

        if len(params['resource'][key]) == 0:
            continue

        getattr(k8s_output_handler, 'print_%ss_state' % (key.replace(' ', '_')))(params['resource'][key])
