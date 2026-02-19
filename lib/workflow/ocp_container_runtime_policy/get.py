from lib import output_helper
from lib.workflow.ocp_container_runtime_policy import common as local_common
from lib.workflow.ocp_container_runtime_policy import output as local_output

def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose params must be true or false'
    
    allowed_keys = [
        'cluster',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Get container runtime policy', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    my_output.default('Collecting data...', before_newline=True, after_newline=True)
    info = local_common.get_ocp_container_policy_info(params['k8s_handler'], params['linux_handler'])
    local_output.print_ocp_container_policy_info(info, my_output)

    return True
