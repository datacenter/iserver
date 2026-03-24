from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow import ocp_common
from lib.workflow.k8s import common as local_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['__id__', True, None, None, None, None, None, None],
        ['namespace', False, None, 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
        ['master', False, None, 'str', None, None, None, None],
        ['vlan', False, None, 'int', 1, 4096, None, None],
        ['ipam', False, None, 'str', None, None, ['static', 'local'], None],
        ['address', True, None, 'str', None, None, None, None],
        ['gateway', True, None, 'str', None, None, None, None],
        ['route', True, [], 'list-of-str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules, extras=['type', '__type__'])
    if not success:
        return None, params

    params, reason = local_common.validate_nad_ipam(params, modes=['static', 'local'])
    if params is None:
        return None, reason

    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('Kubernetes Workflow - Network Attachment Definition - Create VLAN', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    success = params['k8s_handler'].create_nad_vlan(
        params['namespace'], 
        params['name'], 
        params['master'],
        params['vlan'],
        params['ipam'],
        params['address'],
        params['gateway'],
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True        
    )
    if not success:
        return False
    
    info = params['k8s_handler'].get_nad(
        params['namespace'], 
        params['name'], 
        cache_enabled=False
    )
    if info is None:
        my_output.error('Failed to get nad')
        return False
    
    k8s_output_handler.print_nads([info])

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- nad created')
    return True
