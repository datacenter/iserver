from lib import output_helper
from lib.workflow.ocp_cilium_mesh import common as local_common
from lib.workflow.ocp_cilium_cni import common as cilium_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'confirmation' not in params:
        params['confirmation'] = True

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
        'verbose',
        'confirmation',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Disable Cluster Mesh Timescape', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not cilium_common.is_cilium(params, my_output):
        return False

    if not params['k8s_handler'].is_cilium_mesh_enabled():
        my_output.default('Cluster mesh disabled')
        return True
    
    my_output.default('Cluster mesh enabled')

    if not params['k8s_handler'].is_cilium_timescape_enabled(cache_enabled=False):
        my_output.default('Timescape disabled')
        return True
    
    my_output.default('Timescape enabled')

    if not params['k8s_handler'].is_cilium_timescape_mesh_enabled():
        my_output.default('Timescape already disabled for cluster mesh')
        return True
    
    my_output.default('Timescape currently enabled for cluster mesh')

    success = params['k8s_handler'].disable_cilium_timescape_mesh(
        my_output=my_output, 
        confirmation=params['confirmation'], 
        wait=True
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Timescape disabled for cluster mesh')
    return True
