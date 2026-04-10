from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow import ocp_common
from lib.workflow.ocp_ovn_bgp import common as local_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['config', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - OVNKubernetes - Delete route advertisement', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    frr_enabled = params['k8s_handler'].is_ovn_frr_enabled()
    if not frr_enabled:
        my_output.default('FRR %s' % (my_output.add_color('not enabled', 'Red')))
        return False

    ra_enabled = params['k8s_handler'].is_ovn_frr_ra_enabled()
    if not ra_enabled:
        my_output.default('Route advertisement %s' % (my_output.add_color('not enabled', 'Red')))
        return False    
    
    if params['config'] == '__all__':
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
    else:
        success = params['k8s_handler'].delete_route_advertisement(
            params['config'], 
            my_output=my_output, 
            wait=params['wait']
        )
        if not success:
            return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- OVN route advertisement deleted')

    return True
