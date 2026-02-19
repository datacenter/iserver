from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_cilium_cni import common as local_common
from lib.workflow import ocp_common as global_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'config' not in params:
        params['config'] = True

    if not isinstance(params['config'], bool):
        return None, 'config param must be true or false'
    
    if 'map' not in params:
        params['map'] = False

    if not isinstance(params['map'], bool):
        return None, 'map param must be true or false'
    
    if 'state' not in params:
        params['state'] = False

    if not isinstance(params['state'], bool):
        return None, 'state param must be true or false'
        
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
        'config',
        'map',
        'state',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Get config', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id, api_check=False)
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
            name='cilium-config',
            optimize=True
        )
        if cilium_config_map is None:
            my_output.error('Failed to get config map cilium/cilium-config')
        else:
            my_output.default('Cilium Config Map', underline=True, before_newline=True)
            my_output.dictionary(
                cilium_config_map['data']
            )

    return True
