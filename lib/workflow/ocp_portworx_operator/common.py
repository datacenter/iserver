def get_default_params():
    params = {}
    params['namespace'] = 'openshift-operators'
    params['name'] = 'portworx-certified'
    params['operator-group-name'] = None
    params['delete-namespace'] = False
    params['create_subscription'] = 'create_portworx_subscription'
    params['delete_subscription'] = 'delete_portworx_subscription'
    params['title'] = 'OpenShift Workflow - Portworx Operator'
    return params