import time
from lib import output_helper
from lib.workflow.k8s import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['__id__', True, None, None, None, None, None, None],
        ['namespace', False, None, 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
        ['stop-on-delete', False, True, 'bool', None, None, None, None],
        ['sleep-on-delete', False, None, 'int', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules, extras=['__type__'])
    if not success:
        return None, params

    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('Kubernetes Workflow - Virtual Machine - Delete', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if params['sleep-on-delete'] is not None:
        is_vm = params['k8s_handler'].is_virtual_machine(
            params['namespace'], 
            params['name'], 
            cache_enabled=False
        )

    if params['stop-on-delete']:
        success = params['k8s_handler'].stop_virtual_machine(
            params['namespace'], 
            params['name'], 
            confirmation=params['confirmation'],
            my_output=my_output, 
            wait=True,
            error_on_none=False
        )
        if not success:
            return False

    success = params['k8s_handler'].delete_virtual_machine(
        params['namespace'], 
        params['name'], 
        confirmation=params['confirmation'],
        my_output=my_output, 
        wait=True        
    )
    if not success:
        return False

    if params['sleep-on-delete'] is not None and is_vm:
        my_output.default('Sleep on delete for %s seconds' % (params['sleep-on-delete']), before_newline=True)
        time.sleep(
            params['sleep-on-delete']
        )
        
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- virtual machine deleted')
    return True
