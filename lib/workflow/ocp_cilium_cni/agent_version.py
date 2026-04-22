from lib import output_helper
from lib.workflow.ocp_cilium_cni import common as local_common
from lib.workflow.ocp_cilium_cni import agent_exec
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    if params['initialize']:
        params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
        if params is None:
            return False

    cparams = {}
    cparams['cluster'] = params['cluster']
    cparams['command'] = 'cilium version -o json'
    cparams['k8s_handler'] = params['k8s_handler']
    cparams['initialize'] = False
    cparams['silent'] = True
    response = agent_exec.run(cparams, log_id=log_id)
    if response is None:
        my_output.error('Failed to get cilium version from agents')
        return False
    
    local_common.show_agents_version(params, my_output, response)

    return True
