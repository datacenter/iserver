from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_splunk_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'instance' not in params or params['instance'] is None:
        return None, 'Instance name required'

    if 'route' not in params:
        params['route'] = True

    if not isinstance(params['route'], bool):
        return None, 'route param must be true or false'
    
    if 'confirmation' not in params:
        params['confirmation'] = False

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'instance',
        'route',
        'confirmation',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Splunk Operator - Create Instance', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not params['k8s_handler'].is_splunk_subscription(params['namespace'], params['name']):
        my_output.error('Splunk operator must be installed first')
        return False

    if not params['k8s_handler'].is_default_storage_class(cache_enabled=False):
        my_output.error('Default storage class not found')
        return False
    
    if params['k8s_handler'].is_splunk_standalone(params['namespace'], params['instance']):
        my_output.default('Splunk standalone instance already exists')
    else:
        success = params['k8s_handler'].create_splunk_standalone(
            params['namespace'], 
            params['instance'], 
            pvc_finalizers=params['pvc-finalizers'],
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False
    
    if not params['route']:
        success = params['k8s_handler'].delete_splunk_standalone_route(
            params['namespace'], 
            params['instance'], 
            confirmation=params['confirmation'], 
            my_output=my_output
        )
        if not success:
            return False

    if params['route']:
        success = params['k8s_handler'].create_splunk_standalone_route(
            params['namespace'], 
            params['instance'], 
            confirmation=params['confirmation'], 
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

    object_filter=[]
    object_filter.append('namespace:%s' % (params['namespace']))
    object_filter.append('name:%s' % (params['instance']))
    standalones = params['k8s_handler'].get_splunk_standalones(
        object_filter=object_filter,
        pod_info=True,
        pvc_info=True,
        service_info=True,
        route_info=True,
        secret_info=True,
        cache_enabled=False
    )
    if standalones is not None:
        k8s_output_handler.print_standalones(standalones)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Standalone instance created')
    my_output.default('- Route configured')

    return True
