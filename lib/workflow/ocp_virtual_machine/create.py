from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_virtual_machine import common as local_common
from lib.workflow.ocp_virtual_machine import template
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['namespace', False, None, 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
        ['template', False, None, 'str', None, None, ['cirros'], None],
        ['core', True, 1, 'int', 1, 8, None, None],
        ['socket', True, 1, 'int', 1, 8, None, None],
        ['thread', True, 1, 'int', 1, 8, None, None],
        ['memory', True, 1, 'int', 1, 8, None, None],
        ['network', True, [], 'list-of-str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules, allow_kwargs=True)
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

    ocp_common.print_title(params, my_output, 'Create')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    body, metadata = template.get(params, my_output)
    if body is None:
        return False
    
    success = params['k8s_handler'].create_virtual_machine(
        body,
        metadata=metadata,
        confirmation=params['confirmation'],
        wait=params['wait'],
        my_output=my_output
    )
    if not success:
        return False
    
    local_common.get_virtual_machine(
        params, 
        params['namespace'], 
        params['name'], 
        my_output, 
        k8s_output_handler=k8s_output_handler,
        instance=True
    )

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Virtual machine created')    
    return True