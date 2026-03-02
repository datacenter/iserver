from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_vast_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'view' not in params or params['view'] is None:
        params['view'] = ['state']

    if not isinstance(params['view'], list):
        return None, 'view must be list'

    if len(params['view']) == 0:
        params['view'] = ['state']

    for item in params['view']:
        if item not in ['state', 'res']:
            return None, 'unsupported view %s' % (item)
        
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
        'view',
        'check-verbose',
        'verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - VAST CSI Operator - Get Information', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id, ssh_check=True)
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

        if 'sc' in state:
            k8s_output_handler.print_storage_classes(
                state['sc']
            )

        if 'pvc' in state:
            k8s_output_handler.print_pvcs(
                state['pvc']
            )

    return True
