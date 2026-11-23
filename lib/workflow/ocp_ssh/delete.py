import os
from lib import file_helper
from lib import filter_helper
from lib import output_helper
from lib.workflow.ocp_ssh import common as local_common
from lib.workflow import ocp_common
from menu.common import get_confirmation


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['role', False, 'any', 'str', None, None, ['any', 'master', 'worker'], None],
        ['filename', True, [], 'list-of-str', None, None, None, None],
        ['key', True, [], 'list-of-str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Delete')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    content = file_helper.get_files_text(
        params['filename'],
        base_directory=filter_helper.get(params, 'base_directory')
    )
    if content is not None:
        for file_key in content:
            params['key'].append(
                content[file_key].split('\n')[0].replace('\r', '').split(' ')[1]
            )

    if len(params['key']) == 0:
        my_output.default('Define at least one key')
        return True

    my_output.default('SSH public keys matching rules to be deleted', before_newline=True)
    for item in params['key']:
        my_output.default('- %s' % (item))

    if params['confirmation']:
        if not get_confirmation():
            return False
        
    success = params['k8s_handler'].delete_machine_config_ssh(
        params['key'], 
        params['role'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- SSH keys deleted')
    return True