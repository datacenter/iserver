from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_splunk_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['instance', False, None, 'str', None, None, None, None],
        ['route', True, True, 'bool', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Create Instance')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    if not params['k8s_handler'].is_splunk_subscription(params['__default__']['namespace'], params['__default__']['name']):
        my_output.error('Splunk operator must be installed first')
        return False

    if not params['k8s_handler'].is_default_storage_class(cache_enabled=False):
        my_output.error('Default storage class not found')
        return False
    
    if params['k8s_handler'].is_splunk_standalone(params['__default__']['namespace'], params['instance']):
        my_output.default('Splunk standalone instance %s already exists' % (params['instance']))
    else:
        success = params['k8s_handler'].create_splunk_standalone(
            params['__default__']['namespace'], 
            params['instance'], 
            pvc_finalizers=params['__default__']['pvc-finalizers'],
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False
    
    if not params['route']:
        success = params['k8s_handler'].delete_splunk_standalone_route(
            params['__default__']['namespace'], 
            params['instance'], 
            confirmation=params['confirmation'], 
            my_output=my_output
        )
        if not success:
            return False

    if params['route']:
        success = params['k8s_handler'].create_splunk_standalone_route(
            params['__default__']['namespace'], 
            params['instance'], 
            confirmation=params['confirmation'], 
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

    object_filter=[]
    object_filter.append('namespace:%s' % (params['__default__']['namespace']))
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
        k8s_output_handler.print_splunk_standalones_state(standalones)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Standalone instance created')
    my_output.default('- Route configured')
    return True