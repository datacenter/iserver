def get_default_params():
    params = {}
    params['namespace'] = 'openshift-operators'
    params['name'] = 'trident-operator'
    params['operator-group-name'] = None
    params['catalog'] = 'certified-operators'
    params['create_subscription'] = 'create_trident_subscription'
    params['delete_subscription'] = 'delete_trident_subscription'
    params['delete-namespace'] = False
    params['title'] = 'OpenShift Workflow - Trident Operator'
    return params