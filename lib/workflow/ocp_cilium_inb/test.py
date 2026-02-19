import yaml
from lib import output_helper
from lib.workflow.ocp_cilium_inb import common as local_common
from lib.workflow import ocp_common as global_common
from lib.workflow.ocp_cilium_cni import common as cilium_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'confirmation' not in params:
        params['confirmation'] = True

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'confirmation',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Isovalent Network Bridge Functional Test', before_newline=True, after_newline=True, double_underline=True) 

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
        my_output.error('Cluster mesh disabled')
        return False
    
    my_output.default('Cluster mesh enabled')
    
    if not params['k8s_handler'].is_cilium_private_network_enabled(cache_enabled=False):
        my_output.error('Private network disabled')
        return True

    my_output.default('Private network enabled')

    success = True
    if success:
        my_output.default('Test completed successfully', before_newline=True)
        
    return success
