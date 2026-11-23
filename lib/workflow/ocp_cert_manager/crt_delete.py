from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cert_manager import common as local_common
from lib.workflow import ocp_common
from menu.common import get_confirmation


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['namespace', True, None, 'str', None, None, None, None],
        ['name', True, None, 'str', None, None, None, None],
    ]

    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
    
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def get_certificates(params, my_output, k8s_output_handler):
    object_filter = []
    if params['namespace'] is not None:
        object_filter.append('namespace:%s' % (params['namespace']))
    if params['name'] is not None:
        object_filter.append('name:%s' % (params['name']))

    crts = params['k8s_handler'].get_certificates(object_filter=object_filter, cache_enabled=False)
    if crts is None:
        my_output.error('Failed to get certificates')
        return None
    
    if len(crts) == 0:
        my_output.default('No certificates found')
        return None
    
    k8s_output_handler.print_certificates_state(crts)
    if params['confirmation']:
        if not get_confirmation():
            return None
        
    return crts
        

def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Delete certificate')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    crts = get_certificates(params, my_output, k8s_output_handler)
    if crts is None:
        return False
    
    for crt in crts:
        success = params['k8s_handler'].delete_certificate(
            crt['namespace'], 
            crt['name'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False
        
        success = params['k8s_handler'].delete_secret(
            crt['namespace'], 
            crt['secret'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- certificate deleted')
    return True