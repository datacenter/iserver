from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow import ocp_common
from lib.workflow.ocp_ovn_bgp import common as local_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - OVNKubernetes - Wipe frr-k8s and route advertisements', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    frr_enabled = params['k8s_handler'].is_ovn_frr_enabled()
    ra_enabled = params['k8s_handler'].is_ovn_frr_ra_enabled()

    if ra_enabled:
        configs = params['k8s_handler'].get_route_advertisements(cache_enabled=False)
        if configs is None:
            my_output.error('Failed to get route advertisements')
            return False
        
        for config in configs:
            success = params['k8s_handler'].delete_route_advertisement(
                config['name'], 
                my_output=my_output, 
                wait=params['wait']
            )
            if not success:
                return False

        success = params['k8s_handler'].disable_ovn_frr_ra(
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=params['wait']
        )
        if not success:
            return False

    if frr_enabled:
        configs = params['k8s_handler'].get_frr_configurations(cache_enabled=False)
        if configs is None:
            my_output.error('Failed to get frr configurations')
            return False

        for config in configs:
            success = params['k8s_handler'].delete_frr_configuration(
                params['__default__']['namespace'], 
                config['name'], 
                my_output=my_output, 
                wait=params['wait']
            )
            if not success:
                return False
            
        success = params['k8s_handler'].disable_ovn_frr(
            confirmation=params['confirmation'], 
            my_output=my_output, 
            wait=params['wait']
        )
        if not success:
            return False

        if params['__default__']['delete-namespace']:
            success = params['k8s_handler'].delete_namespace(
                params['__default__']['namespace'],
                my_output=my_output,
                wait=True
            )
            if not success:
                return False

    info = params['k8s_handler'].get_cluster_network_operator(cache_enabled=False)
    k8s_output_handler.print_network_operators([info])

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- OVN frr and route advertisement wiped')

    return True
