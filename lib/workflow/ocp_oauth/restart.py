import time
from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_oauth import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['scope', True, 'oauth', 'str', None, None, ['oauth', 'operator'], None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Restart')
    params = ocp_common.workflow_init(params, my_output, log_id)
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
