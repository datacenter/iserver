import time
from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_oauth import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'scope' not in params or params['scope'] is None:
        params['scope'] = 'oauth'

    if params['scope'] not in ['oauth', 'operator']:
        return None, 'unsupported scope value'
        
    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'

    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'scope',
        'check-verbose',
        'confirmation',
        'verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - OAuth - Restart', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
    params = local_common.get_state(
        params,
        my_output,
        scope=['deployment', 'pod']
    )

    if params['scope'] == 'operator':
        k8s_output_handler.print_deployments_state(params['state']['operator_deployment'])
        k8s_output_handler.print_pods_state(params['state']['operator_pod'])

        for deployment in params['state']['operator_deployment']:
            replicas = deployment['replicas']
            success = params['k8s_handler'].set_deployment_replicas(
                deployment['namespace'], 
                deployment['name'], 
                0,
                confirmation=params['confirmation'], 
                my_output=my_output,
                wait=True
            )
            if not success:
                return False
            
            success = params['k8s_handler'].set_deployment_replicas(
                deployment['namespace'], 
                deployment['name'], 
                replicas,
                confirmation=params['confirmation'], 
                my_output=my_output,
                wait=True
            )
            if not success:
                return False
            
        params = local_common.get_state(
            params,
            my_output,
            scope=['pod']
        )
        k8s_output_handler.print_pods_state(params['state']['operator_pod'])

    if params['scope'] == 'oauth':
        k8s_output_handler.print_deployments_state(params['state']['oauth_deployment'])
        k8s_output_handler.print_pods_state(params['state']['oauth_pod'])

        for deployment in params['state']['oauth_deployment']:
            success = params['k8s_handler'].set_deployment_replicas(
                deployment['namespace'], 
                deployment['name'], 
                0,
                confirmation=params['confirmation'], 
                my_output=my_output,
                wait=False
            )
            if not success:
                return False
            
            my_output.default('Take a nap...')
            time.sleep(30)

            success = params['k8s_handler'].wait_deployment_ready_state(
                deployment['namespace'], 
                deployment['name'], 
                my_output=my_output
            )
            
        params = local_common.get_state(
            params,
            my_output,
            scope=['pod']
        )
        k8s_output_handler.print_pods_state(params['state']['oauth_pod'])

    return True
