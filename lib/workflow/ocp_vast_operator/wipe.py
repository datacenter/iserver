from lib import output_helper
from lib.workflow.ocp_vast_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Wipe')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    state = local_common.check_state(
        params, 
        my_output,
        check_ready=True,
        check_resources=True
    )
    if not state['installed']:
        return True
    
    if state['storage'] is not None:
        for item in state['storage']:
            success = params['k8s_handler'].delete_vast_storage(
                item['namespace'],
                item['name'],
                my_output=my_output, 
                wait=params['wait']
            )
            if not success:
                return False
            
    if state['cluster'] is not None:
        for item in state['cluster']:
            success = params['k8s_handler'].delete_vast_cluster(
                item['namespace'],
                item['name'],
                my_output=my_output, 
                wait=params['wait']
            )
            if not success:
                return False

    if state['driver'] is not None:
        for item in state['driver']:
            success = params['k8s_handler'].delete_vast_driver(
                item['namespace'],
                item['name'],
                my_output=my_output, 
                wait=params['wait']
            )
            if not success:
                return False

    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- VAST CRDs deleted')

    return True
