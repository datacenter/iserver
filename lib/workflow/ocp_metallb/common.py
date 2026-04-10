def get_default_params():
    params = {}
    params['namespace'] = 'metallb-system'
    params['name'] = 'metallb-operator'
    params['operator-group-name'] = 'metallb-system'
    params['delete-namespace'] = True
    return params