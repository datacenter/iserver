from lib import output_helper
from lib.workflow.ocp_cilium_mesh import common as local_common
from lib.workflow.ocp_cilium_cni import common as cilium_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
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
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def delete_secret(params, my_output):
    success = params['k8s_handler'].delete_secret(
        params['namespace'], 
        params['secret'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_secret(
        params['namespace'], 
        params['certificate'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].delete_secret(
        params['namespace'], 
        params['certificate-admin'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_secret(
        params['namespace'], 
        params['certificate-remote'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].delete_secret(
        params['namespace'], 
        params['certificate-server'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    return True


def delete_cert(params, my_output):   
    success = params['k8s_handler'].delete_certificate(
        params['namespace'],  
        params['certificate'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].delete_issuer(
        params['namespace'], 
        params['namespace'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_issuer(
        params['namespace'], 
        params['secret'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_certificate(
        params['namespace'],  
        params['certificate-admin'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False


    success = params['k8s_handler'].delete_certificate(
        params['namespace'],  
        params['certificate-remote'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_certificate(
        params['namespace'],  
        params['certificate-server'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False

    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Disable Cluster Mesh', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not cilium_common.is_cilium(params, my_output):
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
