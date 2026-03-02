from lib import output_helper
from lib.workflow.ocp_vast_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'channel' not in params:
        params['channel'] = '__default__'

    if 'confirmation' not in params:
        params['confirmation'] = True

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'

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
        'channel',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - VAST CSI Operator - Create Operator', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
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
            my_output.default('- VAST CSI already %s and %s' % (
                my_output.add_color('installed', 'Green'),
                my_output.add_color('ready', 'Green')
            ))
        else:
            my_output.default('')
            my_output.default('Completed tasks')
            my_output.default('- VAST CSI already %s and %s' % (
                my_output.add_color('installed', 'Green'),
                my_output.add_color('not ready', 'Red')
            ))

        return True

    success = params['k8s_handler'].create_namespace(
        params['namespace'],
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].create_operator_group(
        params['namespace'], 
        name=params['operator-group-name'], 
        add_target_namespaces=True, 
        target_namespaces=[params['namespace']], 
        upgrade_strategy=None, 
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].create_vast_subscription(
        params['namespace'], 
        params['name'], 
        channel=params['channel'],
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True            
    )
    if not success:
        return False
     
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- VAST CSI operator installed')

    return True
