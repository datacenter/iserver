from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_virtual_machine import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['namespace', True, None, 'str', None, None, None, None],
        ['name', True, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Stop')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    ret, virtual_machines = local_common.select_virtual_machines(
        params,
        my_output,
        k8s_output_handler
    )
    if virtual_machines is None:
        return ret
    
    success = True
    for virtual_machine in virtual_machines:
        vm_success = params['k8s_handler'].stop_virtual_machine(
            virtual_machine['namespace'],
            virtual_machine['name'],
            confirmation=False,
            wait=params['wait'],
            my_output=my_output
        )
        success = success and vm_success

        if vm_success:
            info = params['k8s_handler'].get_virtual_machine(
                virtual_machine['namespace'],
                virtual_machine['name']
            )
            k8s_output_handler.print_virtual_machines_state([info])
            
    return success
