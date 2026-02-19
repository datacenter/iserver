import os
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_ssh import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'role' not in params:
        params['role'] = 'any'

    if params['role'] not in ['any', 'master', 'worker']:
        return None, 'Role parameter must be one of any, master, worker'
        
    keys = []

    if 'key' not in params:
        params['key'] = []

    for key in params['key']:
        keys.append(key)

    if 'filename' not in params:
        params['filename'] = []
    
    locations = []
    for item in params['filename']:
        try:
            if not os.path.isabs(item):
                item = os.path.join(
                    params['base_directory'],
                    item
                )
        except BaseException:
            return None, 'SSH public key file path detection failed'
        
        locations.append(item)

    for item in locations:
        file_keys = file_helper.get_files_text(item)
        if file_keys is not None:
            for file_key in file_keys:
                keys.append(
                    file_keys[file_key].split('\n')[0].replace('\r', '').split(' ')[1]
                )

    params['key'] = keys
    if len(params['key']) == 0:
        return None, 'Define keys'

    if 'wait' not in params:
        params['wait'] = True

    if not isinstance(params['wait'], bool):
        return None, 'wait param must be true or false'

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'role',
        'key',
        'wait',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Delete SSH public key', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
    success = params['k8s_handler'].delete_machine_config_ssh(
        params['key'], 
        params['role'], 
        my_output=my_output, 
        wait=True
    )

    if not success:
        my_output.error('Workflow failed')
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- SSH keys deleted')

    return True
