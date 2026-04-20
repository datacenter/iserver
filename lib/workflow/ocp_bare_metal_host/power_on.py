from lib import output_helper
from lib.workflow.ocp_bare_metal_host import common as local_common
from lib.k8s import output as k8s_output
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['node', False, None, 'str', 1, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Bare Metal Host - Power on', before_newline=True, after_newline=True, double_underline=True)

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
    
    found = False
    for bmh in bmhs:
        if bmh['name'] == params['node']:
            found = True
            break

    if not found:
        my_output.error('Node %s not found' % (params['node']))
        return False

    success = params['k8s_handler'].set_bare_metal_host_power_on(
        params['__default__']['namespace'],
        params['node'],
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
    my_output.default('- bare metal hosts powered on')

    return True
