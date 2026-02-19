import os 
import base64
import yaml
from lib import output_helper
from lib import iaccount_helper
from lib import file_helper
from lib.workflow.ocp_iotel import common as local_common
from lib.workflow.ocp_prometheus import common as prometheus_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
        
    if 'key' not in params or params['key'] is None or len(params['key']) == 0:
        params['key'] = None

    if 'pem' not in params or params['pem'] is None or len(params['pem']) == 0:
        params['pem'] = None

    if 'iaccount' not in params or params['iaccount'] is None or len(params['iaccount']) == 0:
        params['iaccount'] = None

    if params['iaccount'] is None and params['key'] is None and params['pem'] is None:
        return None, 'iaccount name or key and pem required'

    if params['key'] is not None and params['pem'] is not None:
        params['iaccount'] = None

    if params['iaccount'] is None:
        if params['key'] is None:
            return None, 'Intersight key required'
        
        if params['pem'] is None:
            return None, 'Intersight pem required'
        
    if params['iaccount'] is not None:
        iaccount_handler = iaccount_helper.IntersightAccount()
        iaccount_configuration = iaccount_handler.get_iaccount_configuration(params['iaccount'])
        if iaccount_configuration is None:
            return None, 'Intersight account not found'

        params['key'] = iaccount_handler.get_iaccount_key(
            params['iaccount']
        )
        if params['key'] is None:
            return None, 'Key not found for iaccount %s' % (params['iaccount'])
        
        params['pem'] = iaccount_handler.get_iaccount_keyfile(
            params['iaccount']
        )
        if params['pem'] is None:
            return None, 'Pem file not found for iaccount %s' % (params['iaccount'])
    
    pem_filename = params['pem']
    if 'base_directory' in params:
        try:
            pem_filename = os.path.join(
                params['base_directory'],
                params['pem']
            )
        except BaseException:
            return None, 'Pem file path detection failed'
        
    params['private_key'] = file_helper.get_file_text(
        pem_filename
    )
    if params['private_key'] is None:
        return None, 'Pem file read failed'

    params['key_id'] = base64.b64encode(params['key'].encode('utf-8')).decode('utf-8')
    params['private_key'] = base64.b64encode(params['private_key'].encode('utf-8')).decode('utf-8')

    if 'suffix' not in params or params['suffix'] is None:
        if params['iaccount'] is None:
            return None, 'Resources base name required'
        
        params['suffix'] = params['iaccount']

    if 'pollers' not in params or params['pollers'] is None:
        params['pollers'] = None
        params['poller'] = 'otel_collector_endpoint = "http://127.0.0.1:4317"\n'

    if params['pollers'] is not None:
        pollers_filename = params['pollers']
        if 'base_directory' in params:
            try:
                pollers_filename = os.path.join(
                    params['base_directory'],
                    params['pollers']
                )
            except BaseException:
                return None, 'Pem file path detection failed'
            
        params['poller'] = file_helper.get_file_text(
            pollers_filename
        )
        if params['poller'] is None:
            return None, 'Pollers file read failed'

    if 'confirmation' not in params:
        params['confirmation'] = True

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'
    
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
        'iaccount',
        'key',
        'pem',
        'key_id',
        'private_key',
        'poller',
        'pollers',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def generate_names(params, my_output):
    my_output.default('Resources', underline=True, before_newline=True)

    my_output.default('namespace: %s' % (params['namespace']))

    params['secret_namespace'] = params['namespace']
    params['secret_name'] = params['secret-basename']
    if len(params['suffix']) > 0:
        params['secret_name'] = '%s-%s' % (params['secret_name'], params['suffix'])

    my_output.default('intersight-otel secret: %s/%s' % (params['secret_namespace'], params['secret_name']))

    params['secret_content'] = {}
    params['secret_content']['intersight-key'] = params['private_key']
    params['secret_content']['intersight-key-id'] = params['key_id']

    params['intersight_config_namespace'] = params['namespace']
    params['intersight_config_name'] = params['intersight-basename']
    if len(params['suffix']) > 0:
        params['intersight_config_name'] = '%s-%s' % (params['intersight_config_name'], params['suffix'])

    my_output.default('intersight-otel config map: %s/%s' % (params['intersight_config_namespace'], params['intersight_config_name']))
    
    params['otel_config_namespace'] = params['namespace']
    params['otel_config_name'] = params['otel-basename']
    if len(params['suffix']) > 0:
        params['otel_config_name'] = '%s-%s' % (params['otel_config_name'], params['suffix'])

    my_output.default('otel-collector config map: %s/%s' % (params['otel_config_namespace'], params['otel_config_name']))
    
    params['deployment_namespace'] = params['namespace']
    params['deployment_name'] = params['deployment-basename']
    if len(params['suffix']) > 0:
        params['deployment_name'] = '%s-%s' % (params['deployment_name'], params['suffix'])

    my_output.default('deployment: %s/%s' % (params['deployment_namespace'], params['deployment_name']))

    params['service_namespace'] = params['namespace']
    params['service_name'] = params['service-basename']
    if len(params['suffix']) > 0:
        params['service_name'] = '%s-%s' % (params['service_name'], params['suffix'])

    my_output.default('service: %s/%s' % (params['service_namespace'], params['service_name']))

    params['service_monitor_namespace'] = params['namespace']
    params['service_monitor_name'] = params['service-monitor-basename']
    if len(params['suffix']) > 0:
        params['service_monitor_name'] = '%s-%s' % (params['service_monitor_name'], params['suffix'])

    my_output.default('service monitor: %s/%s' % (params['service_monitor_namespace'], params['service_monitor_name']))

    return params


