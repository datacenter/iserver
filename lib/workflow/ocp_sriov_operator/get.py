import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.k8s import output as k8s_output
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

    my_output.default('OpenShift Workflow - SRIOV Operator - Get Information', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.augment_params(params)

    my_output.default('Workflow Parameters', underline=True)
    my_output.default(json.dumps(params, indent=4), after_newline=True)

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['verbose'] = True
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return False
    
    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler
    
    subscription = params['k8s_handler'].get_subscription_by_package(
        params['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('Operator not found: %s' % (params['name']))
        return True
    
    my_output.default('Operator', underline=True)
    my_output.default('- subscription: %s' % (subscription['namespace_name']))
    my_output.default('- channel: %s' % (subscription['channel']))
    my_output.default('- csv: %s' % (subscription['installed_csv']))
    
    config = params['k8s_handler'].get_sriov_operator_config(cache_enabled=False)
    if config is None:
        my_output.default('SRIOV operator configuration (instance) not defined', before_newline=True)
        return True
    
    my_output.default('SRIOV operator configuration', before_newline=True, underline=True)
    my_output.default('- namespace: %s' % (config['namespace']))
    my_output.default('- name: %s' % (config['name']))
    
    my_output.default(json.dumps(config['spec'], indent=4), wrap='~~~', before_newline=True)

    return True
