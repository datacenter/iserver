import copy
import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.k8s import output as k8s_output
from lib.workflow.ocp_local_storage_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'list-of-str', None, None, None, None],
        ['view', True, ['state'], 'view', None, None, ['state', 'res'], None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(mparams, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    mparams, error = validate(mparams)
    if error is not None:
        my_output.error(error)
        return False
    
    for cluster in mparams['cluster']:
        params = copy.deepcopy(mparams)
        params['cluster'] = cluster

        ocp_common.print_title(params, my_output, 'Get Information')
        params = ocp_common.workflow_init(params, my_output, log_id, ssh_optional=True)
        if params is None:
            continue

        params = ocp_common.get_operator(params, my_output, csv=True)
        if params['subscription'] is None:
            continue

        state = local_common.check_state(
            params, 
            my_output,
            check_ready=True,
            check_resources=True
        )
        if not state['installed']:
            continue

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