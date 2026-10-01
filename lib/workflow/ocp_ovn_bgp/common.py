def get_default_params():
    params = {}
    params['namespace'] = 'openshift-frr-k8s'
    params['delete-namespace'] = True
    params['title'] = 'OpenShift Workflow - OVN BGP'
    return params