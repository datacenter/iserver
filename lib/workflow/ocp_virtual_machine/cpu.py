from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_virtual_machine import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'namespace' not in params:
        params['namespace'] = None

    if 'name' not in params:
        params['name'] = None

    if 'sockets' not in params:
        return None, 'Sockets count required'
    
    if not isinstance(params['sockets'], int):
        return None, 'sockets param must be int'

    if params['sockets'] < 1 or params['sockets'] > 32:
        return None, 'sockets param must be <1, 32> integer'

    if 'cores' not in params:
        return None, 'Cores count required'
    
    if not isinstance(params['cores'], int):
        return None, 'cores param must be int'

    if params['cores'] < 1 or params['cores'] > 32:
        return None, 'cores param must be <1, 32> integer'

    if 'threads' not in params:
        return None, 'Threads count required'
    
    if not isinstance(params['threads'], int):
        return None, 'threads param must be int'

    if params['threads'] < 1 or params['threads'] > 32:
        return None, 'threads param must be <1, 32> integer'
        
    if 'restart' not in params:
        params['restart'] = False

    if not isinstance(params['restart'], bool):
        return None, 'restart param must be true or false'

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
        'sockets',
        'cores',
        'threads',
        'restart',
        'confirmation',
        'wait',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Virtual Machine - CPU Topology Configuration', before_newline=True, after_newline=True, double_underline=True)

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
        vm_success = params['k8s_handler'].change_virtual_machine_cpu(
            virtual_machine['namespace'],
            virtual_machine['name'],
            params['sockets'],
            params['cores'],
            params['threads'],
            confirmation=False,
            wait=params['wait'],
            restart=params['restart'],
            my_output=my_output
        )
        success = success and vm_success

        if vm_success:
            info = params['k8s_handler'].get_virtual_machine(
                virtual_machine['namespace'],
                virtual_machine['name']
            )
            k8s_output_handler.print_virtual_machines([info])
            
    return success
