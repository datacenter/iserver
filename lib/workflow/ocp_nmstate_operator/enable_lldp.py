from lib import output_helper
from lib.workflow.ocp_nmstate_operator import lldp as workflow_lldp
from lib.workflow.ocp_nmstate_operator import common as local_common
from lib.workflow import ocp_common
from lib.workflow import netshoot_helper


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['enable', True, True, 'bool', None, None, None, None],
        ['fw', True, False, 'bool', None, None, None, None],
        ['node', True, None, 'str', None, None, None, None],
        ['include-down', True, False, 'bool', None, None, None, None],
        ['delete-nncp', True, False, 'bool', None, None, None, None]
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

    ocp_common.print_title(params, my_output, 'Enable LLDP')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    success = params['k8s_handler'].is_subscription_nmstate_ready(with_instance=True, my_output=my_output, details=True)
    if not success:
        my_output.error('NMState not ready')
        return False

    params = netshoot_helper.create_netshoots(params, my_output=my_output)
    if params is None:
        return False

    params['interfaces'], error = workflow_lldp.get_interfaces(
        params,
        my_output,
        node_name_filter=params['node']
    )
    if params['interfaces'] is None:
        my_output.error(error)
        return False

    if params['fw']:
        workflow_lldp.configure_nic(
            params,
            my_output
        )

    if params['enable']:
        params = workflow_lldp.enable_nns(
            params,
            my_output,
            log_id=log_id
        )
        if not params['success']:
            my_output.error(params['error'])
            return False

    success = netshoot_helper.delete_netshoots(params, my_output=my_output)
    if not success:
        pass

    my_output.default('')
    my_output.default('Completed tasks')
    if params['fw']:
        my_output.default('- LLDP disabled on fw nic level')
    if params['enable']:
        my_output.default('- LLDP enabled on nmstate level')
    my_output.default('- LLDP enabled')

    return True