def get_otel_config():
    config = {}
    config['receivers'] = {}
    config['receivers']['otlp'] = {}
    config['receivers']['otlp']['protocols'] = {}
    config['receivers']['otlp']['protocols']['grpc'] = {}
    config['receivers']['otlp']['protocols']['http'] = {}
    
    config['processors'] = {}
    config['processors']['batch'] = {}
    config['processors']['memory_limiter'] = {}
    config['processors']['memory_limiter']['limit_mib'] = 1500
    config['processors']['memory_limiter']['spike_limit_mib'] = 512
    config['processors']['memory_limiter']['check_interval'] = '5s'

    config['extensions'] = {}
    config['extensions']['zpages'] = {}

    config['exporters'] = {}
    config['exporters']['prometheus'] = {}
    config['exporters']['prometheus']['endpoint'] = ':2112'
    config['exporters']['prometheus']['send_timestamps'] = True
    config['exporters']['prometheus']['metric_expiration'] = '180m'
    config['exporters']['prometheus']['enable_open_metrics'] = True
    config['exporters']['prometheus']['resource_to_telemetry_conversion'] = dict(enabled=True)

    config['service'] = {}
    config['service']['extensions'] = ['zpages']
    config['service']['pipelines'] = {}
    config['service']['pipelines']['metrics'] = {}
    config['service']['pipelines']['metrics']['receivers'] = ['otlp']
    config['service']['pipelines']['metrics']['processors'] = ['memory_limiter', 'batch']
    config['service']['pipelines']['metrics']['exporters'] = ['prometheus']

    # https://www.reddit.com/r/kubernetes/comments/1937dld/my_configmap_comes_out_in_this_scattered_yaml/
    return yaml.dump(config).replace('{}', '').replace(' \n', '\n')


def get_intersight_otel_body(params):
    container = {}
    container['name'] = 'intersight-otel'
    container['image'] = params['intersight-image']
    container['command'] = [
        '/target/release/intersight_otel',
        '-c',
        '/etc/intersight-otel/intersight-otel.toml'
    ]
    container['securityContext'] = params['k8s_handler'].get_deployment_secontext_body(
        escalation=False, 
        privileged=False, 
        ro_rootfs=True, 
        drop_all_caps=True
    )
    container['resources'] = params['k8s_handler'].get_deployment_resources_body(
        '100m',
        '200m',
        '64Mi',
        '128Mi'
    )

    container['env'] = []

    proxy = params['k8s_handler'].get_proxy()
    if proxy['https_proxy'] is not None:
        env = {}
        env['name'] = 'HTTPS_PROXY'
        env['value'] = proxy['https_proxy']
        container['env'].append(env)

    env = {}
    env['name'] = 'RUST_LOG'
    env['value'] = 'info'
    container['env'].append(env)

    env = {}
    env['name'] = 'intersight_otel_key_file'
    env['value'] = '/etc/intersight-otel-key/intersight.pem'
    container['env'].append(env)

    env = {}
    env['name'] = 'intersight_otel_key_id'
    env['valueFrom'] = {}
    env['valueFrom']['secretKeyRef'] = {}
    env['valueFrom']['secretKeyRef']['name'] = params['secret_name']
    env['valueFrom']['secretKeyRef']['key'] = 'intersight-key-id'
    container['env'].append(env)

    container['volumeMounts'] = []

    volume = {}
    volume['name'] = 'intersight-otel-config'
    volume['mountPath'] = '/etc/intersight-otel'
    volume['readyOnly'] = True
    container['volumeMounts'].append(volume)

    volume = {}
    volume['name'] = 'intersight-otel-key'
    volume['mountPath'] = '/etc/intersight-otel-key'
    volume['readyOnly'] = True
    container['volumeMounts'].append(volume)

    return container


def get_otel_collector_body(params):
    container = {}
    container['name'] = 'otel-collector'
    container['image'] = params['otel-image']
    container['command'] = [
        '/otelcol',
        '--config=/conf/otel-collector-config.yaml'
    ]
    container['resources'] = params['k8s_handler'].get_deployment_resources_body(
        '200m',
        '1',
        '400Mi',
        '2Gi'
    )
    container['ports'] = [
        dict(containerPort=4317),
        dict(containerPort=2112)
    ]
    container['volumeMounts'] = []
    volume = {}
    volume['name'] = 'otel-collector-config-vol'
    volume['mountPath'] = '/conf'
    container['volumeMounts'].append(volume)
    return container


