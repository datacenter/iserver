import os
from lib import settings_helper
from lib.openshift import api
from lib.openshift import settings


def get_settings_directory(my_output=None, log_id=None):
    settings_handler = settings_helper.Settings(log_id=log_id)
    directory = settings_handler.get_settings_dir()
    if directory is None:
        if my_output is not None:
            my_output.error('Unexpected failure in getting .itool settings directory')
        return None
    
    if not os.path.isdir(directory):
        if my_output is not None:
            my_output.error('Unexpected no .itool settings directory: %s' % (directory))
        return None
    
    openshift_directory = os.path.join(directory, 'openshift')
    if not os.path.isdir(openshift_directory):
        if my_output is not None:
            my_output.default('Openshift settings directory will be created: %s' % (openshift_directory))
        os.makedirs(openshift_directory, exist_ok=True)

    return openshift_directory


def get_token():
    settings_handler = settings.OpenShiftSettings()
    return settings_handler.get_api_token()


def check_openshift_authentication(my_output=None, log_id=None):
    token = get_token()
    if token is None:
        if my_output is not None:
            my_output.error('OpenShift Console token not defined')
        return False
    
    api_handler = api.Api(token, log_id=log_id)
    access_token = api_handler.get_access_token()
    if access_token is None:
        if my_output is not None:
            my_output.error('OpenShift Console authentication with token failed')
        return False

    if my_output is not None:
        my_output.default('OpenShift Console authentication successful')

    return True