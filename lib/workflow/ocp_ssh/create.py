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
    
    params['key'] = []

    if 'filename' not in params or len(params['filename']) == 0:
        return None, 'Ssh filename missing'
    
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
        keys = file_helper.get_files_text(item)
        if keys is not None:
            for key in keys:
                params['key'].append(
                    keys[key].split('\n')[0].replace('\r', '')
                )

    if 'wait' not in params:
        params['wait'] = True

    if not isinstance(params['wait'], bool):
        return None, 'wait param must be true or false'

    if 'confirmation' not in params:
        params['confirmation'] = False

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'role',
        'key',
        'confirmation',
        'wait',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Add SSH public key', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    success = params['k8s_handler'].add_machine_config_ssh(
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
    my_output.default('- SSH keys added')

    return True
