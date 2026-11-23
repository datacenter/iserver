def get_default_params():
    params = {}
    params['namespace'] = 'openshift-sriov-network-operator'
    params['name'] = 'sriov-network-operator'
    params['operator-group-name'] = 'sriov-operator-group'
    params['config'] = {}
    params['config']['name'] = 'default'
    params['config']['injector'] = True
    params['config']['webhook'] = True
    params['delete-namespace'] = True
    params['create_subscription'] = 'create_sriov_subscription'
    params['delete_subscription'] = 'delete_sriov_subscription'
    params['title'] = 'OpenShift Workflow - SRIOV Operator'
    return params