def get_deployment_body(params):
    body = {}
    body['apiVersion'] = 'apps/v1'
    body['kind'] = 'Deployment'
    body['metadata'] = {}
    body['metadata']['namespace'] = params['deployment_namespace']
    body['metadata']['name'] = params['deployment_name']
    body['spec'] = {}
    body['spec']['selector'] = {}
    body['spec']['selector']['matchLabels'] = {}
    body['spec']['selector']['matchLabels']['app'] = params['deployment_name']
    body['spec']['template'] = {}
    body['spec']['template']['metadata'] = {}
    body['spec']['template']['metadata']['labels'] = {}
    body['spec']['template']['metadata']['labels']['app'] = params['deployment_name']
    body['spec']['template']['metadata']['labels']['component'] = 'otel-collector'

    volumes = []

    volume = {}
    volume['name'] = 'intersight-otel-config'
    volume['configMap'] = {}
    volume['configMap']['name'] = params['intersight_config_name']
    volumes.append(volume)

    volume = {}
    volume['name'] = 'intersight-otel-key'
    volume['secret'] = {}
    volume['secret']['secretName'] = params['secret_name']
    volume['secret']['items'] = []

    item = {}
    item['key'] = 'intersight-key'
    item['path'] = 'intersight.pem'
    volume['secret']['items'].append(item)
    volumes.append(volume)

    volume = {}
    volume['name'] = 'otel-collector-config-vol'
    volume['configMap'] = {}
    volume['configMap']['name'] = params['otel_config_name']
    volume['configMap']['items'] = []

    item = {}
    item['key'] = 'otel-collector-config'
    item['path'] = 'otel-collector-config.yaml'
    volume['configMap']['items'].append(item)
    volumes.append(volume)

    body['spec']['template']['spec'] = {}
    body['spec']['template']['spec']['containers'] = [
        get_intersight_otel_body(params),
        get_otel_collector_body(params)
    ]
    body['spec']['template']['spec']['volumes'] = volumes
    return body


def get_service_body(params):
    body = params['k8s_handler'].get_service_base_body(
        params['service_namespace'], 
        params['service_name'], 
        labels=dict(
            app=params['deployment_name'],
            component='otel-collector'
        )
    )
    body['spec']['ports'] = [dict(name='prometheus-exporter', port=2112)]
    body['spec']['selector'] = dict(
        app=params['deployment_name'],
        component='otel-collector'
    )
    return body


def get_service_monitor_body(params):
    body = params['k8s_handler'].get_service_monitor_base_body(
        params['service_monitor_namespace'], 
        params['service_monitor_name'], 
        labels=dict(
            app=params['deployment_name'],
            component='otel-collector'
        )
    )
    endpoint = {}
    endpoint['interval'] = '30s'
    endpoint['port'] = 'prometheus-exporter'
    endpoint['scheme'] = 'http'
    endpoint['path'] = '/metrics'
    body['spec']['endpoints'].append(endpoint)
    return body


def create_instance(params, my_output):        
    success = params['k8s_handler'].create_namespace(
        params['namespace'],
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].create_secret_kv(
        params['secret_namespace'], 
        params['secret_name'],
        params['secret_content'], 
        secret_type='Opaque',
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    labels = {}
    labels['app'] = 'opentelemetry'
    labels['component'] = 'otel-collector-config'

    success = params['k8s_handler'].create_config_map_data(
        params['otel_config_namespace'], 
        params['otel_config_name'],
        'otel-collector-config', 
        get_otel_config(),
        labels=labels,
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].create_config_map_data(
        params['intersight_config_namespace'], 
        params['intersight_config_name'],
        'intersight-otel.toml', 
        params['poller'],
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].create_deployment(
        params['deployment_namespace'], 
        params['deployment_name'], 
        get_deployment_body(params),
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].create_service(
        params['service_namespace'], 
        params['service_name'], 
        get_service_body(params),
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].create_service_monitor(
        params['service_monitor_namespace'], 
        params['service_monitor_name'], 
        get_service_monitor_body(params),
        confirmation=params['confirmation'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False
    
    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Intersight Open Telemetry (iotel) - Create Instance', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not prometheus_common.check_user_workload_monitoring(params, my_output):
        return False
    
    params = generate_names(params, my_output)

    success = params['k8s_handler'].is_deployment(
        params['deployment_namespace'], 
        params['deployment_name'],
        cache_enabled=False
    )
    if success:
        my_output.default('Instance already exists')
        return True
    
    if not create_instance(params, my_output):
        return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Namespace created')
    my_output.default('- Secret with intersight authentication ready')
    my_output.default('- ConfigMap for otel-collector ready')
    my_output.default('- ConfigMap for intersight poller ready')
    my_output.default('- Deployment ready')
    my_output.default('- Service created')
    my_output.default('- Service monitor ready with prometheus target')

    return True
