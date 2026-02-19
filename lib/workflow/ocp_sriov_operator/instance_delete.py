import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow.ocp_sriov_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'

    new_params = {}
    allowed_keys = [
        'cluster',
        'check-verbose'
    ]
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - SRIOV Operator - Delete Instance', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not params['k8s_handler'].is_sriov_subscription(params['namespace'], params['name'], cache_enabled=False):
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
