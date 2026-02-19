import json
from lib import output_helper
from lib.workflow.ocp_access import check as ocp_check
from lib.k8s import output as k8s_output
from lib.workflow.ocp_prometheus import common as local_common


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
    
    new_params = {}
    allowed_keys = [
        'cluster',
        'verbose',
        'check-verbose'
    ]
    for key in params:
        if key in allowed_keys:
            new_params[key] = params[key]

    return new_params, None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Prometheus - Get Information', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
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
