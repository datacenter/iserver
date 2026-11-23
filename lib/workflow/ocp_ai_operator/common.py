def get_default_params():
    params = {}
    params['namespace'] = 'redhat-ods-operator'
    params['application-namespace'] = 'redhat-ods-applications'
    params['monitoring-namespace'] = 'redhat-ods-monitoring'
    params['notebook-namespace'] = 'rhods-notebooks'
    params['model-namespace'] = 'rhoai-model-registries'
    params['name'] = 'rhods-operator'
    params['mesh'] = 'servicemeshoperator'
    params['serverless'] = 'serverless-operator'
    params['operator-group-name'] = 'ods-operator-group'
    params['delete-namespace'] = True
    params['title'] = 'OpenShift Workflow - Data Science (AI)'
    return params