import os
from lib import output_helper
from lib import file_helper
from lib import settings_helper
from lib.openshift import console


def validate(params):
    if 'token' not in params:
        return None, 'Token filename required: https://console.redhat.com/openshift/token'

    if not os.path.isfile(params['token']):
        return None, 'Token file not found: %s' % (params['token'])
    
    if 'secret' not in params:
        return None, 'Secret filename required: https://console.redhat.com/openshift/install/pull-secret'

    if not os.path.isfile(params['secret']):
        return None, 'Secret file not found: %s' % (params['secret'])

    return params, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - OpenShift Console REST API - Configure access', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False
    
    settings_handler = settings_helper.Settings(log_id=log_id)
    directory = settings_handler.get_settings_dir()
    if directory is None:
        my_output.error('Unexpected failure in getting .itool settings directory')
        return False
    
    if not os.path.isdir(directory):
        my_output.error('Unexpected no .itool settings directory: %s' % (directory))
        return False
    
    openshift_directory = os.path.join(directory, 'openshift')
    if not os.path.isdir(openshift_directory):
        my_output.default('Openshift settings directory will be created: %s' % (openshift_directory))
        os.makedirs(openshift_directory, exist_ok=True)
        
    content = file_helper.get_file_text(params['token'])
    if content is None:
        my_output.error('Failed to read token content: %s' % (params['token']))
        return False
    
    token_filename = os.path.join(openshift_directory, 'token')
    if not file_helper.set_file(token_filename, content.strip()):
        my_output.error('Failed to save token: %s' % (token_filename))
        return False
    
    my_output.default('Token saved: %s' % (token_filename))

    content = file_helper.get_file_text(params['secret'])
    if content is None:
        my_output.error('Failed to read pull secret content: %s' % (params['secret']))
        return False
    
    secret_filename = os.path.join(openshift_directory, 'pull_secret.txt')
    if not file_helper.set_file(secret_filename, content.strip()):
        my_output.error('Failed to save pull secret: %s' % (secret_filename))
        return False
    
    my_output.default('Pull secret saved: %s' % (secret_filename))
    
    console_handler = console.Console(log_id=log_id)
    if console_handler.api_handler.get_access_token() is None:
        my_output.error('OpenShift console connection failed')
        return False
    else:
        my_output.default('OpenShift console connection successful')

    return True
