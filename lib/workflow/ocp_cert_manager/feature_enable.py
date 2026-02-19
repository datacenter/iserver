from lib import output_helper
from lib.workflow.ocp_cert_manager import common as local_common


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


def add_repo(params, my_output):
    my_output.default('Add repo %s %s' % (params['repo_name'], params['repo_url']))
    success, output, error = params['ssh_handler'].run_cmd(
        'helm repo add %s %s' % (params['repo_name'], params['repo_url'])
    )
    my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
    if not success:
        my_output.error('Failed')
        return False
    
    my_output.default('Helm repo added')
    return True


def add_helm(params, my_output):
    my_output.default('Install %s/%s' % (params['repo_name'], params['helm']))
    success, output, error = params['ssh_handler'].run_cmd(
        'helm install %s %s/%s --namespace %s --create-namespace --set crds.enabled=true' % (
            params['helm'],
            params['repo_name'],
            params['helm'],
            params['namespace']
        )
    )
    my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
    if not success:
        my_output.error('Failed')
        return False
    
    my_output.default('Helm installed')
    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Certificate Manager - Install', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_repo(params, my_output):
        success = add_repo(params, my_output)
        if not success:
            return False
        
    if not local_common.is_helm(params, my_output):
        success = add_helm(params, my_output)
        if not success:
            return False

    crds = local_common.get_crds(params)
    if not crds['ready']:
        my_output.error('Failed to get crds')
        return False
    
    my_output.default('CRDs found')

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- certificate manager installed')

    return True
