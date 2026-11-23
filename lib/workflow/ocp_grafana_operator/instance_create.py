from lib import output_helper
from lib.workflow.ocp_grafana_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['instance', False, None, 'str', None, None, None, None],
        ['username', False, None, 'str', None, None, None, None],
        ['password', False, None, 'str', None, None, None, None],
        ['prometheus', True, False, 'bool', None, None, None, None],
        ['datasource', True, 'my-prometheus', 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def add_cluster_role_binding(params, my_output):
    my_output.default('Cluster Role Binding', underline=True, before_newline=True)

    object_filter = ['role:cluster-monitoring-view']
    crbs = params['k8s_handler'].get_cluster_role_bindings(object_filter=object_filter, cache_enabled=False)
    if crbs is None:
        my_output.error('Unexpected exception in cluster role binding api call')
        return None

    found = False
    sa_name = '%s-sa' % (params['instance'])
    crb_name = None
    for crb in crbs:
        for crb_subject in crb['subject']:
            if crb_subject['kind'] != 'ServiceAccount':
                continue

            if crb_subject['namespace'] != params['__default__']['namespace']:
                continue

            if crb_subject['name'] != sa_name:
                continue

            crb_name = crb['name']
            found = True

    if found:
        my_output.default(
            'Service Account [%s] already associated with role [cluster-monitoring-view] in ClusterRoleBinding CR [%s]' % (
                sa_name,
                crb_name
            )
        )

    if not found:
        my_output.default('Service Account [%s] is not yet associated with role [cluster-monitoring-view]' % (sa_name))

        crb_name = '%s-sa-view' % (params['instance'])
        crb_name = params['k8s_handler'].create_service_account_cluster_role_binding(
            crb_name,
            'cluster-monitoring-view',
            sa_name,
            params['__default__']['namespace']
        )
        if crb_name is None:
            my_output.error('Failed to create cluster role binding')
            return None

        my_output.default('Cluster role binding created: %s' % (crb_name))

    return params


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Create Instance')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    if not params['k8s_handler'].is_grafana_subscription(params['__default__']['namespace'], params['__default__']['name']):
        my_output.error('Grafana Operator is not installed')
        return False
    
    instance_namespace = params['__default__']['namespace']
    instance_name = params['instance']
    if params['k8s_handler'].is_grafana(instance_namespace, instance_name, cache_enabled=False):
        my_output.default('Grafana instance [%s/%s] already defined' % (instance_namespace, instance_name))
    else:
        success = params['k8s_handler'].create_grafana(
            params['__default__']['namespace'], 
            params['instance'], 
            username=params['username'],
            password=params['password'],
            route=True,
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

    if params['prometheus']:
        if not local_common.check_user_workload_monitoring(params, my_output):
            my_output.error('Prometheus data source requested and user workload monitoring disabled. Enable it first')
            return False

        params = add_cluster_role_binding(params, my_output)
        if params is None:
            return False

        success = params['k8s_handler'].create_grafana_datasource_thanos(
            params['__default__']['namespace'], 
            params['instance'], 
            params['datasource'], 
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False
    
    my_output.default('')
    my_output.default('Completed tasks', underline=True, before_newline=True)
    my_output.default('- Grafana instance defined')
    if params['prometheus']:
        my_output.default('- Prometheus data source created')

    return True
