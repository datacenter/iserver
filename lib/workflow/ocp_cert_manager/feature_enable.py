from lib import output_helper
from lib.linux import output as linux_output
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


def add_repo(params, my_output):
    my_output.default('Add repo %s %s' % (params['__default__']['repo_name'], params['__default__']['repo_url']))
    success, output, error = params['ssh_handler'].run_cmd(
        'helm repo add %s %s' % (params['__default__']['repo_name'], params['__default__']['repo_url'])
    )
    my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
    if not success:
        my_output.error('Failed')
        return False
    
    my_output.default('Helm repo added')
    return True


def add_helm(params, my_output):
    my_output.default('Install %s/%s' % (params['__default__']['repo_name'], params['__default__']['helm']))
    success, output, error = params['ssh_handler'].run_cmd(
        'helm install %s %s/%s --namespace %s --create-namespace --set crds.enabled=true' % (
            params['__default__']['helm'],
            params['__default__']['repo_name'],
            params['__default__']['helm'],
            params['__default__']['namespace']
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
    linux_output_handler = linux_output.LinuxOutput(log_id=log_id)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Install')
    params = ocp_common.workflow_init(params, my_output, log_id, ssh_required=True, linux_required=True)
    if params is None:
        return False

    params = local_common.collect_state_info(params, resource=False)

    if params['state']['repo'] is None:
        success = add_repo(params, my_output)
        if not success:
            return False
        
    if params['state']['chart'] is None:
        success = add_helm(params, my_output)
        if not success:
            return False

    params = local_common.collect_state_info(params)
    local_common.print_state(params, my_output, linux_output_handler)

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- certificate manager installed')
    return True
