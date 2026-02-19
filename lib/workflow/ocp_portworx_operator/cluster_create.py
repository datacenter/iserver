import os
from lib.k8s import output as k8s_output
from lib import output_helper
from lib import file_helper
from lib.linux import output as linux_output
from lib.workflow.ocp_portworx_operator import common as local_common


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
            return None, 'LVM cluster file path detection failed'
        
        params['instance'] = file_helper.get_file_yaml(
            params['filename']
        )
        if params['instance'] is None:
            return None, 'Yaml file read failed: %s' % (params['filename'])
        
        if 'kind' not in params['instance']:
            return None, 'Invalid yaml file content: %s' % (params['filename'])

    if 'confirmation' not in params:
        params['confirmation'] = True

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
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    linux_output_handler = linux_output.LinuxOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Portworx Operator - Create Storage Cluster', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    subscription = params['k8s_handler'].get_subscription_by_package(
        params['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.error('Portworx Operator must be created first')
        return False

    success = params['k8s_handler'].create_portworx_storage_cluster(
        body=params['instance'], 
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    cluster = params['k8s_handler'].get_portworx_storage_cluster(cache_enabled=False)
    k8s_output_handler.print_portworx_storage_cluster(cluster)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Portworx storage cluster instance created and ready')

    return True
