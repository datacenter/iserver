from lib import output_helper
from lib.workflow.ocp_iotel import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'
    
    if 'wipe' not in params:
        params['wipe'] = False

    if not isinstance(params['wipe'], bool):
        return None, 'wipe param must be true or false'
    
    if 'suffix' not in params or params['suffix'] is None:
        params['suffix'] = None
        if not params['wipe']:
            return None, 'Suffix name required or select wipe mode'

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = False

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'suffix',
        'wipe',
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


def delete_instance(params, my_output):        
    success = params['k8s_handler'].delete_service_monitor(
        params['service_monitor_namespace'], 
        params['service_monitor_name'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].delete_service(
        params['service_namespace'], 
        params['service_name'], 
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_deployment(
        params['deployment_namespace'], 
        params['deployment_name'], 
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_config_map(
        params['intersight_config_namespace'], 
        params['intersight_config_name'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False
    
    success = params['k8s_handler'].delete_config_map(
        params['otel_config_namespace'], 
        params['otel_config_name'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_secret(
        params['secret_namespace'], 
        params['secret_name'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False
    
    if not params['delete-namespace']:
        return True
    
    used = params['k8s_handler'].check_namespace_usage_and_state(
        params['namespace'],
        my_output=my_output
    )
    if not used:
        success = params['k8s_handler'].delete_namespace(
            params['namespace'],
            check_usage=False,
            my_output=my_output,
            wait=True
        )
        if not success:
            return False

    return True


def wipe(params, my_output):
    for deployment in params['deployment']:
        success = params['k8s_handler'].delete_deployment(
            deployment['namespace'], 
            deployment['name'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False
        
    for secret in params['secret']:
        if secret['name'].startswith('intersight-'):
            success = params['k8s_handler'].delete_secret(
                secret['namespace'], 
                secret['name'], 
                my_output=my_output, 
                wait=True
            )
            if not success:
                return False

    for config_map in params['config_map']:
        if config_map['name'].startswith('intersight-'):
            success = params['k8s_handler'].delete_config_map(
                config_map['namespace'], 
                config_map['name'], 
                my_output=my_output, 
                wait=True
            )
            if not success:
                return False

    for service in params['service']:
        success = params['k8s_handler'].delete_service(
            service['namespace'], 
            service['name'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False

    for service_monitor in params['service_monitor']:
        success = params['k8s_handler'].delete_service_monitor(
            service_monitor['namespace'], 
            service_monitor['name'], 
            my_output=my_output, 
            wait=True
        )
        if not success:
            return False
        
    if not params['delete-namespace']:
        return True
    
    used = params['k8s_handler'].check_namespace_usage_and_state(
        params['namespace'],
        my_output=my_output
    )
    if not used:
        success = params['k8s_handler'].delete_namespace(
            params['namespace'],
            check_usage=False,
            my_output=my_output,
            wait=True
        )
        if not success:
            return False
        
    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Intersight Open Telemetry (iotel) - Delete Instance', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if params['wipe']:
        params = local_common.get_resources(params, my_output)
        if params is None:
            return False

        if not wipe(params, my_output):
            return False
    else:
        params = generate_names(params, my_output)
        if not delete_instance(params, my_output):
            return False

    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Service monitor deleted')
    my_output.default('- Service deleted')
    my_output.default('- Deployment deleted')
    my_output.default('- ConfigMap for intersight poller deleted')
    my_output.default('- ConfigMap for otel-collector deleted')
    my_output.default('- Secret with intersight authentication deleted')
    my_output.default('- Namespace deleted (if empty)')

    return True
