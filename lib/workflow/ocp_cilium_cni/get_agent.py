import yaml
from lib.k8s import output as k8s_output
from lib import output_helper
from lib import filter_helper
from lib.workflow.ocp_cilium_cni import common as local_common
from lib.workflow import ocp_common as global_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'agent' not in params:
        params['agent'] = None

    if 'pod' not in params:
        params['pod'] = True

    if not isinstance(params['pod'], bool):
        return None, 'pod param must be true or false'
    
    if 'logs' not in params:
        params['logs'] = False

    if not isinstance(params['logs'], bool):
        return None, 'logs param must be true or false'
        
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
        'agent',
        'pod',
        'logs',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Get agent', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id, api_check=False)
    if params is None:
        return False

    if params['pod']:
        local_common.show_agents(params, my_output, k8s_output_handler)

    if params['logs']:
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

    return True
