from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_bare_metal_host import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['node', False, None, 'str', 1, None, None, None],
        ['bmc', False, None, 'ip', None, None, None, None],
        ['type', False, None, 'str', None, None, ['ucsc'], None],
        ['username', False, None, 'str', None, None, None, None],
        ['password', False, None, 'str', None, None, None, None],
        ['mac', False, None, 'mac', None, None, None, None],
        ['serial', True, None, 'str', None, None, None, None],
        ['boot', False, None, 'str', None, None, ['uefi', 'secure', 'legacy'], None],
        ['cert', False, None, 'bool', None, None, None, None]
    ]

    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Bare Metal Host - Create host', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    # verify bmh node names
    bmhs = params['k8s_handler'].get_bare_metal_hosts(cache_enabled=False)
    if bmhs is None:
        my_output.error('Failed to get BareMetalHost crd')
        return False

    k8s_output_handler.print_bare_metal_hosts_state(bmhs)
        
    found = False
    for bmh in bmhs:
        if bmh['name'] == params['node']:
            found = True
            break

    if found:
        my_output.default('Node %s %s' % (params['node'], my_output.add_color('found', 'Green')), before_newline=True)
        return True

    if not params['k8s_handler'].is_noproxy(params['bmc'], my_output=my_output):
        success = params['k8s_handler'].add_noproxy(
            params['bmc'],
            my_output=my_output,
            confirmation=params['confirmation'],
            wait=True
        )
        if not success:
            return False
            
    success = params['k8s_handler'].create_bare_metal_host(
        params['__default__']['namespace'],
        params['node'],
        params['bmc'],
        params['username'],
        params['password'],
        params['cert'],
        params['mac'],
        params['boot'],
        server_type=params['type'],
        serial=params['serial'],
        my_output=my_output,
        confirmation=params['confirmation'],
        wait=params['wait']
    )
    if not success:
        return False

    bmhs = params['k8s_handler'].get_bare_metal_hosts(
        object_filter=['name:%s' % (params['node'])], 
        cache_enabled=False
    )
    k8s_output_handler.print_bare_metal_hosts_state(bmhs)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- bare metal host created')

    return True
