import json
from lib import ip_helper
from lib import output_helper
from lib.workflow.ocp_tetragon_operator import common as local_common
from lib.workflow.ocp_cilium_registry import common as registry_common
from lib.workflow.ocp_cilium_registry import helper as registry_helper
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['version', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def get_labels():
    labels = {}
    labels['openshift.io/user-monitoring'] = 'true'
    return labels


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Create Operator')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    if params['k8s_handler'].is_tetragon_subscription(params['__default__']['namespace'], params['__default__']['name']):
        my_output.default('Tetragon Operator already created')
        return True

    if params['k8s_handler'].is_namespace(params['__default__']['namespace']):
        my_output.default('Namespace %s %s' % (
            params['__default__']['namespace'],
            my_output.add_color('already created', 'Green')
        ))
    else:
        success = params['k8s_handler'].create_namespace(
            params['__default__']['namespace'],
            labels=get_labels(),
            confirmation=params['confirmation'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

    if params['k8s_handler'].is_catalog_source(params['__default__']['catalog-namespace'], params['__default__']['catalog-name'], cache_enabled=False):
        my_output.default('CatalogSource %s/%s %s' % (
            params['__default__']['catalog-namespace'],
            params['__default__']['catalog-name'],
            my_output.add_color('already created', 'Green')
        ))
    else:
        registry_settings = registry_common.get_registry_settings(my_output=my_output, log_id=log_id)
        if registry_settings is None:
            if my_output is not None:
                my_output.error('Isovalent registry settings not defined')
            return False

        access_token = registry_common.create_access_token(
            registry_settings['registry'],
            registry_settings['identity_token'],
            my_output=my_output
        )
        if access_token is None:
            return False

        data = {}
        data['auths'] = {}
        data['auths'][registry_settings['registry']] = {}
        data['auths'][registry_settings['registry']]['username'] = access_token['username']
        data['auths'][registry_settings['registry']]['password'] = access_token['access_token']
        data['auths'][registry_settings['registry']]['auth'] = ip_helper.encode_text_64(
            '%s:%s' % (
                access_token['username'],
                access_token['access_token']
            )
        )
        my_output.default('CatalogSource secret data')
        my_output.default(json.dumps(data, indent=4), wrap='~~~')
        
        success = params['k8s_handler'].create_secret_docker(
            params['__default__']['namespace'], 
            params['__default__']['secret-name'],
            json.dumps(data),
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

        success = params['k8s_handler'].create_catalog_source(
            params['__default__']['catalog-namespace'],
            params['__default__']['catalog-name'],
            registry_helper.fixup_tetragon_url(registry_settings['registry']),
            secrets=[params['__default__']['secret-name']],
            confirmation=params['confirmation'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

    my_output.default('Wait for tetragon package...')
    if not params['k8s_handler'].wait_tetragon_package():
        my_output.error('Tetragon package not found')
        return False
    
    my_output.default('Tetragon package %s' % (my_output.add_color('found', 'Green')))

    success = params['k8s_handler'].create_operator_group(
        params['__default__']['namespace'], 
        name=params['__default__']['operator-group-name'], 
        add_target_namespaces=False,
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].create_tetragon_subscription(
        params['__default__']['namespace'], 
        params['__default__']['name'], 
        params['__default__']['catalog-namespace'], 
        params['__default__']['catalog-name'], 
        None,
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True            
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Namespace created')
    my_output.default('- Operator Group created')
    my_output.default('- Tetragon Operator installed')
    return True