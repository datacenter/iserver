from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_mtv_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'map' not in params:
        return None, 'Map name required'
    
    if 'source' not in params:
        return None, 'Source name required'

    if 'destination' not in params:
        return None, 'Destination name required'

    if 'network' not in params:
        return None, 'Network list required'

    if not isinstance(params['network'], list):
        return None, 'Network list required'
    
    if len(params['network']) == 0:
        return None, 'Network list with items required'
    
    for item in params['network']:
        if 'source' not in item:
            return None, 'Network.source required'

        if 'destination' not in item:
            return None, 'Network.destination required'

        if item['destination'] not in ['pod', 'multus']:
            return None, 'Network.destination must be pod or multus'
        
    if 'confirmation' not in params:
        params['confirmation'] = True

    if 'wait' not in params:
        params['wait'] = True

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
        'type',
        'map',
        'source',
        'destination',
        'network',
        'wait',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Migration Toolkit for Virtualization Operator - Create Network Map', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_subscription_ready(params, my_output, details=True):
        return True

    if params['k8s_handler'].is_network_map(params['namespace'], params['map']):
        my_output.default('Network map %s already defined' %  (params['map']), before_newline=True)
        return True
    
    success = params['k8s_handler'].create_network_map(
        params['namespace'],
        params['map'],
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
