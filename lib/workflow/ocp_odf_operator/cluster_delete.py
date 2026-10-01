from lib import output_helper
from lib.workflow.ocp_odf_operator import common as local_common
from lib.workflow import ocp_common as global_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params

    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def wipe_rook_fs(params, my_output, log_id):
    # https://rook.io/docs/rook/latest/Storage-Configuration/ceph-teardown/#cleaning-up-a-cluster
    my_output.default('Wipe rook filesystem', before_newline=True, underline=True)

    handlers = global_common.get_nodes_ssh_handler(
        params['cluster'],
        params['k8s_handler'],
        log_id=log_id
    )
    for node_name in handlers:
        my_output.default('- %s' % (node_name))
        success = handlers[node_name].delete_directory('/var/lib/rook/*', sudo=True)
        if not success:
            return False

    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Delete Cluster')
    params = ocp_common.workflow_init(params, my_output, log_id, ssh_optional=True)
    if params is None:
        return False
    
    if not params['k8s_handler'].is_odf_subscription(params['__default__']['namespace'], params['__default__']['name']):
        my_output.default('ODF not installed')
    else:
        success = params['k8s_handler'].delete_storage_cluster(
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False
    
    if params['ssh_handler'] is not None:
        if not wipe_rook_fs(params, my_output, log_id):
            return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Cluster deleted')
    return True