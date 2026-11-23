from lib import output_helper
from lib.workflow.ocp_cilium_mesh import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def delete_secret(params, my_output):
    success = params['k8s_handler'].delete_secret(
        params['__default__']['namespace'], 
        params['__default__']['secret'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_secret(
        params['__default__']['namespace'], 
        params['__default__']['certificate'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].delete_secret(
        params['__default__']['namespace'], 
        params['__default__']['certificate-admin'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_secret(
        params['__default__']['namespace'], 
        params['__default__']['certificate-remote'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].delete_secret(
        params['__default__']['namespace'], 
        params['__default__']['certificate-server'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    return True


def delete_cert(params, my_output):   
    success = params['k8s_handler'].delete_certificate(
        params['__default__']['namespace'],  
        params['__default__']['certificate'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].delete_issuer(
        params['__default__']['namespace'], 
        params['__default__']['namespace'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_issuer(
        params['__default__']['namespace'], 
        params['__default__']['secret'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_certificate(
        params['__default__']['namespace'],  
        params['__default__']['certificate-admin'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False


    success = params['k8s_handler'].delete_certificate(
        params['__default__']['namespace'],  
        params['__default__']['certificate-remote'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_certificate(
        params['__default__']['namespace'],  
        params['__default__']['certificate-server'], 
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

    ocp_common.print_title(params, my_output, 'Disable')
    params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
    if params is None:
        return False
    
    if not params['k8s_handler'].is_cilium_mesh_enabled():
        my_output.default('Cluster mesh already disabled', before_newline=True)
    else:
        my_output.default('Cluster mesh will be disabled', before_newline=True)
        if not params['k8s_handler'].disable_cilium_mesh(my_output=my_output):
            return False

    if not delete_cert(params, my_output):
        return False
    
    if not delete_secret(params, my_output):
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Cluster mesh disabled')
    my_output.default('- Certificate manager resources deleted')
    my_output.default('- Root CA and certificate manager secrets deleted')

    return True
