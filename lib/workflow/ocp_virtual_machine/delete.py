from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_virtual_machine import common as local_common
from lib.workflow.k8s import pvc_delete


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'namespace' not in params:
        params['namespace'] = None

    if 'name' not in params:
        params['name'] = None

    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'wait' not in params:
        params['wait'] = True

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
        'namespace',
        'name',
        'confirmation',
        'wait',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Virtual Machine - Delete', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
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
