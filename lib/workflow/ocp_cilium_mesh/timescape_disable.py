from lib import output_helper
from lib.workflow.ocp_cilium_mesh import common as local_common
from lib.workflow import ocp_common


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
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Disable timescape')
    params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
    if params is None:
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
