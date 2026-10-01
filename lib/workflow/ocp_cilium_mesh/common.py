def get_default_params():
    params = {}
    params['namespace'] = 'cilium'
    params['secret'] = 'cilium-ca-root'
    params['certificate'] = 'cilium-ocp'
    params['certificate-admin'] = 'clustermesh-apiserver-admin-cert'
    params['certificate-remote'] = 'clustermesh-apiserver-remote-cert'
    params['certificate-server'] = 'clustermesh-apiserver-server-cert'
    params['title'] = 'OpenShift Workflow - Cilium Cluster Mesh'
    return params