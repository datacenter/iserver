def get_default_params():
    params = {}
    params['namespace'] = 'openshift-nfd'
    params['name'] = 'nfd'
    params['catalog'] = 'redhat-operators'
    params['operator-group-name'] = 'nfd-operator-group'
    params['delete-namespace'] = True
    params['create_subscription'] = 'create_nfd_subscription'
    params['delete_subscription'] = 'delete_nfd_subscription'
    params['title'] = 'OpenShift Workflow - Node Feature Discovery Operator'
    return params