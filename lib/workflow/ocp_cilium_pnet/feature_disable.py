from lib import output_helper
from lib.workflow.ocp_cilium_pnet import common as local_common
from lib.workflow.ocp_cilium_pnet import wipe
from lib.workflow.ocp_cilium_cni import common as cilium_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'wipe' not in params:
        params['wipe'] = False

    if not isinstance(params['wipe'], bool):
        return None, 'wipe param must be true or false'
    
    if 'confirmation' not in params:
        params['confirmation'] = True

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'
    
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
        'wipe',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium Private Network - Disable', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not cilium_common.is_cilium(params, my_output):
        return False

    if not params['k8s_handler'].is_cilium_private_network_enabled(cache_enabled=False):
        my_output.default('Private network already disabled')
        return True
    
    if params['wipe']:
        child_params = {}
        child_params['cluster'] = params['cluster']
        child_params['check-verbose'] = False
        child_params['confirmation'] = params['confirmation']
        success = wipe.run(child_params, log_id=log_id)
        if not success:
            return False
        
    if params['k8s_handler'].is_cilium_private_network_configured(cache_enabled=False):
        my_output.error('Unconfigure private networks crds first')
        return False

    success = params['k8s_handler'].disable_cilium_private_network(
        my_output=my_output, 
        confirmation=params['confirmation']
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Private Network feature disabled')

    return True
