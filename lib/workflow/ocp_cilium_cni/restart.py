import time
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_cni import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['operator', True, True, 'bool', None, None, None, None],
        ['agent', True, True, 'bool', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Rollout restart', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    if params['initialize']:
        params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
        if params is None:
            return False

    if params['operator']:
        local_common.show_operators(params, my_output, k8s_output_handler)

        my_output.default('Restart deployment %s/%s' % (params['__default__']['namespace'], params['__default__']['operator-name']))
        success = params['k8s_handler'].restart_deployment(params['__default__']['namespace'], params['__default__']['operator-name'], my_output=my_output)
        if not success:
            return False

    if params['agent']:
        local_common.show_agents(params, my_output, k8s_output_handler)

        my_output.default('Restart daemon set %s/%s' % (params['__default__']['namespace'], params['__default__']['agent-name']))
        success = params['k8s_handler'].restart_daemon_set(params['__default__']['namespace'], params['__default__']['agent-name'], my_output=my_output)
        if not success:
            return False

    if not params['wait']:
        return True
    
    my_output.default('Take a nap...')
    time.sleep(10)

    if params['operator']:
        success = params['k8s_handler'].wait_deployments_ready_state(
            [{'namespace': params['__default__']['namespace'], 'name': params['__default__']['operator-name']}], 
            max_time=600, 
            my_output=my_output
        )
        if not success:
            return False

        local_common.show_operators(params, my_output, k8s_output_handler)

    if params['agent']:
        success = params['k8s_handler'].wait_daemon_sets_ready_state(
            [{'namespace': params['__default__']['namespace'], 'name': params['__default__']['agent-name']}], 
            max_time=600, 
            my_output=my_output
        )
        if not success:
            return False

        local_common.show_agents(params, my_output, k8s_output_handler)

    return True
