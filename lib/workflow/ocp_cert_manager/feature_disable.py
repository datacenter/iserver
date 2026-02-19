from lib import output_helper
from lib.workflow.ocp_cert_manager import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'wipe' not in params:
        params['wipe'] = True

    if not isinstance(params['wipe'], bool):
        return None, 'wipe param must be true or false'
      
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
        'wipe',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None

def cleanup_cert_manager(params, my_output):
    my_output.default('Check cluster manager crds...')
    crd = local_common.get_crds(params)
    if not crd['ready']:
        my_output.default('- crd not available')
        return True
    
    my_output.default('- Issuer CRD [#%s]' % (len(crd['issuer'])))
    my_output.default('- Certificate CRD [#%s]' % (len(crd['certificate'])))

    if crd['used']:
        if not params['wipe']:
            my_output.error('Certificate manager crds exist. Clean it up or re-run with --wipe option')
            return False
    
        success = params['k8s_handler'].wipe_certificates()
        if not success:
            my_output.error('Failed to wipe certificates')
            return False
        
        success = params['k8s_handler'].wipe_issuers()
        if not success:
            my_output.error('Failed to wipe issuers')
            return False

    return True

def uninstall_helm(params, my_output):
    my_output.default('Uninstall helm %s' % (params['helm']))

    success, output, error = params['ssh_handler'].run_cmd(
        'helm uninstall %s --namespace %s' % (
            params['helm'],
            params['namespace']
        )
    )
    if not success:
        my_output.error('Failed')
        my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
        return False
    
    my_output.default('Helm installed')
    return True


def delete_repo(params, my_output):
    my_output.default('Remove helm repo %s' % (params['repo_name']))
    success, output, error = params['ssh_handler'].run_cmd(
        'helm repo remove %s' % (params['repo_name'])
    )
    if not success:
        my_output.error('Failed')
        my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
        return False
    
    my_output.default('Helm repo removed')
    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Certificate Manager - Uninstall', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
    success = cleanup_cert_manager(params, my_output)
    if not success:
        return False
    
    if local_common.is_helm(params, my_output):
        success = uninstall_helm(params, my_output)
        if not success:
            return False

    if local_common.is_repo(params, my_output):
        success = delete_repo(params, my_output)
        if not success:
            return False

    if params['k8s_handler'].is_namespace(params['namespace']):
        success = params['k8s_handler'].delete_namespace(
            params['namespace'],
            my_output=my_output,
            wait=True
        )
        if not success:
            return False
        
    my_output.default('')
    my_output.default('Completed tasks')
    if params['wipe']:
        my_output.default('- resources wiped')
    my_output.default('- helm uninstalled')
    my_output.default('- helm repo removed')
    my_output.default('- namespace deleted')

    return True
