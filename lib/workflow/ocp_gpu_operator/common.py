def get_default_params():
    params = {}
    params['namespace'] = 'nvidia-gpu-operator'
    params['name'] = 'gpu-operator-certified'
    params['operator-group-name'] = 'gpu-operator-group'
    params['delete-namespace'] = True
    params['ds-dcgm'] = 'nvidia-dcgm'
    params['ds-dcgm-exporter'] = 'nvidia-dcgm-exporter'
    params['monitoring'] = {}
    params['monitoring']['dashboard_url'] = 'https://github.com/NVIDIA/dcgm-exporter/raw/main/grafana/dcgm-exporter-dashboard.json'
    params['monitoring']['dashboard_namespace'] = 'openshift-config-managed'
    params['monitoring']['dashboard_name'] = 'nvidia-dcgm-exporter-dashboard'
    params['monitoring']['admin'] = True
    params['monitoring']['developer'] = False
    params['title'] = 'OpenShift Workflow - GPU Operator'
    return params