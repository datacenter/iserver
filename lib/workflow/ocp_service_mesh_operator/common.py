def get_default_params():
    params = {}
    params['namespace'] = 'openshift-operators'
    params['name'] = 'servicemeshoperator'
    params['operator-group-name'] = None
    params['operator-add-target-namespace'] = False
    params['delete-namespace'] = False
    params['create_subscription'] = 'create_service_mesh_subscription'
    params['delete_subscription'] = 'delete_service_mesh_subscription'
    params['title'] = 'OpenShift Workflow - Service Mesh Operator'
    return params