from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_mtv_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    network_rules = [
        ['source', False, None, 'str', None, None, None, None],
        ['destination', False, None, 'str', None, None, ['pod', 'multus'], None]
    ]

    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['namespace', True, 'openshift-mtv', 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
        ['source', False, None, 'str', None, None, None, None],
        ['destination', False, None, 'str', None, None, None, None],
        ['network', False, None, 'list-of-dict', 1, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(
        params, 
        rules,  
        nested=dict(subnet=network_rules)
    )
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

    ocp_common.print_title(params, my_output, 'Create Network Map')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    if not local_common.is_subscription_ready(params, my_output, details=True):
        return True

    if params['k8s_handler'].is_network_map(params['namespace'], params['name']):
        my_output.default('Network map %s already defined' %  (params['name']), before_newline=True)
        return True
    
    success = params['k8s_handler'].create_network_map(
        params['namespace'],
        params['name'],
        params['source'],
        params['destination'],
        params['network'],
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True            
    )
    if not success:
        return False        

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- network map created and ready')

    return True