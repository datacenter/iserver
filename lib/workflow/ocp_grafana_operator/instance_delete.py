from lib import filter_helper
from lib import output_helper
from lib.workflow.ocp_grafana_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'instance' not in params:
        return None, 'instance name required'

    if not isinstance(params['instance'], str):
        return None, 'instance param must be string'
        
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
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def delete_cluster_role_binding(params, my_output):
    my_output.default('Cluster Role Binding', underline=True, before_newline=True)

    object_filter = ['role:cluster-monitoring-view']
    crbs = params['k8s_handler'].get_cluster_role_bindings(object_filter=object_filter, cache_enabled=False)
    if crbs is None:
        my_output.error('Unexpected exception in cluster role binding api call')
        return None

    found = False
    sa_name = '%s-sa' % (params['instance'])
    crb_name = None
    subjects_count = 0
    for crb in crbs:
        for crb_subject in crb['subject']:
            if crb_subject['kind'] != 'ServiceAccount':
                continue

            if crb_subject['namespace'] != params['namespace']:
                continue

            if crb_subject['name'] != sa_name:
                continue

            crb_name = crb['name']
            subjects_count = len(crb['subject'])
            found = True

    if not found:
        my_output.default('Service Account [%s] not associated with role [cluster-monitoring-view]' % (sa_name))
        return True

    my_output.default(
        'Service Account [%s] associated with role [cluster-monitoring-view] in ClusterRoleBinding CR [%s]' % (
            sa_name,
            crb_name
        )
    )
    if subjects_count == 1:
        my_output.default('Delete ClusterRoleBinding CR [%s]' % (crb_name))
        success = params['k8s_handler'].delete_cluster_role_binding_mo(crb_name)
        if not success:
            my_output.error('REST API failed')
            return False
    
    if subjects_count > 1:
        my_output.error('Unsupported scenario - delete CRB manually and re-run the workflow')
        return False
    
    return True


def delete_data_source(params, my_output):
    my_output.default('Grafana Data Source', underline=True, before_newline=True)

    datasources = params['k8s_handler'].get_grafana_datasources(return_mo=True, cache_enabled=False)
    if datasources is None:
        my_output.error('Unexpected exception in grafana datasource api call')
        return False

    for datasource in datasources:
        datasource_dashboard = filter_helper.get(datasource, 'spec:instanceSelector:matchLabels:dashboards')
        if datasource_dashboard is None:
            continue

        if datasource_dashboard != params['instance']:
            continue

        datasource_type = filter_helper.get(datasource, 'spec:datasource:type')
        if datasource_type is None:
            continue

        if datasource_type != 'prometheus':
            continue

        my_output.default('- delete %s' % (datasource['metadata']['name']))
        success = params['k8s_handler'].delete_grafana_datasource(
            datasource['metadata']['namespace'],
            datasource['metadata']['name'],
            wait=True
        )
        if not success:
            my_output.error('REST API failed')
            return False
        
    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Grafana Operator - Delete instance', before_newline=True, after_newline=True, double_underline=True)

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
    if not params['k8s_handler'].is_grafana(instance_namespace, instance_name, cache_enabled=False):
        my_output.default('Grafana instance [%s/%s] not defined' % (instance_namespace, instance_name))
        return True
    
    if not delete_data_source(params, my_output):
        return False
    
    if not delete_cluster_role_binding(params, my_output):
        return False
    
    success = params['k8s_handler'].delete_grafana(
        params['namespace'], 
        params['instance'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks', underline=True, before_newline=True)
    my_output.default('- Grafana instance deleted')
    
    return True
