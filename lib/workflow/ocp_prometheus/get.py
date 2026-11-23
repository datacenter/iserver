import copy
import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.k8s import output as k8s_output
from lib.workflow.ocp_prometheus import common as local_common
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
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)

    mparams, error = validate(mparams)
    if error is not None:
        my_output.error(error)
        return False
    
    for cluster in mparams['cluster']:
        params = copy.deepcopy(mparams)
        params['cluster'] = cluster

        ocp_common.print_title(params, my_output, 'Get Information')
        params = ocp_common.workflow_init(params, my_output, log_id)
        if params is None:
            continue
    
        local_common.check_user_workload_monitoring(params, my_output)

        my_output.default('Targets', before_newline=True, underline=True)
        platform = params['k8s_handler'].get_prometheus_targets(object_filter=['type:P'])
        if platform is None:
            my_output.error('Failed to get platform metrics')
        else:
            ready = 0
            for item in platform:
                if item['ready']:
                    ready += 1

            my_output.default('- platform targets: %s/%s' % (ready, len(platform)))
        
        user = params['k8s_handler'].get_prometheus_targets(object_filter=['type:U'])
        if user is None:
            my_output.default('- no user targets')
        else:
            ready = 0
            for item in user:
                if item['ready']:
                    ready += 1

            my_output.default('- user targets: %s/%s' % (ready, len(user)))

    return True
