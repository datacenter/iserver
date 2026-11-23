def get_default_params():
    params = {}
    params['namespace'] = 'cisco-intersight'
    params['name'] = 'cisco-intersight'
    params['instance'] = 'cisco-intersight'
    params['secret'] = 'intersight-configurations'
    params['operator-group-name'] = 'cisco-intersight'
    params['delete-namespace'] = True
    params['create_subscription'] = 'create_intersight_subscription'
    params['delete_subscription'] = 'delete_intersight_subscription'
    params['title'] = 'OpenShift Workflow - Cisco Intersight Operator'
    return params