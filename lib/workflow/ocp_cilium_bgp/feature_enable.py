from lib import output_helper
from lib.workflow.ocp_cilium_bgp import common as local_common
from lib.workflow.ocp_cilium_cni import common as cilium_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

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
        'confirmation',
        'check-verbose',
        'verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium BGP Control Plane - Enable', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not cilium_common.is_cilium(params, my_output):
        return False

    if params['k8s_handler'].is_cilium_bgp_enabled(cache_enabled=False):
        my_output.default('BGP control plane %s' % (my_output.add_color('already enabled', 'Green')))
    else:
        success = params['k8s_handler'].enable_cilium_bgp(
            my_output=my_output, 
            confirmation=params['confirmation']
        )
        if not success:
            return False        
    
    if not local_common.is_bgp_crd(params, my_output=my_output):
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- BGP Control Plane feature enabled')
    my_output.default('- CRD ready')

    return True
