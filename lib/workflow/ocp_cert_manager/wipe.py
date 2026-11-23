from lib import output_helper
from lib.workflow.ocp_cert_manager import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def cleanup_cert_manager(params, my_output):
    local_common.print_resource_summary(params, my_output)
    if not params['state']['resources']:
        return True
    
    success = params['k8s_handler'].wipe_certificates(my_output=my_output, wait=True)
    if not success:
        return False
    
    success = params['k8s_handler'].wipe_issuers(my_output=my_output, wait=True)
    if not success:
        return False
    
    success = params['k8s_handler'].wipe_cluster_issuers(my_output=my_output, wait=True)
    if not success:
        return False

    if params['resource']['certificate'] is not None:
        for certificate in params['resource']['certificate']:
            success = params['k8s_handler'].delete_secret(
                certificate['namespace'], 
                certificate['secret'], 
                my_output=my_output, 
                wait=True
            )
            if not success:
                return False  
                
    if params['resource']['issuer'] is not None:
        for issuer in params['resource']['issuer']:
            success = params['k8s_handler'].delete_secret(
                issuer['namespace'], 
                issuer['secret'], 
                my_output=my_output, 
                wait=True
            )
            if not success:
                return False    

    if params['resource']['cluster issuer'] is not None:
        for issuer in params['resource']['cluster issuer']:
            success = params['k8s_handler'].delete_secret(
                params['__default__']['namespace'], 
                issuer['secret'], 
                my_output=my_output, 
                wait=True
            )
            if not success:
                return False    

    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Wipe')
    params = ocp_common.workflow_init(params, my_output, log_id, ssh_required=True, linux_required=True)
    if params is None:
        return False
    
    params = local_common.collect_state_info(params)

    success = cleanup_cert_manager(params, my_output)
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- resources wiped')
    return True