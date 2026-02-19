import os
import base64
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_cilium_mesh import common as local_common
from lib.workflow.ocp_cilium_cni import common as cilium_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'mesh-id' not in params:
        return None, 'mesh-id required'

    if not isinstance(params['mesh-id'], int):
        return None, 'mesh-id param must be int'

    if  params['mesh-id'] < 1 or params['mesh-id'] > 255:
        return None, 'mesh-id param must be int in [1, 255] range'
    
    if 'mesh-name' not in params or params['mesh-name'] is None:
        return None, 'mesh-name required'

    if not isinstance(params['mesh-name'], str):
        return None, 'mesh-name param must be str'

    if 'mesh-port' not in params:
        return None, 'mesh-port required'

    if params['mesh-port'] is not None and not isinstance(params['mesh-port'], int):
        return None, 'mesh-port param must be int'

    if  params['mesh-port'] < 1 or params['mesh-port'] > 65535:
        return None, 'mesh-port param must be int in [1, 65535] range'
    
    if 'ca-crt' not in params or params['ca-crt'] is None:
        return None, 'Root ca certificate file required'
    
    try:
        if not os.path.isabs(params['ca-crt']):
            params['ca-crt'] = os.path.join(
                params['base_directory'],
                params['ca-crt']
            )
    except BaseException:
        return None, 'Root ca certificate file path detection failed'
    
    content = file_helper.get_file(params['ca-crt'])
    if content is None:
        return None, 'Root ca certificate file read failed: %s' % (params['ca-crt'])
    
    params['root-ca-crt'] = base64.b64encode(content.encode('utf-8')).decode('utf-8')

    if 'ca-key' not in params or params['ca-key'] is None:
        return None, 'Root ca private key file required'
    
    try:
        if not os.path.isabs(params['ca-key']):
            params['ca-key'] = os.path.join(
                params['base_directory'],
                params['ca-key']
            )
    except BaseException:
        return None, 'Root ca private key file path detection failed'
    
    content = file_helper.get_file(params['ca-key'])
    if content is None:
        return None, 'Root ca private key file read failed: %s' % (params['ca-key'])
    
    params['root-ca-key'] = base64.b64encode(content.encode('utf-8')).decode('utf-8')

    if 'confirmation' not in params:
        params['confirmation'] = True

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
        'mesh-id',
        'mesh-name',
        'mesh-port',
        'ca-crt',
        'ca-key',
        'root-ca-crt',
        'root-ca-key',
        'verbose',
        'confirmation',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def prepare_secret(params, my_output):
    my_output.default('Root CA Cert', before_newline=True, underline=True)

    secret_namespace = params['namespace']
    secret_name = params['secret']

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
        params['namespace'], 
        params['secret'], 
        params['secret'], 
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].create_certificate(
        params['namespace'],  
        params['certificate'], 
        params['secret'], 
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].create_issuer(
        params['namespace'], 
        params['namespace'], 
        params['certificate'], 
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Enable Cluster Mesh', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not cilium_common.is_cilium(params, my_output):
        return False

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
