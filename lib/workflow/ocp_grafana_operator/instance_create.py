from lib import output_helper
from lib.workflow.ocp_grafana_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'instance' not in params:
        return None, 'instance name required'

    if not isinstance(params['instance'], str):
        return None, 'instance param must be string'

    if 'username' not in params:
        return None, 'username value required'

    if params['username'] is None:
        return None, 'username non-null value required'
    
    if not isinstance(params['username'], str):
        return None, 'username param must be string'

    if 'password' not in params:
        return None, 'password required'

    if params['password'] is None:
        return None, 'password non-null value required'

    if not isinstance(params['password'], str):
        return None, 'password param must be string'

    if 'prometheus' not in params:
        params['prometheus'] = False

    if not isinstance(params['prometheus'], bool):
        return None, 'prometheus param must be true or false'
        
    if 'datasource' not in params:
        params['datasource'] = 'my-prometheus'

    if not isinstance(params['datasource'], str):
        return None, 'datasource param must be string'
    
    if 'confirmation' not in params:
        params['confirmation'] = False

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'
        
    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'instance',
        'username',
        'password',
        'prometheus',
        'datasource',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


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

            if crb_subject['namespace'] != params['namespace']:
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
            params['namespace']
        )
        if crb_name is None:
            my_output.error('Failed to create cluster role binding')
            return None

        my_output.default('Cluster role binding created: %s' % (crb_name))

    return params


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Grafana Operator - Create Instance', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not params['k8s_handler'].is_grafana_subscription(params['namespace'], params['name']):
        my_output.error('Grafana Operator is not installed')
        return False
    
    instance_namespace = params['namespace']
    instance_name = params['instance']
    if params['k8s_handler'].is_grafana(instance_namespace, instance_name, cache_enabled=False):
        my_output.default('Grafana instance [%s/%s] already defined' % (instance_namespace, instance_name))
    else:
        success = params['k8s_handler'].create_grafana(
            params['namespace'], 
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
            params['namespace'], 
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
