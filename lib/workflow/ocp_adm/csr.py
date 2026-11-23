from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_adm import common as local_common
from lib.workflow import ocp_common
from menu.common import get_confirmation


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['name', True, None, 'str', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Approve CSR')
    params = ocp_common.workflow_init(params, my_output, log_id)
    if params is None:
        return False

    if params['name'] is not None:
        csr = params['k8s_handler'].get_csrs(
            object_filter=['name:%s' % (params['name'])]
        )
    else:
        csr = params['k8s_handler'].get_csrs()
        
    if csr is None:
        my_output.error('Failed to get csr')
        return False

    if len(csr) == 0:
        my_output.default('No csr. Nothing to do.')
        return True
    
    k8s_output_handler.print_csrs_state(csr)

    if params['confirmation']:
        if not get_confirmation():
            return True

    for item in csr:
        k8s_output_handler.print_csr(item)
        if not item['pending']:
            my_output.default('CSR is not in pending state and was already approved')
            continue

        success = params['k8s_handler'].approve_csr_mo(item['name'])
        if not success:
            return False

        if params['wait']:
            success = params['k8s_handler'].wait_certificate_issued(item['name'], my_output=my_output)
            if not success:
                return False

        new_csr = csr = params['k8s_handler'].get_csr(
            item['name'],
            cache_enabled=False
        )
        if new_csr is None:
            my_output.error('CSR not found after approval')
            return False

        my_output.default('')
        k8s_output_handler.print_csr_certificate(new_csr)
        
    return True