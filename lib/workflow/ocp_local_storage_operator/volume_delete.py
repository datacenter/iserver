import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.k8s import output as k8s_output
from lib.workflow.ocp_local_storage_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'

    allowed_keys = [
        'cluster',
        'check-verbose'
    ]  
    return local_common.sanitize_params(params, allowed_keys), None


def validate_values(params, my_output):
    my_output.default('Collect cluster state and validate input values', before_newline=True, underline=True)

    my_output.default('- get kubernetes node names')
    params['node'] = params['k8s_handler'].get_nodes_name()
    if params['node'] is None:
        my_output.error('Failed to get node names')
        return None
    
    if len(params['node']) == 0:
        my_output.error('Unexpected no nodes found')
        return None
    
    my_output.default('- get local volume discovery')
    params['local_volume_discovery'] = params['k8s_handler'].get_local_volume_discoveries(cache_enabled=False)
    if params['local_volume_discovery'] is None:
        my_output.error('Unexpected error in getting information')
        return None

    my_output.default('- get local volume sets')
    params['local_volume_set'] = params['k8s_handler'].get_local_volume_sets(pv_info=True, cache_enabled=False)
    if params['local_volume_set'] is None:
        my_output.error('Unexpected error in getting information')
        return None

    my_output.default('- get local volumes')
    params['local_volume'] = params['k8s_handler'].get_local_volumes(pv_info=True, cache_enabled=False)
    if params['local_volume'] is None:
        my_output.error('Unexpected error in getting information')
        return None

    return params


def unlabel_nodes(params, my_output):
    my_output.default('Unlabel Storage Nodes', before_newline=True, underline=True)
    my_output.default('- node label: cluster.ocs.openshift.io/openshift-storage=""')
    for node_name in params['node']:
        my_output.default('- node: %s' % (node_name))
        if not params['k8s_handler'].delete_node_label(node_name, 'cluster.ocs.openshift.io/openshift-storage'):
            my_output.error('REST API failed')
            return False
    
    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    my_output.default('OpenShift Workflow - Local Storage Operator - Delete Local Volume', before_newline=True, after_newline=True, double_underline=True)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not params['k8s_handler'].check_local_storage_subscription(params['name'], my_output=my_output, required=False):
        return False
    
    params = validate_values(params, my_output)
    if params is None:
        return False
    
    success = params['k8s_handler'].delete_local_volumes(
        params['local_volume'],
        my_output=my_output,
        k8s_output=k8s_output_handler
    )
    if not success:
        return False
    
    success = params['k8s_handler'].delete_local_volume_sets(
        params['local_volume_set'],
        my_output=my_output,
        k8s_output=k8s_output_handler
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_local_volume_discoveries(
        params['local_volume_discovery'],
        my_output=my_output,
        k8s_output=k8s_output_handler
    )
    if not success:
        return False

    if not unlabel_nodes(params, my_output): 
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Volumes deleted')
    my_output.default('- Node labels removed')

    return True
