from lib import output_helper
from lib.workflow.ocp_nmstate_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

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
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - NMState Operator - Delete Operator', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    subscription = params['k8s_handler'].get_subscription_by_package(
        params['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('NMState operator already deleted')
    else:
        success = params['k8s_handler'].delete_node_network_configuration_policies(
            my_output=my_output,
            wait=True
        )
        if not success:
            return False
        
        success = params['k8s_handler'].delete_nmstate(
            my_output=my_output,
            wait=True
        )

        success = params['k8s_handler'].delete_nmstate_subscription(
            subscription['namespace'],
            subscription['name'],
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False
        
    success = params['k8s_handler'].delete_operator_group(
        params['namespace'],
        params['name'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    if params['delete-namespace']:
        success = params['k8s_handler'].delete_namespace(
            params['namespace'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- NMState resources deleted')
    my_output.default('- NMState operator unconfigured and deleted')

    return True
