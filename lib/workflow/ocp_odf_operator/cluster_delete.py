from lib import output_helper
from lib.workflow.ocp_odf_operator import common as local_common
from lib.workflow import ocp_common as global_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
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
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


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
    my_output.default('OpenShift Workflow - OpenShift Data Foundation (ODF) Operator - Delete Cluster', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id, ssh_required=True)
    if params is None:
        return False

    if not params['k8s_handler'].is_odf_subscription(params['namespace'], params['name']):
        my_output.default('ODF not installed')
    else:
        success = params['k8s_handler'].delete_storage_cluster(
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False
    
    if not wipe_rook_fs(params, my_output, log_id):
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Cluster deleted')

    return True
