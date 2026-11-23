import copy
from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_vast_operator import common as local_common
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
        params = ocp_common.workflow_init(params, my_output, log_id)
        if params is None:
            continue

        params = ocp_common.get_operator(params, my_output)
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

        if 'res' in params['view']:
            k8s_output_handler.print_vast_drivers_state(
                state['driver']
            )
        
            k8s_output_handler.print_vast_clusters_state(
                state['cluster']
            )

            k8s_output_handler.print_vast_storages_state(
                state['storage']
            )

            k8s_output_handler.print_deployments_state(
                state['dep']
            )

            k8s_output_handler.print_daemon_sets_state(
                state['ds']
            )

            k8s_output_handler.print_pods_state(
                state['pod']
            )

            if 'sc' in state:
                k8s_output_handler.print_storage_classes(
                    state['sc']
                )

            if 'pvc' in state:
                k8s_output_handler.print_pvcs(
                    state['pvc']
                )

    return True
