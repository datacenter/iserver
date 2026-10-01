from lib import output_helper
from lib.workflow.k8s import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['__id__', True, None, None, None, None, None, None],
        ['name', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules, extras=['__type__'])
    if not success:
        return None, params

    return ocp_common.sanitize_params(params, allowed_keys, add_defaults=False, copy_handler=False), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'OVN Cluster User Defined Network - Delete')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    success = params['k8s_handler'].delete_cluster_user_defined_network(
        params['name'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- ovn cluster user defined network deleted')
    return True
