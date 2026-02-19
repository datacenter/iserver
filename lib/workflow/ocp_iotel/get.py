from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_iotel import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'suffix' not in params:
        params['suffix'] = None

    if 'poller' not in params:
        params['poller'] = False

    if not isinstance(params['poller'], bool):
        return None, 'poller param must be true or false'
            
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
        'suffix',
        'poller',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def get_info(params, my_output):
    params = local_common.get_resources(params, my_output)
    if params is None:
        return None
    
    params['instance'] = []
    for deployment in params['deployment']:
        instance = {}
        instance['__Output'] = {}
        instance['namespace'] = deployment['namespace']
        instance['name'] = deployment['name']
        instance['namespace_name'] = deployment['namespace_name']
        instance['namespace_nameT'] = deployment['namespace_nameT']
        instance['readyT'] = deployment['readyT']
        instance['__Output']['readyT'] = deployment['__Output']['readyT']

        instance['suffix'] = deployment['name'].split('-')[1]
        if params['suffix'] is not None and instance['suffix'] != params['suffix']:
            continue

        instance['secret'] = None
        instance['intersightTick'] = '\u2717'
        instance['__Output']['intersightTick'] = 'Red'
        for secret in params['secret']:
            if secret['name'] == 'intersight-%s' % (instance['suffix']):
                instance['secret'] = secret
                instance['intersightTick'] = '\u2713'
                instance['__Output']['intersightTick'] = 'Green'

        instance['poller'] = None
        instance['pollerCount'] = 0
        instance['metric'] = []
        instance['pollerTick'] = '\u2717'
        instance['__Output']['pollerTick'] = 'Red'
        for config_map in params['config_map']:
            if config_map['name'] == 'intersight-%s' % (instance['suffix']):
                try:
                    instance['poller'] = config_map['data']['intersight-otel.toml']
                    for line in instance['poller'].split('\n'):
                        if '[[pollers]]' in line:
                            instance['pollerCount'] += 1

                        if '[[tspollers]]' in line:
                            instance['pollerCount'] += 1

                        if len(line.split('name = ')) == 2 and len(line.split('name = ')[0]) == 0:
                            metric_name = line.split('name = ')[1].replace('"', '')
                            if metric_name not in instance['metric']:
                                instance['metric'].append(
                                    metric_name
                                )

                    instance['pollerTick'] = '\u2713'
                    instance['__Output']['pollerTick'] = 'Green'
                except BaseException:
                    pass

        instance['metricCount'] = len(instance['metric'])
        instance['service'] = None
        instance['serviceTick'] = '\u2717'
        instance['__Output']['serviceTick'] = 'Red'
        for service in params['service']:
            if service['name'] == 'otel-%s' % (instance['suffix']):
                instance['service'] = service
                if len(service['podT']) > 0:
                    instance['serviceTick'] = '\u2713'
                    instance['__Output']['serviceTick'] = 'Green'

        instance['service_monitor'] = None
        instance['serviceMonitorTick'] = '\u2717'
        instance['__Output']['serviceMonitorTick'] = 'Red'
        for service_monitor in params['service_monitor']:
            if service_monitor['name'] == 'otel-%s' % (instance['suffix']):
                instance['service_monitor'] = service_monitor
                instance['serviceMonitorTick'] = '\u2713'
                instance['__Output']['serviceMonitorTick'] = 'Green'

        params['instance'].append(instance)

    return params


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Intersight Open Telemetry (iotel) - Get instance', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not params['k8s_handler'].is_namespace(params['namespace']):
        my_output.default('No namespace [%s]' % (params['namespace']))
        return True
    
    params = get_info(params, my_output)
    if params is None:
        return False

    k8s_output_handler.my_table(
        params['instance'],
        [
            ['Deployment', 'namespace_nameT'],
            ['Ready', 'readyT'],
            ['Suffix', 'suffix'],
            ['Intersight API', 'intersightTick'],
            ['Poller', 'pollerTick'],
            ['Query', 'pollerCount'],
            ['Metric', 'metric'],
            ['OTEL Service', 'serviceTick'],
            ['Service Monitor', 'serviceMonitorTick'],
        ]
    )

    if params['poller'] or params['verbose']:
        for instance in params['instance']:
            my_output.default('Instance: %s' % (instance['suffix']), before_newline=True, underline=True)
            my_output.default(instance['poller'])

    if params['verbose']:
        k8s_output_handler.print_secrets(params['secrets'])
        k8s_output_handler.print_config_maps(params['config_maps'])
        k8s_output_handler.print_deployments(params['deployments'])
        k8s_output_handler.print_pods_state(params['pods'])
        k8s_output_handler.print_services(params['services'])
        k8s_output_handler.print_service_monitors(params['service_monitors'])

    my_output.default('Output option: --poller, --verbose', before_newline=True)
    return True
