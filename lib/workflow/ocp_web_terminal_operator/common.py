def get_default_params():
    params = {}
    params['namespace'] = 'openshift-operators'
    params['name'] = 'web-terminal'
    params['operator-group-name'] = None
    params['workspace'] = 'devworkspace-operator'
    params['terminal-ns'] = 'openshift-terminal'
    params['delete-namespace'] = False
    params['create_subscription'] = 'create_web_terminal_subscription'
    params['delete_subscription'] = 'delete_web_terminal_subscription'
    params['title'] = 'OpenShift Workflow - Web Terminal Operator'
    return params