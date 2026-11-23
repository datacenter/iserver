def get_default_params():
    params = {}
    params['namespace'] = 'openshift-operators'
    params['name'] = 'nim-operator-certified'
    params['operator-group-name'] = None
    params['delete-namespace'] = False
    params['create_subscription'] = 'create_nim_subscription'
    params['delete_subscription'] = 'delete_nim_subscription'
    params['title'] = 'OpenShift Workflow - NVIDIA NIM Operator'
    return params