from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_mesh import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['mesh-ip', False, None, 'ipv4', None, None, None, None],
        ['mesh-name', False, None, 'str', None, None, None, None],
        ['mesh-port', False, None, 'int', 1, 65535, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Add cluster')
    params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
    if params is None:
        return False
    
    if not params['k8s_handler'].is_cilium_mesh_enabled():
        my_output.default('Cluster mesh not enabled', before_newline=True)
        return False

    my_output.default('Cluster mesh enabled', before_newline=True, after_newline=True)

    success = params['k8s_handler'].add_cilium_mesh_cluster(
        params['mesh-ip'], 
        params['mesh-port'], 
        params['mesh-name'], 
        my_output=my_output, 
        confirmation=params['confirmation'],
        wait=params['wait']
    )
    if not success:
        return False

    status = params['k8s_handler'].get_cilium_mesh_status(object_filter=['cluster_name:%s' % (params['mesh-name'])])
    k8s_output_handler.print_cilium_mesh_status(status)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Cluster mesh added')

    return True
