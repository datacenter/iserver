from lib import output_helper
from lib.linux import main as linux
from lib.workflow import ocp_common as workflow_common


def validate(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)

    if 'cluster' not in params or params['cluster'] is None:
        my_output.error('Cluster name required')
        return None

    params['k8s_handler'] = workflow_common.verify_cluster_name(params['cluster'], log_id=log_id)
    if params['k8s_handler'] is None:
        my_output.error('Cluster invalid: %s' % (params['cluster']))
        return None

    params['key_filename'] = workflow_common.get_ocp_cluster_filename(params['cluster'], log_id=log_id)
    if params['key_filename'] is None:
        my_output.error('Node ssh public key not found: %s' % (params['cluster']))
        return None

    return params


def run(params, log_id=None):
    params = validate(params, log_id=log_id)
    if params is None:
        return None

    nodes_ip = workflow_common.get_cluster_nodes_ip(k8s_handler=params['k8s_handler'], log_id=log_id)
    if nodes_ip is None:
        return None

    interfaces = {}
    for node_name in nodes_ip:
        linux_handler = linux.Linux(
            nodes_ip[node_name],
            'core',
            key_filename=params['key_filename'],
            log_id=log_id
        )
        interfaces[node_name] = linux_handler.get_interfaces_state_up_map()

    return interfaces
