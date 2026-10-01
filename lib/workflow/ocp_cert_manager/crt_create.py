import json
from lib import file_helper
from lib import ip_helper
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cert_manager import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['namespace', False, None, 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
        ['cn', False, None, 'str', None, None, None, None],
        ['issuer', False, None, 'str', None, None, None, None]
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

    ocp_common.print_title(params, my_output, 'Create certificate')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False
    
    issuer = params['k8s_handler'].get_issuer(params['namespace'], params['issuer'])
    if issuer is not None:
        kind = 'Issuer'
    else:
        issuer = params['k8s_handler'].get_cluster_issuer(params['issuer'])
        if issuer is None:
            my_output.error('Issuer or ClusterIssuer not found with name %s' % (params['name']))
            return False
        
        kind = 'ClusterIssuer'

    sucess = params['k8s_handler'].create_certificate(
        params['namespace'], 
        params['name'], 
        params['issuer'], 
        kind=kind, 
        ca=True, 
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=params['wait']
    )
    if not sucess:
        return False
    
    crt = params['k8s_handler'].get_certificate(params['namespace'], params['name'], secret_info=True, cache_enabled=False, optimized=False)
    if crt is None:
        my_output.error('Certificate not found')
        return False
    
    k8s_output_handler.print_certificates_state([crt])

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- certificate created')
    return True