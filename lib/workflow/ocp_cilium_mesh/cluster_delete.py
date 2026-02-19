from lib import ip_helper
from lib import output_helper
from lib.workflow.ocp_cilium_mesh import common as local_common
from lib.workflow.ocp_cilium_cni import common as cilium_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'mesh-ip' not in params or len(params['mesh-ip']) == 0:
        params['mesh-ip'] = None

    if params['mesh-ip'] is not None and not ip_helper.is_valid_ipv4_address(params['mesh-ip']):
        return None, 'mesh-ip param must be ipv4 address'

    if 'mesh-name' not in params:
        params['mesh-name'] = None

    if params['mesh-name'] is not None and not isinstance(params['mesh-name'], str):
        return None, 'mesh-name param must be str'

    if params['mesh-name'] is None and params['mesh-ip'] is None:
        return None, 'select cluster by name or ip address'

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
        'mesh-ip',
        'mesh-name',
        'verbose',
        'confirmation',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Delete Cluster from Mesh', before_newline=True, after_newline=True, double_underline=True)

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
        my_output.default('Cluster mesh not enabled', before_newline=True)
        return True

    my_output.default('Cluster mesh enabled', before_newline=True, after_newline=True)

    success = params['k8s_handler'].delete_cilium_mesh_cluster(
        mesh_ip=params['mesh-ip'], 
        mesh_name=params['mesh-name'], 
        my_output=my_output, 
        confirmation=params['confirmation']
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Cluster mesh deleted')

    return True
