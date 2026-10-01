import json
import copy
from lib.workflow.ocp_access import check as ocp_check


def get_default_params():
    params = {}
    params['namespace'] = 'intersight-otel'
    params['deployment-basename'] = 'instance'
    params['secret-basename'] = 'intersight'
    params['intersight-basename'] = 'intersight'
    params['otel-basename'] = 'otel'
    params['service-basename'] = 'otel'
    params['service-monitor-basename'] = 'otel'
    params['intersight-image'] = 'ghcr.io/cgascoig/intersight-otel:v0.1.2'
    params['otel-image'] = 'otel/opentelemetry-collector:0.59.0'
    params['delete-namespace'] = True
    params['title'] = 'Intersight Open Telemetry (iotel)'
    return params


def get_resources(params, my_output):
    my_output.default('Collect resources in namespace %s' % (params['__default__']['namespace']), before_newline=True)

    my_output.default('- deployment')
    params['deployment'] = params['k8s_handler'].get_deployments(
        object_filter=['namespace:%s' % (params['__default__']['namespace'])]
    )
    if params['deployment'] is None:
        my_output.error('deployments rest api failed')
        return None

    my_output.default('- pod')
    params['pod'] = params['k8s_handler'].get_pods(
        object_filter=['namespace:%s' % (params['__default__']['namespace'])],
        service_info=True
    )
    if params['pod'] is None:
        my_output.error('pods rest api failed')
        return None
    
    my_output.default('- secret')
    params['secret'] = params['k8s_handler'].get_secrets(
        object_filter=['namespace:%s' % (params['__default__']['namespace'])]
    )
    if params['secret'] is None:
        my_output.error('secrets rest api failed')
        return None
    
    my_output.default('- config map')
    params['config_map'] = params['k8s_handler'].get_config_maps(
        object_filter=['namespace:%s' % (params['__default__']['namespace'])]
    )
    if params['config_map'] is None:
        my_output.error('config maps rest api failed')
        return None
    
    my_output.default('- service')
    params['service'] = params['k8s_handler'].get_services(
        object_filter=['namespace:%s' % (params['__default__']['namespace'])],
        endpoint_info=True
    )
    if params['service'] is None:
        my_output.error('services rest api failed')
        return None
    
    my_output.default('- service monitor')
    params['service_monitor'] = params['k8s_handler'].get_service_monitors(
        object_filter=['namespace:%s' % (params['__default__']['namespace'])],
        endpoint_info=True, 
        target_info=True
    )
    if params['service_monitor'] is None:
        my_output.error('service monitors rest api failed')
        return None

    return params


def get_instances(params, my_output):
    my_output.default('Collect resources')

    my_output.default('- deployment')
    params['deployment'] = params['k8s_handler'].get_deployments(
        object_filter=['namespace:%s' % (params['__default__']['namespace'])]
    )
    if params['deployment'] is None:
        my_output.error('deployments rest api failed')
        return None

    my_output.default('- secret')
    secrets = params['k8s_handler'].get_secrets(
        object_filter=['namespace:%s' % (params['__default__']['namespace'])]
    )
    if secrets is None:
        my_output.error('secrets rest api failed')
        return None
    
    my_output.default('- config map')
    config_maps = params['k8s_handler'].get_config_maps(
        object_filter=['namespace:%s' % (params['__default__']['namespace'])]
    )
    if config_maps is None:
        my_output.error('config maps rest api failed')
        return None

    params['instance'] = []
    for deployment in params['deployment']:
        instance = {}
        instance['__Output'] = {}
        instance['namespace'] = deployment['namespace']
        instance['name'] = deployment['name']
        instance['suffix'] = deployment['name'].split('-')[1]
        if params['suffix'] is not None and instance['suffix'] != params['suffix']:
            continue

        instance['intersight_config_namespace'] = None
        instance['intersight_config_name'] = None
        instance['poller'] = None
        for config_map in config_maps:
            if config_map['name'] == 'intersight-%s' % (instance['suffix']):
                instance['intersight_config_namespace'] = config_map['namespace']
                instance['intersight_config_name'] = config_map['name']
                try:
                    instance['poller'] = config_map['data']['intersight-otel.toml']
                except BaseException:
                    pass

        instance['intersight_key'] = None
        instance['intersight_pem'] = None
        for secret in secrets:
            if secret['name'] == 'intersight-%s' % (instance['suffix']):
                instance['intersight_key'] = secret['data']['intersight-key-id']
                instance['intersight_pem'] = secret['data']['intersight-key']

        params['instance'].append(instance)

    return params