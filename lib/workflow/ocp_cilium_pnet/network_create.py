from lib import output_helper
from lib import ip_helper
from lib.workflow.ocp_cilium_pnet import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'network' not in params or params['network'] is None:
        return None, 'Private network name required'

    if 'subnet' not in params:
        params['subnet'] = None

    if 'gateway' not in params:
        params['gateway'] = None

    if 'inb' not in params:
        params['inb'] = []

    if params['gateway'] is not None:
        if ip_helper.is_valid_ipv4_cidr(params['gateway']):
            params['subnet'] = ip_helper.get_network_cidr_from_cidr(params['gateway'])
            params['gateway'] = params['gateway'].split('/')[0]
    
    if params['subnet'] is None:
        return None, 'Private network subnet required'
    
    if params['gateway'] is not None:
        if not ip_helper.is_valid_ipv4_address(params['gateway']):
            return None, 'Gateway ipv4 format required'
        
        if not ip_helper.is_ipv4_in_cidr(params['gateway'], params['subnet']):
            return None, 'Gateway must belong to subnet'
        
    if 'confirmation' not in params:
        params['confirmation'] = True

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'
    
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
        'network',
        'subnet',
        'gateway',
        'inb',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium Private Network - Create Private Network', before_newline=True, after_newline=True, double_underline=True) 

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_pnet_ready(params, my_output):
        return False
    
    success = params['k8s_handler'].create_clusterwide_private_network(
        params['network'], 
        params['subnet'], 
        inb=params['inb'], 
        gatewayv4=params['gateway'], 
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False


    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Private Network created')

    return True
