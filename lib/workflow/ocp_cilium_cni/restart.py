import json
import time
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_cni import common as local_common
from lib.workflow.ocp_cilium_cni import agent_exec


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'operator' not in params:
        params['operator'] = True

    if not isinstance(params['operator'], bool):
        return None, 'operator param must be true or false'

    if 'agent' not in params:
        params['agent'] = True

    if not isinstance(params['agent'], bool):
        return None, 'agent param must be true or false'

    if 'wait' not in params:
        params['wait'] = True

    if not isinstance(params['wait'], bool):
        return None, 'wait param must be true or false'

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
        'operator',
        'agent',
        'wait',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Rollout restart', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if params['operator']:
        local_common.show_operators(params, my_output, k8s_output_handler)

        my_output.default('Restart deployment %s/%s' % (params['namespace'], params['operator-name']))
        success = params['k8s_handler'].restart_deployment(params['namespace'], params['operator-name'], my_output=my_output)
        if not success:
            return False

    if params['agent']:
        local_common.show_agents(params, my_output, k8s_output_handler)

        my_output.default('Restart daemon set %s/%s' % (params['namespace'], params['agent-name']))
        success = params['k8s_handler'].restart_daemon_set(params['namespace'], params['agent-name'], my_output=my_output)
        if not success:
            return False

    if not params['wait']:
        return True
    
    my_output.default('Take a nap...')
    time.sleep(10)

    if params['operator']:
        success = params['k8s_handler'].wait_deployments_ready_state(
            [{'namespace': params['namespace'], 'name': params['operator-name']}], 
            max_time=600, 
            my_output=my_output
        )
        if not success:
            return False

        local_common.show_operators(params, my_output, k8s_output_handler)

    if params['agent']:
        success = params['k8s_handler'].wait_daemon_sets_ready_state(
            [{'namespace': params['namespace'], 'name': params['agent-name']}], 
            max_time=600, 
            my_output=my_output
        )
        if not success:
            return False

        local_common.show_agents(params, my_output, k8s_output_handler)

    return True
