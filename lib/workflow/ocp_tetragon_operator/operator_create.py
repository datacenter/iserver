from lib import output_helper
from lib.workflow.ocp_tetragon_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['channel', True, '__default__', 'str', None, None, None, None],
        ['image', False, None, 'str', None, None, None, None]
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

    if not params['k8s_handler'].is_namespace(params['__default__']['namespace']):
        success = params['k8s_handler'].create_namespace(
            params['__default__']['namespace'],
            labels=get_labels(),
            confirmation=params['confirmation'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

    success = params['k8s_handler'].create_catalog_source(
        params['__default__']['catalog-namespace'],
        params['__default__']['catalog-name'],
        params['image'],
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    my_output.default('Wait for tetragon package...', before_newline=True)
    if not params['k8s_handler'].wait_tetragon_package():
        my_output.error('Tetragon package not found')
        return False
    my_output.default('Tetragon package %s' % (my_output.add_color('found', 'Green')))

    if params['k8s_handler'].is_tetragon_subscription(params['__default__']['namespace'], params['__default__']['name']):
        my_output.default('Tetragon Operator already created')
        return True

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
        params['channel'],
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