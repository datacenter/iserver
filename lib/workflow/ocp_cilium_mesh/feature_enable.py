import os
import base64
import traceback
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_cilium_mesh import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['mesh-id', False, None, 'int', 1, 255, None, None],
        ['mesh-name', False, None, 'str', None, None, None, None],
        ['mesh-port', False, None, 'int', 1, 65535, None, None],
        ['ca-crt', False, None, 'file', None, None, None, None],
        ['ca-key', False, None, 'file', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def prepare_secret(params, my_output):
    my_output.default('Root CA Cert', before_newline=True, underline=True)

    secret_namespace = params['__default__']['namespace']
    secret_name = params['__default__']['secret']

    my_output.default('Cilium root ca secret')
    my_output.default('- namespace: %s' % (secret_namespace))
    my_output.default('- name: %s' % (secret_name))

    if params['k8s_handler'].is_secret(secret_namespace, secret_name, cache_enabled=False):
        my_output.default('- already created')
        return True
    
    my_output.default('- secret will be created based on user provided root ca crt and key')

    content = {}
    content['tls.crt'] = params['root-ca-crt']
    content['tls.key'] = params['root-ca-key']
    success = params['k8s_handler'].create_secret_kv(
        secret_namespace,
        secret_name,
        content,
        secret_type='kubernetes.io/tls',
        my_output=my_output,
        wait=True
    )
    if not success:
        return False
    
    return True


def prepare_cert(params, my_output):     
    success = params['k8s_handler'].create_issuer(
        params['__default__']['namespace'], 
        params['__default__']['secret'], 
        params['__default__']['secret'], 
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].create_certificate(
        params['__default__']['namespace'],  
        params['__default__']['certificate'], 
        params['__default__']['secret'], 
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].create_issuer(
        params['__default__']['namespace'], 
        params['__default__']['namespace'], 
        params['__default__']['certificate'], 
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Enable')
    params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
    if params is None:
        return False
    
    if params['base_directory'] is not None:
        if not os.path.isabs(params['ca-crt']):
            try:
                params['ca-crt'] = os.path.join(
                    params['base_directory'],
                    params['ca-crt']
                )
            except BaseException:
                my_output.error('Root ca certificate file path detection failed: %s' % (params['ca-crt']))
                return False
    
    content = file_helper.get_file(params['ca-crt'])
    if content is None:
        my_output.error('Root ca certificate file read failed: %s' % (params['ca-crt']))
        return False
    
    params['root-ca-crt'] = base64.b64encode(content.encode('utf-8')).decode('utf-8')

    if params['base_directory'] is not None:
        if not os.path.isabs(params['ca-key']):
            try:
                params['ca-key'] = os.path.join(
                    params['base_directory'],
                    params['ca-key']
                )
            except BaseException:
                my_output.error('Root ca private key file path detection failed: %s' % (params['ca-key']))
                return False
    
    content = file_helper.get_file(params['ca-key'])
    if content is None:
        my_output.error('Root ca private key file read failed: %s' % (params['ca-key']))
        return False
    
    params['root-ca-key'] = base64.b64encode(content.encode('utf-8')).decode('utf-8')

    cilium_config = params['k8s_handler'].get_cilium_config()
    if cilium_config is None:
        my_output.error('Failed to get cilium configuration')
        return False

    if params['k8s_handler'].is_cilium_mesh_enabled():
        my_output.default('Cluster mesh already enabled', before_newline=True)
        return True

    if not prepare_secret(params, my_output):
        return False
    
    if not prepare_cert(params, my_output):
        return False
    
    success = params['k8s_handler'].enable_cilium_mesh(
        params['mesh-id'], 
        params['mesh-name'], 
        params['mesh-port'], 
        my_output=my_output, 
        confirmation=params['confirmation']
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Root CA secret created')
    my_output.default('- Certificate manager resources created')
    my_output.default('- Cluster mesh enabled')

    return True