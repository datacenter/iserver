import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.k8s import output as k8s_output
from lib.workflow.ocp_local_storage_operator import common as local_common


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


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Local Storage Operator - Get Information', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    state = local_common.check_state(
        params, 
        my_output,
        check_ready=True,
        check_resources=True
    )
    if not state['installed']:
        return True

    if state['local_volume_discovery'] is not None and len(state['local_volume_discovery']) > 0:
        k8s_output_handler.print_local_volume_discoveries(state['local_volume_discovery'])

    if state['local_volume_discovery_result'] is not None and len(state['local_volume_discovery_result']) > 0:
        k8s_output_handler.print_local_volume_discovery_results(state['local_volume_discovery_result'])

    if state['local_volume_set'] is not None and len(state['local_volume_set']) > 0:
        k8s_output_handler.print_local_volume_sets(state['local_volume_set'])

    if state['local_volume'] is not None and len(state['local_volume']) > 0:
        k8s_output_handler.print_local_volumes(state['local_volume'])

    if state['local_volume_set'] is not None:
        for item in state['local_volume_set']:
            storage_class = params['k8s_handler'].get_storage_class(item['storage_class'], pv_info=True)
            if storage_class is not None:
                k8s_output_handler.print_storage_classes_with_resources([storage_class])

    if state['local_volume'] is not None:
        sc_names = []
        for item in state['local_volume']:
            for device in item['device']:
                if device['sc'] not in sc_names:
                    sc_names.append(device['sc'])

        for item in sc_names:
            storage_class = params['k8s_handler'].get_storage_class(item, pv_info=True)
            if storage_class is not None:
                k8s_output_handler.print_storage_classes_with_resources([storage_class])
    
    return True
