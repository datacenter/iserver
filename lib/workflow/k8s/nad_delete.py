from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.k8s import common as local_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'namespace' not in params:
        params['namespace'] = None

    if 'name' not in params:
        params['name'] = None

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
        'verbose',
        'check-verbose',
        'confirmation'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('Kubernetes Workflow - Network Attachment Definition - Delete', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    nads = local_common.get_nads(
        params['k8s_handler'],
        namespace=params['namespace'], 
        name=params['name']
    )
    if nads is None:
        my_output.error('Failed to get nads')
        return False
    
    if len(nads) == 0:
        my_output.default('No nad found')
        return True
    
    k8s_output_handler.print_nads(nads)

    if params['confirmation']:
        if not get_confirmation():
            return False

    success = True
    for nad_info in nads:
        nad_success = params['k8s_handler'].delete_nad(
            nad_info['namespace'],
            nad_info['name'],
            my_output=my_output, 
            wait=True
        )
        success = success and nad_success

    if not success:
        my_output.error('Some delete api calls failed', before_newline=True)

    return success
