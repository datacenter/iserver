import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow.ocp_local_storage_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['channel', True, 'stable', 'str', None, None, None, None],
        ['node-selector-override', True, False, 'bool', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def get_namespace_annotations(params):
    annotations = {}

    if params['k8s_handler'].get_node_count() == 1:
        annotations['workload.openshift.io/allowed'] = 'management'

    if params['node-selector-override']:
        annotations['openshift.io/node-selector'] = ''

    return annotations


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
    
    state = local_common.check_state(
        params, 
        my_output,
        check_ready=True
    )
    if state['installed']:
        if state['ready']:
            my_output.default('')
            my_output.default('Completed tasks')
            my_output.default('- Local Storage Operator already %s and %s' % (
                my_output.add_color('installed', 'Green'),
                my_output.add_color('ready', 'Green')
            ))
        else:
            my_output.default('')
            my_output.default('Completed tasks')
            my_output.default('- Local Storage Operator already %s and %s' % (
                my_output.add_color('installed', 'Green'),
                my_output.add_color('not ready', 'Red')
            ))

        return True
    
    success = params['k8s_handler'].create_namespace(
        params['__default__']['namespace'],
        annotations=get_namespace_annotations(params),
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].create_operator_group(
        params['__default__']['namespace'], 
        name=params['__default__']['operator-group-name'], 
        add_target_namespaces=True, 
        target_namespaces=[params['__default__']['namespace']], 
        upgrade_strategy=None, 
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].create_local_storage_subscription(
        params['__default__']['namespace'], 
        params['__default__']['name'], 
        channel=params['channel'],
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
    my_output.default('- Local Storage Operator installed')

    return True