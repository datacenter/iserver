from lib import output_helper
from lib.workflow.ocp_tetragon_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'channel' not in params:
        params['channel'] = '__default__'

    if 'image' not in params:
        params['image'] = None

    if params['image'] is None:
        return None, 'Tetragon image source required'

    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'

    allowed_keys = [
        'cluster',
        'channel',
        'image',
        'confirmation',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def get_labels():
    labels = {}
    labels['openshift.io/user-monitoring'] = 'true'
    return labels


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Tetragon Operator - Create Operator', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if params['k8s_handler'].is_tetragon_subscription(params['namespace'], params['name']):
        my_output.default('Tetragon Operator already created')
        return True

    success = params['k8s_handler'].create_namespace(
        params['namespace'],
        labels=get_labels(),
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].create_operator_group(
        params['namespace'], 
        name=params['operator-group-name'], 
        add_target_namespaces=False,
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].create_catalog_source(
        params['catalog-namespace'],
        params['catalog-name'],
        params['image'],
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True,
        hide_image=True
    )
    if not success:
        return False

    my_output.default('Wait for tetragon package...')
    if not params['k8s_handler'].wait_tetragon_package():
        my_output.error('Tetragon package not found')
        return False
    
    success = params['k8s_handler'].create_tetragon_subscription(
        params['namespace'], 
        params['name'], 
        params['catalog-namespace'], 
        params['catalog-name'], 
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
