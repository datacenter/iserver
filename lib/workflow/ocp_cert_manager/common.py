import json
import copy
from lib.workflow.ocp_access import check as ocp_check
from lib.workflow import ocp_common


def initialize(params, my_output, log_id):
    params = augment_params(params)

    if params['verbose']:
        my_output.default('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        my_output.default(json.dumps(display_params, indent=4), after_newline=True)
    else:
        my_output.debug('Workflow Parameters', underline=True)
        display_params = copy.deepcopy(params)
        my_output.debug(json.dumps(display_params, indent=4), after_newline=True)

    ocp_check_params = {}
    ocp_check_params['cluster'] = params['cluster']
    ocp_check_params['mgmt-required'] = True
    ocp_check_params['cli-helm-check'] = True
    ocp_check_params['cli-helm-required'] = True
    ocp_check_params['verbose'] = params['check-verbose']
    ocp_params, errors = ocp_check.run(
        ocp_check_params,
        log_id=log_id
    )
    if errors is not None:
        my_output.error(errors)
        return None

    params['k8s_handler'] = ocp_params['data']['ocp_handler'].k8s_handler
    params['ssh_handler'] = ocp_common.get_management_node_ssh_handler(params['cluster'], log_id=log_id)
    return params


def get_default_params():
    params = {}
    params['namespace'] = 'cert-manager'
    params['helm'] = 'cert-manager'
    params['repo_name'] = 'jetstack'
    params['repo_url'] = 'https://charts.jetstack.io'
    return params


def augment_params(params):
    defaults = get_default_params()
    for key in defaults:
        params[key] = defaults[key]
    return params


def sanitize_params(params, allowed_keys):
    new_params = {}
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params


def is_repo(params, my_output):
    my_output.default('Check repo %s %s' % (params['repo_name'], params['repo_url']))    
    success, output, error = params['ssh_handler'].run_cmd(
        'helm repo ls'
    )
    if not success:
        if 'no repositories to show' in output or 'no repositories to show' in error:
            my_output.default('Not found')
            return False
                    
        my_output.error('Failed')
        my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
        return False
    
    if params['repo_name'] in output:
        my_output.default('Found')
        return True
    
    my_output.default('Not found')
    return False


def is_helm(params, my_output):
    my_output.default('Check helm chart %s' % (params['helm']))    
    success, output, error = params['ssh_handler'].run_cmd(
        'helm ls -A'
    )
    if not success:
        my_output.error('Failed')
        my_output.default('%s\n%s' % (str(output), str(error)), wrap='~~~')
        return False

    if params['helm'] in output:
        my_output.default('Found')
        return True

    my_output.default('Not found')
    return False

def get_crds(params):
    crd = {}
    crd['ready'] = params['k8s_handler'].is_custom_resource_definition('clusterissuers.cert-manager.io')
    crd['used'] = False
    if crd['ready']:
        crd['issuer'] = params['k8s_handler'].get_issuers(cache_enabled=False)
        if len(crd['issuer']) > 0:
            crd['used'] = True
        crd['certificate'] = params['k8s_handler'].get_certificates(cache_enabled=False)
        if len(crd['certificate']) > 0:
            crd['used'] = True

    return crd
