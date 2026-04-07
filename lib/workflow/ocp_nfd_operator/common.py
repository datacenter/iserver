def get_default_params():
    params = {}
    params['namespace'] = 'openshift-nfd'
    params['name'] = 'nfd'
    params['operator-group-name'] = 'nfd-operator-group'
    params['delete-namespace'] = True
    return params