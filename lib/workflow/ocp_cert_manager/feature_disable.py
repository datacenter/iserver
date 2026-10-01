from lib import output_helper
from lib.workflow.ocp_cert_manager import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['wipe', False, True, 'bool', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def cleanup_cert_manager(params, my_output):
    local_common.print_resource_summary(params, my_output)
    if not params['state']['resources']:
        return True
    
    if not params['wipe']:
        my_output.error('Certificate manager crds exist. Clean it up or re-run with --wipe option')
        return False

    success = params['k8s_handler'].wipe_certificates(my_output=my_output, wait=True)
    if not success:
        return False
    
    success = params['k8s_handler'].wipe_issuers(my_output=my_output, wait=True)
    if not success:
        return False

    return True


def uninstall_helm(params, my_output):
    my_output.default('Uninstall helm %s' % (params['__default__']['helm']))

    success, output, error = params['ssh_handler'].run_cmd(
        'helm uninstall %s --namespace %s' % (
            params['__default__']['helm'],
            params['__default__']['namespace']
        )
    )
    if not success:
        my_output.error('Failed')
        my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
        return False
    
    my_output.default('Helm uninstalled')
    return True


def delete_repo(params, my_output):
    my_output.default('Remove helm repo %s' % (params['__default__']['repo_name']))
    success, output, error = params['ssh_handler'].run_cmd(
        'helm repo remove %s' % (params['__default__']['repo_name'])
    )
    if not success:
        my_output.error('Failed')
        my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
        return False
    
    my_output.default('Helm repo removed')
    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Uninstall')
    params = ocp_common.workflow_init(params, my_output, log_id, ssh_required=True, linux_required=True)
    if params is None:
        return False
    
    params = local_common.collect_state_info(params)

    success = cleanup_cert_manager(params, my_output)
    if not success:
        return False
    
    if params['state']['chart'] is not None:
        success = uninstall_helm(params, my_output)
        if not success:
            return False

    if params['state']['repo'] is not None:
        success = delete_repo(params, my_output)
        if not success:
            return False

    if params['k8s_handler'].is_namespace(params['__default__']['namespace']):
        success = params['k8s_handler'].delete_namespace(
            params['__default__']['namespace'],
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