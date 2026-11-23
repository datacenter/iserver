from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cert_manager import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['namespace', False, None, 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
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

    ocp_common.print_title(params, my_output, 'Delete issuer')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    issuer = params['k8s_handler'].get_issuer(params['namespace'], params['name'], secret_info=True, cache_enabled=False, optimized=False)
    if issuer is None:
        my_output.default('Issuer %s/%s %s' % (params['namespace'], params['name'], my_output.add_color('already deleted', 'Green')))
        return True
    
    k8s_output_handler.print_issuers_state([issuer])
    success = params['k8s_handler'].delete_issuer(
        params['namespace'], 
        params['name'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].delete_secret(
        issuer['namespace'], 
        issuer['secret'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
        
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- issuer deleted')
    return True