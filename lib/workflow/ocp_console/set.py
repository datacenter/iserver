import os
from lib import output_helper
from lib import file_helper
from lib.openshift import helper
from lib.workflow import ocp_common
from lib.workflow.ocp_console import common as local_common


def validate(params):
    rules = [
        ['token', True, None, 'str', None, None, None, None],
        ['secret', True, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Configure access')

    openshift_directory = helper.get_settings_directory(
        my_output=my_output,
        log_id=log_id
    )
    if openshift_directory is None:
        return False
    
    if params['token'] is not None:
        if os.path.isfile(params['token']):
            content = file_helper.get_file_text(params['token'])
            if content is None:
                my_output.error('Failed to read token file content: %s' % (params['token']))
                return False
        else:
            content = params['token']

        token_filename = os.path.join(openshift_directory, 'token')
        if not file_helper.set_file(token_filename, content.strip()):
            my_output.error('Failed to save token: %s' % (token_filename))
            return False
        
        my_output.default('Token saved: %s' % (token_filename))

    if params['secret'] is not None:
        content = file_helper.get_file_text(params['secret'])
        if content is None:
            my_output.error('Failed to read pull secret content: %s' % (params['secret']))
            return False
        
        secret_filename = os.path.join(openshift_directory, 'pull_secret.txt')
        if not file_helper.set_file(secret_filename, content.strip()):
            my_output.error('Failed to save pull secret: %s' % (secret_filename))
            return False
        
        my_output.default('Pull secret saved: %s' % (secret_filename))

    success = helper.check_openshift_authentication(
        my_output=my_output,
        log_id=log_id
    ) 

    return success