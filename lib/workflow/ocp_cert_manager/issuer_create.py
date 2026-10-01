import json
from lib import file_helper
from lib import ip_helper
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cert_manager import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['namespace', True, None, 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
        ['secret', True, None, 'str', None, None, None, None],
        ['type', True, 'local', 'str', None, None, ['local'], None]
    ]

    rules_local = [
        ['crt', False, None, 'file', None, None, None, None],
        ['key', False, None, 'file', None, None, None, None]
    ]

    conditions = []
    condition = {}
    condition['key'] = 'type'
    condition['value'] = 'local'
    condition['rules'] = rules_local
    conditions.append(condition)

    success, params, allowed_keys = ocp_common.check_parameters(params, rules, conditions=conditions)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def prepare_secret(params, my_output):
    my_output.default('Root CA Cert', before_newline=True)
    my_output.default(json.dumps(params['root-ca-crt-info'], indent=2), wrap='~~~')

    content = {}
    content['tls.crt'] = ip_helper.encode_text_64(params['root-ca-crt'])
    content['tls.key'] = params['root-ca-key']

    success = params['k8s_handler'].create_or_update_secret_kv(
        params['secret-namespace'],
        params['secret'],
        content,
        secret_type='kubernetes.io/tls',
        my_output=my_output,
        confirmation=params['confirmation'],
        wait=True
    )
    if not success:
        return False
    
    return True


def prepare_cert(params, my_output, k8s_output_handler):
    if params['namespace'] is None:
        success = params['k8s_handler'].create_cluster_issuer(
            params['name'], 
            params['secret'], 
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False
        
        issuer = params['k8s_handler'].get_cluster_issuer(params['name'], secret_info=True, cache_enabled=False, optimized=False)
        if issuer is None:
            my_output.error('Failed to find cluster issuer crd %s' % (params['name']))
            return False
        
        k8s_output_handler.print_cluster_issuers_state([issuer])

    if params['namespace'] is not None:
        success = params['k8s_handler'].create_issuer(
            params['namespace'], 
            params['name'], 
            params['secret'], 
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False
        
        issuer = params['k8s_handler'].get_issuer(params['namespace'], params['name'], secret_info=True, cache_enabled=False, optimized=False)
        if issuer is None:
            my_output.error('Failed to find issuer crd %s/%s' % (params['namespace'], params['name']))
            return False
        
        k8s_output_handler.print_issuers_state([issuer])

    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Create issuer')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    if params['type'] == 'local':
        params['secret-namespace'] = params['namespace']
        if params['secret-namespace'] is None:
            params['secret-namespace'] = params['__default__']['namespace']


        if params['secret'] is None:
            params['secret'] = params['name']

        params['root-ca-crt'] = file_helper.get_file_text(params['crt'], base_directory=params['base_directory'])
        if params['root-ca-crt'] is None:
            my_output.error('Root ca certificate file read failed: %s' % (params['crt']))
            return False

        params['root-ca-crt-info'] = ip_helper.get_cert_info(params['root-ca-crt'].encode('utf-8'))
        if params['root-ca-crt-info'] is None:
            my_output.error('File does not have valid certificate: %s' % (params['crt']))
            return False

        params['root-ca-key'] = file_helper.get_file_base64(params['key'], base_directory=params['base_directory'])
        if params['root-ca-key'] is None:
            my_output.error('Root ca private key file read failed: %s' % (params['key']))
            return False

        if not prepare_secret(params, my_output):
            return False
        
        if not prepare_cert(params, my_output, k8s_output_handler):
            return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- issuer created')
    return True
