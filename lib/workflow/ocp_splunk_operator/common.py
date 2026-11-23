import yaml
from lib import file_helper
from lib import ip_helper


def get_default_params():
    params = {}
    params['namespace'] = 'splunk-operator'
    params['name'] = 'splunk-operator'
    params['operator-group-name'] = 'splunk-operator-group'
    params['operator-target-namespaces'] = ['splunk-operator']
    params['deployment'] = 'splunk-operator-controller-manager'
    params['base_url'] = 'https://github.com/splunk/splunk-operator/releases/download/%s/splunk-operator-cluster.yaml'
    params['license-at-splunk'] = True
    params['role-binding'] = True
    params['role-binding-name'] = 'system:openshift:scc:nonroot-v2'
    params['pvc-finalizers'] = True
    params['delete-namespace'] = True
    params['title'] = 'OpenShift Workflow - Splunk Operator'
    params['resource_keys'] = [
        'standalone',
        'cluster_master',
        'cluster_manager',
        'indexer_cluster',
        'license_manager',
        'license_master',
        'monitoring_console',
        'search_head_cluster'
    ]
    params['resource_output'] = [
        ['standalone', 'standalone'],
        ['cluster master', 'cluster_master'],
        ['cluster manager', 'cluster_manager'],
        ['indexer cluster', 'indexer_cluster'],
        ['license manager', 'license_manager'],
        ['license master', 'license_master'],
        ['monitoring console', 'monitoring_console'],
        ['search head cluster', 'search_head_cluster']
    ]
    return params


def collect_state_info(params):
    params['summary'] = {}
    params['summary']['resources'] = False

    params['standalone'] = params['k8s_handler'].get_splunk_standalones(
        pod_info=True,
        pvc_info=True,
        service_info=True,
        route_info=True,
        secret_info=True
    )

    for key in params['__default__']['resource_keys']:
        if key == 'standalone':
            continue

        params[key] = getattr(params['k8s_handler'], 'get_splunk_%ss' % (key))(cache_enabled=False)

    for key in params['__default__']['resource_keys']:
        params['summary'][key] = '---'
        if params[key] is not None:
            params['summary'][key] = len(params[key])
            if len(params[key]) > 0:
                params['summary']['resources'] = True

    return params


def get_body(params, my_output):
    operator_yaml_source = params['__default__']['base_url'] % (params['version'])
    operator_yaml = '/tmp/splunk_operator.yaml'
    my_output.default('Download manifest from: %s to %s' % (operator_yaml_source, operator_yaml))

    operator_yaml, error = ip_helper.download_url(
        operator_yaml_source,
        operator_yaml,
        return_error=True,
        proxies=ip_helper.get_proxies()
    )
    if operator_yaml is None:
        my_output.error('Download failed')
        my_output.default(error, wrap='~~~')
        return None

    operator_yaml_body = file_helper.get_file_yaml(operator_yaml)
    if operator_yaml_body is None:
        my_output.error('Failed to read yaml content')
        return None

    for item in operator_yaml_body:
        if not file_helper.is_kube_kind(item):
            my_output.error('Unexpected content')
            my_output.default(item, wrap='~~~')
            return None

    my_output.default('File downloaded with %s crds' % (len(operator_yaml_body)))

    return operator_yaml_body