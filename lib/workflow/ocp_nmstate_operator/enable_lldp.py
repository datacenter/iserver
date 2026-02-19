from lib import output_helper
from lib.workflow.ocp_nmstate_operator import lldp as workflow_lldp
from lib.workflow.ocp_nmstate_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'settings' not in params:
        params['settings'] = {}
        params['settings']['nic-fw-disable'] = False
        params['settings']['enable'] = False
        params['settings']['node'] = None
        params['settings']['include-down'] = True
        params['settings']['delete-nncp'] = True

    if 'nic-fw-disable' not in params['settings']:
        params['settings']['nic-fw-disable'] = False

    if 'enable' not in params['settings']:
        params['settings']['enable'] = False

    if 'node' not in params['settings']:
        params['settings']['node'] = None

    if 'include-down' not in params['settings']:
        params['settings']['include-down'] = True

    if 'delete-nncp' not in params['settings']:
        params['settings']['delete-nncp'] = True

    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    new_params = {}
    allowed_keys = [
        'cluster',
        'settings',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - NMState Operator - Enable LLDP', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id, ssh_required=True)
    if params is None:
        return False

    success = params['k8s_handler'].is_subscription_nmstate_ready(with_instance=True)
    if not success:
        my_output.error('NMState not ready')
        return False
    
    params['interfaces'], error = workflow_lldp.get_interfaces(
        params,
        my_output,
        log_id,
        node_name_filter=params['settings']['node']
    )
    if params['interfaces'] is None:
        my_output.error(error)
        return False

    if params['settings']['nic-fw-disable']:
        workflow_lldp.configure_nic(
            params,
            log_id=log_id
        )

    if params['settings']['enable']:
        params = workflow_lldp.enable_nns(
            params,
            log_id=log_id
        )
        if not params['success']:
            my_output.error(params['error'])
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    if params['settings']['nic-fw-disable']:
        my_output.default('- LLDP disabled on fw nic level')
    if params['settings']['enable']:
        my_output.default('- LLDP enabled on nmstate level')

    return True
