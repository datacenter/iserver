import os
from lib.k8s import output as k8s_output
from lib import output_helper
from lib import file_helper
from lib.workflow.ocp_vast_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    params['instance'] = None
    if 'filename' in params and params['filename'] is not None:
        try:
            print(params['filename'])
            if not os.path.isabs(params['filename']):
                params['filename'] = os.path.join(
                    params['base_directory'],
                    params['filename']
                )
        except BaseException:
            return None, 'VAST cluster file path detection failed'
        
        params['instance'] = file_helper.get_file_yaml(
            params['filename']
        )
        if params['instance'] is None:
            return None, 'Yaml file read failed: %s' % (params['filename'])
        
        if 'kind' not in params['instance']:
            return None, 'Invalid yaml file content: %s' % (params['filename'])

    if params['instance'] is None:
        if 'name' not in params or params['name'] is None:
            return None, 'Cluster name required'
        
        params['vast_cluster_name'] = params['name']

        if 'endpoint' not in params or params['endpoint'] is None:
            return None, 'endpoint required'

        if 'username' not in params or params['username'] is None:
            return None, 'username required'

        if 'password' not in params or params['password'] is None:
            return None, 'password required'

    if 'confirmation' not in params:
        params['confirmation'] = True

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'

    if 'wait' not in params:
        params['wait'] = True

    if not isinstance(params['wait'], bool):
        return None, 'wait param must be true or false'
    
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
        'name',
        'vast_cluster_name',
        'endpoint',
        'username',
        'password',
        'instance',
        'filename',
        'base_directory',
        'confirmation',
        'wait',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys, allow_kwargs=True), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - VAST CSI Operator - Create Cluster', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
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
    
    success = params['k8s_handler'].create_vast_cluster(
        params['namespace'],
        params['vast_cluster_name'],
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
        params['namespace'],
        params['vast_cluster_name'],
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
