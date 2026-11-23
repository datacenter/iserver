from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_virtual_machine import common as local_common
from lib.workflow.k8s import pvc_delete
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

    ocp_common.print_title(params, my_output, 'Delete')
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
            vm_success = params['k8s_handler'].delete_virtual_machine(
                virtual_machine['namespace'],
                virtual_machine['name'],
                confirmation=False,
                wait=params['wait'],
                my_output=my_output
            )
            success = success and vm_success

            if not vm_success:
                continue

            for volume in virtual_machine['volume']:
                if volume['pvc'] is None:
                    continue

                pvc_delete_params = {}
                pvc_delete_params['cluster'] = params['cluster']
                pvc_delete_params['namespace'] = virtual_machine['namespace']
                pvc_delete_params['name'] = volume['pvc']
                pvc_delete_success = pvc_delete.run(
                    pvc_delete_params,
                    log_id=log_id
                )
                success = success and pvc_delete_success

    return success
