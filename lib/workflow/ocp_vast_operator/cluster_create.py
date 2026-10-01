from lib.k8s import output as k8s_output
from lib import output_helper
from lib import filter_helper
from lib.workflow.ocp_vast_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['filename', True, None, 'file-k8s', None, None, 'VastCluster', None],
        ['name', True, None, 'str', None, None, None, None],
        ['endpoint', True, None, 'str', None, None, None, None],
        ['username', True, None, 'str', None, None, None, None],
        ['password', True, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules, allow_kwargs=True)
    if not success:
        return None, params

    success, error = ocp_common.check_param_options(params, ['filename'], ['name', 'endpoint', 'username', 'password'])
    if not success:
        return None, error
            
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Create Cluster')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    state = local_common.check_state(
        params, 
        my_output,
        check_ready=True
    )
    if not state['installed']:
        my_output.error('VAST operator not installed')
        return False

    if not state['ready']:
        my_output.error('VAST operator not ready')
        return False
    
    if params['filename'] is not None:
        body = ocp_common.get_k8s_body(params['filename'], 'VastCluster', my_output)
        if body is None:
            return False
        
        namespace = filter_helper.get(body, 'metadata:namespace')
        if namespace != params['__default__']['namespace']:
            my_output.error('Namespace %s expected: %s' % (
                params['__default__']['namespace'],
                namespace
            ))
            return False
        
        params['name'] = filter_helper.get(body, 'metadata:name')

        success = params['k8s_handler'].create_vast_cluster_from_body(
            body,
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=params['wait']
        )
        if not success:
            return False

    if params['filename'] is None:
        success = params['k8s_handler'].create_vast_cluster(
            params['__default__']['namespace'],
            params['name'],
            params['endpoint'], 
            params['username'],
            params['password'],
            extras=params['kwargs'],
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=params['wait']
        )
        if not success:
            return False
    
    info = params['k8s_handler'].get_vast_cluster(
        params['__default__']['namespace'],
        params['name'],
        storage_info=True,
        cache_enabled=False
    )
    if info is None:
        my_output.error('Exception: no object found')
        return False
    
    k8s_output_handler.print_vast_clusters_state([info])

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- VAST cluster created')

    return True