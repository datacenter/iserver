def get_default_params():
    params = {}
    params['namespace'] = 'openshift-nmstate'
    params['name'] = 'kubernetes-nmstate-operator'
    params['operator-group-name'] = 'nmstate-operator-group'
    params['delete-namespace'] = True
    params['create_subscription'] = 'create_nmstate_subscription'
    params['delete_subscription'] = 'delete_nmstate_subscription'
    params['title'] = 'OpenShift Workflow - NMState Operator'
    return params