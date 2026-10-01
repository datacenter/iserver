def get_default_params():
    params = {}
    params['namespace'] = 'openshift-serverless'
    params['name'] = 'serverless-operator'
    params['operator-group-name'] = 'serverless-operator-group'
    params['operator-add-target-namespace'] = False
    params['delete-namespace'] = True
    params['create_subscription'] = 'create_serverless_subscription'
    params['delete_subscription'] = 'delete_serverless_subscription'
    params['title'] = 'OpenShift Workflow - Serverless Operator'
    return params