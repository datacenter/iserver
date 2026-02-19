from lib import output_helper
from lib import ip_helper
from lib.workflow.ocp_cilium_pnet import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'network' not in params or params['network'] is None:
        return None, 'Private network name required'

    if 'app-namespace' not in params or params['app-namespace'] is None:
        params['app-namespace'] = 'default'

    if 'app-name' not in params or params['app-name'] is None:
        params['app-name'] = 'pnet-app'

    if 'app-image' not in params or params['app-image'] is None:
        params['app-image'] = 'netshoot'

    if 'app-ipv4' not in params or params['app-ipv4'] is None:
        return None, 'Application ipv4 address required'

    if not ip_helper.is_valid_ipv4_address(params['app-ipv4']):
        return None, 'Invalid ipv4 address'

    if 'app-mac' not in params or params['app-mac'] is None:
        params['app-mac'] = ip_helper.generate_mac()

    if not ip_helper.is_valid_mac_address(params['app-mac']):
        return None, 'Invalid mac address'

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
        'app-namespace',
        'app-name',
        'app-image',
        'app-ipv4',
        'app-mac',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium Private Network - Attach POD', before_newline=True, after_newline=True, double_underline=True) 

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_pnet_ready(params, my_output):
        return False
    
    success = params['k8s_handler'].create_clusterwide_private_network_pod(
        params['app-namespace'], 
        params['app-name'], 
        params['app-image'], 
        params['network'], 
        params['app-ipv4'], 
        None, 
        params['app-mac'], 
        caps=True,
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Pod attached to private network created and running')

    return True
