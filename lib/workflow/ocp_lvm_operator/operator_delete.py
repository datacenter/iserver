from lib import output_helper
from lib.workflow.ocp_lvm_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def check_resources(params, my_output):
    if params['k8s_handler'].get_lvm_cluster(cache_enabled=False) is not None:
        my_output.error('Delete LVM cluster first')
        return False
    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Delete Operator')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    if params['k8s_handler'].get_lvm_cluster(cache_enabled=False) is not None:
        my_output.error('Delete LVM cluster first')
        return False
        
    success = ocp_common.delete_operator(
        params,
        my_output
    )
    if not success:
        return False
    
    return True