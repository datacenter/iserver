import yaml
from lib import filter_helper
from lib import output_helper
from lib.workflow.ocp_tetragon_operator import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'check-verbose' not in params:
        params['check-verbose'] = True

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'

    allowed_keys = [
        'cluster',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def disable_service_monitoring(params, my_output):
    managed_object, config = local_common.get_operator_config(params, my_output)
    if managed_object is None:
        return False
    
    if 'serviceMonitorEnabled' not in config:
        my_output.error('Unsupported content of config map: no serviceMonitorEnabled property found in agentDaemonSet')
        return False

    if config['serviceMonitorEnabled'] and not config['serviceMonitorEnabled']:
        my_output.default('serviceMonitorEnabled already set to false')
        return True
    
    my_output.default('serviceMonitorEnabled will be set to false')

    managed_object['data']['agentDaemonSet'] = managed_object['data']['agentDaemonSet'].replace('serviceMonitorEnabled: true', 'serviceMonitorEnabled: false')
    if not local_common.update_operator_config(managed_object['data'], params, my_output):
        return False
    
    service_monitors = [
        {'namespace': params['sm-namespace'], 'name': params['sm-name']}
    ]
    success = params['k8s_handler'].wait_no_service_monitors(service_monitors, my_output=my_output)
    if not success:
        my_output.default('Fallback service monitor delete mode...')

        if not params['k8s_handler'].delete_service_monitor_mo(params['sm-namespace'], params['sm-name']):
            my_output.error('REST API failed')
            return False
    
    return params


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Tetragon Operator - Enable Prometheus Service Monitor', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if params is None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not params['k8s_handler'].is_tetragon_subscription(params['namespace'], params['name']):
        my_output.default('Tetragon Operator not installed')
        return False
    
    if not disable_service_monitoring(params, my_output):
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Tetragon service monitors disabled')

    return True
