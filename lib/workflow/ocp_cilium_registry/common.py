import os
import json
import requests
from lib.workflow.ocp_cilium_registry import helper as registry_helper
from lib import file_helper
from lib import ip_helper
from lib import settings_helper


def get_default_params():
    params = {}
    params['title'] = 'OpenShift Workflow'
    return params


def get_cilium_settings_directory(my_output=None, log_id=None):
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
    
    cilium_directory = os.path.join(directory, 'cilium')
    return cilium_directory


def create_cilium_settings_directory(my_output=None, log_id=None):
    cilium_directory = get_cilium_settings_directory(my_output=my_output, log_id=log_id)
    if cilium_directory is None:
        return None
    
    if not os.path.isdir(cilium_directory):
        if my_output is not None:
            my_output.default('Cilium settings directory will be created: %s' % (cilium_directory))
        os.makedirs(cilium_directory, exist_ok=True)
        return cilium_directory

    if my_output is not None:
        my_output.default('Cilium settings directory: %s' % (cilium_directory))

    return cilium_directory


def create_access_token(registry, identity_token, description='iserver-test-token', my_output=None):
    headers = {}
    headers['Authorization'] = 'Bearer %s' % (identity_token)
    headers['Content-Type'] = 'application/json'

    body = {}
    body['description'] = description
    body['token_id'] = description
    body['token_type'] = 'access_token'

    url = 'https://%s/access/api/v1/tokens' % (registry)

    try:
        response = requests.post(
            url,
            data=json.dumps(
                body
            ),
            headers=headers,
            verify=False
        )
    except BaseException:
        if my_output is not None:
            my_output.error('REST POST request exception: %s' % (url))
        return None

    if response.status_code >= 300:
        if my_output is not None:
            my_output.error('REST POST request failed: %s' % (response.content.decode('utf-8')))
        return None

    try:
        response_body = response.json()
    except BaseException:
        if my_output is not None:
            my_output.error('REST POST response json parse failed')
        return None

    if my_output is not None:
        my_output.default('Access token created')
        my_output.default(json.dumps(response_body, indent=4), wrap='~~~')

    return response_body


def revoke_access_token(registry, identity_token, access_token_id, my_output=None):
    headers = {}
    headers['Authorization'] = 'Bearer %s' % (identity_token)
    headers['Content-Type'] = 'application/json'

    url = 'https://%s/access/api/v1/tokens/%s' % (registry, access_token_id)

    try:
        response = requests.delete(
            url,
            headers=headers,
            verify=False
        )
    except BaseException:
        if my_output is not None:
            my_output.error('REST DELETE request exception: %s' % (url))
        return False

    if response.status_code >= 300:
        if my_output is not None:
            my_output.error('REST DELETE request failed: %s' % (response.content.decode('utf-8')))
        return False

    if my_output is not None:
        my_output.default('Access token deleted: %s' % (access_token_id))

    return True


def check_identity_token(registry, identity_token, my_output=None):
    if my_output is not None:
        my_output.default('Registry: %s' % registry)
        my_output.default('Identity token: %s' % identity_token)

    access_token = create_access_token(
        registry,
        identity_token,
        my_output=my_output
    )
    if access_token is None:
        return False

    if not revoke_access_token(registry, identity_token, access_token['token_id'], my_output=my_output):
        return False

    if my_output is not None:
        my_output.default('Registry authentication and access token manipulation successfully verified')

    return True


def get_registry_settings(my_output=None, log_id=None):
    if os.environ.get('IEP_REGISTRY') is not None and os.environ.get('IEP_TOKEN') is not None:
        registry_settings = {}
        registry_settings['registry'] = os.environ.get('IEP_REGISTRY')
        registry_settings['identity_token'] = os.environ.get('IEP_TOKEN')
        return registry_settings
    
    cilium_directory = get_cilium_settings_directory(my_output=my_output, log_id=log_id)
    if cilium_directory is None:
        return None

    registry_settings = file_helper.get_file_json(
        os.path.join(cilium_directory, 'registry')
    )

    parsed = ip_helper.get_url_parse('https://%s' % (registry_settings['registry']))
    if parsed is None:
        if my_output is not None:
            my_output.error('Invalid hostname: %s' % (registry_settings['registry']))
        return None

    registry_settings['registry'] = parsed['hostname']
    return registry_settings


def set_identity_token(registry, identity_token, my_output=None, log_id=None):
    cilium_directory = create_cilium_settings_directory(my_output=my_output, log_id=log_id)
    if cilium_directory is None:
        return False

    body = {}
    body['registry'] = registry
    body['identity_token'] = identity_token

    success = file_helper.set_file_json(
        os.path.join(cilium_directory, 'registry'),
        body
    )
    if not success:
        if my_output is not None:
            my_output.error('Failed to save registry settings')
        return False

    if my_output is not None:
        my_output.default('Isovalent registry settings saved')

    return True


def check_registry_access(my_output=None, log_id=None):
    registry_settings = get_registry_settings(my_output=my_output, log_id=log_id)
    if registry_settings is None:
        if my_output is not None:
            my_output.error('Isovalent registry settings not defined')
        return False
    
    success = check_identity_token(
        registry_settings['registry'], 
        registry_settings['identity_token'],
        my_output=my_output
    )
    if not success:
        return False

    return True 


def download_manifests(version, my_output=None, log_id=None):
    registry_settings = get_registry_settings(my_output=my_output, log_id=log_id)
    if registry_settings is None:
        if my_output is not None:
            my_output.error('Isovalent registry settings not defined')
        return None, None
    
    success = check_identity_token(
        registry_settings['registry'], 
        registry_settings['identity_token'],
        my_output=my_output
    )
    if not success:
        return None, None

    access_token = create_access_token(
        registry_settings['registry'], 
        registry_settings['identity_token'],
        my_output=my_output
    )
    if access_token is None:
        return None, None

    url = registry_helper.fixup_clife_url(registry_settings['registry'], version)
    filename = ip_helper.download_url(
        url = url,
        filename = '/tmp/clife-%s.tar.gz' % (ip_helper.get_short_uuid()),
        verify=True,
        username=access_token['username'], 
        password=access_token['access_token']
    )
    if filename is None:
        if my_output is not None:
            my_output.error('Download url failed: %s' % (url))
        
    if not revoke_access_token(registry_settings['registry'], registry_settings['identity_token'], access_token['token_id'], my_output=my_output):
        return None, None

    return url, filename