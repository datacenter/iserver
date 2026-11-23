import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow.ocp_sriov_operator import common as local_common
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

    ocp_common.print_title(params, my_output, 'Delete Instance')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    if not params['k8s_handler'].is_sriov_subscription(params['__default__']['namespace'], params['__default__']['name'], cache_enabled=False):
        my_output.default('SRIOV operator not installed')
        return True
    
    my_output.default('SRIOV network operator installed')

    if not params['k8s_handler'].is_sriov_operator_config(cache_enabled=False):
        my_output.default('Sriov instance already deleted')
        return True

    my_output.default('SRIOV operator configuration defined')

    policies = params['k8s_handler'].get_sriov_network_node_policies(cache_enabled=False)
    if policies is None:
        my_output.error('Failed to get sriov network node policies')
        return False
    
    if len(policies) > 0:
        my_output.error('Delete sriov network node policies first')
        return False
    
    my_output.default('No sriov network node policy found')
    
    success = params['k8s_handler'].delete_sriov_operator_config(
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('- SRIOV Operator configuration deleted')

    return True