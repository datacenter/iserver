import os
from lib import ip_helper
from lib import output_helper
from lib import ssh
from lib.k8s import output as k8s_output
from lib.workflow import ocp_common
from lib.workflow.k8s import common as local_common
from lib.linux import settings


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'namespace' not in params or params['namespace'] is None:
        return None, 'Namespace required'

    if 'name' not in params or params['name'] is None:
        return None, 'Name required'

    if 'master' not in params:
        return None, 'Master interface name required'

    if 'vlan' not in params:
        return None, 'Vlan id required'

    success, reason = local_common.validate_vlan(params['vlan'])
    if not success:
        return None, reason

    params, reason = local_common.validate_nad_ipam(params, modes=['static', 'local'])
    if params is None:
        return None, reason

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'

    if 'confirmation' not in params:
        params['confirmation'] = True

    allowed_keys = [
        'cluster',
        'namespace',
        'name',
        'master',
        'vlan',
        'ipam',
        'address',
        'gateway',
        'verbose',
        'check-verbose',
        'confirmation'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('Kubernetes Workflow - Network Attachment Definition - Create VLAN', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    success = params['k8s_handler'].create_nad_vlan(
        params['namespace'], 
        params['name'], 
        params['master'],
        params['vlan'],
        params['ipam'],
        params['address'],
        params['gateway'],
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True        
    )
    if not success:
        return False
    
    info = params['k8s_handler'].get_nad(
        params['namespace'], 
        params['name'], 
        cache_enabled=False
    )
    if info is None:
        my_output.error('Failed to get nad')
        return False
    
    k8s_output_handler.print_nads([info])
    return True
