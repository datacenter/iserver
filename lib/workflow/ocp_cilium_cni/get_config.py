from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_cilium_cni import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['config', True, True, 'bool', None, None, None, None],
        ['map', True, True, 'bool', None, None, None, None],
        ['state', True, False, 'bool', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Get config', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    if params['initialize']:
        params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
        if params is None:
            return False

    if params['config'] or params['state']:
        cilium_config = params['k8s_handler'].get_cilium_config()
        if cilium_config is None:
            my_output.error('Failed to get cilium configuration')
        else:
            if params['config']:
                k8s_output_handler.print_cilium_config(cilium_config)
            
            if params['config'] or params['state']:
                k8s_output_handler.print_cilium_config_state(cilium_config)

    if params['map']:
        cilium_config_map = params['k8s_handler'].get_config_map(
            namespace='cilium', 
            name='cilium-config'
        )
        if cilium_config_map is None:
            my_output.error('Failed to get config map cilium/cilium-config')
        else:
            my_output.default('Cilium Config Map', underline=True, before_newline=True)
            my_output.dictionary(
                cilium_config_map['data']
            )

    return True
