import copy
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.linux import output as linux_output
from lib.workflow.ocp_cert_manager import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'list-of-str', None, None, None, None],
        ['view', True, ['state'], 'view', None, None, ['state', 'res'], None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(mparams, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    linux_output_handler = linux_output.LinuxOutput(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    mparams, error = validate(mparams)
    if error is not None:
        my_output.error(error)
        return False
    
    for cluster in mparams['cluster']:
        params = copy.deepcopy(mparams)
        params['cluster'] = cluster

        ocp_common.print_title(params, my_output, 'Get Information')
        params = ocp_common.workflow_init(params, my_output, log_id, ssh_required=True, helm_required=True, linux_required=True)
        if params is None:
            continue

        params = local_common.collect_state_info(params)

        if 'state' in params['view']:
            local_common.print_state(params, my_output, linux_output_handler)

        if 'res' in params['view']:
            local_common.print_resource_summary(params, my_output)
            local_common.print_resources(params, k8s_output_handler)

    return True