import json
from lib import output_helper
from lib.workflow.ocp_cilium_cni import common as local_common
from lib.workflow.ocp_cilium_cni import agent_exec


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
    
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    cparams = {}
    cparams['cluster'] = params['cluster']
    cparams['command'] = 'cilium version -o json'
    cparams['check-verbose'] = False
    cparams['silent'] = True
    response = agent_exec.run(cparams, log_id=log_id)
    if response is None:
        my_output.error('Failed to get cilium version from agents')
        return False
    
    my_output.default('Cilium Agent Versions', underline=True, before_newline=True)
    for key in response:
        try:
            my_output.default('- %s: %s' % (key, json.loads(response[key].replace("'", '"'))['Client']['Version']))
        except BaseException:
            my_output.error('Failed to get cilium version from agents')
            my_output.default(json.dumps(response), wrap='~~~')
            return False

    return True
