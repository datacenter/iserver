from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_cilium_cni import agent_version
from lib.workflow.ocp_cilium_cni import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['agent', True, None, 'str', None, None, None, None],
        ['view', False, None, 'list-of-str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Get agent', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
    if params is None:
        return False

    if 'pod' in params['view']:
        local_common.show_agents(params, my_output, k8s_output_handler)

    if 'logs' in params['view']:
        pods = params['k8s_handler'].get_cilium_agent_logs(
            agent=params['agent'], 
            cache_enabled=False
        )
        if pods is None:
            my_output.error('Failed to get cilium agent logs')
        else:
            for pod in pods:
                my_output.default('Cilium Agent [%s/%s]' % (pod['namespace'], pod['name']), underline=True, before_newline=True)
                my_output.default(pod['logs'], wrap='~~~')

    if 'version' in params['view']:
        cparams = {}
        cparams['cluster'] = params['cluster']
        cparams['k8s_handler'] = params['k8s_handler']
        cparams['initialize'] = False
        cparams['silent'] = True
        success = agent_version.run(cparams, log_id=log_id)
        if not success:
            return False

    return True
