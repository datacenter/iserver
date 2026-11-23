def get_default_params():
    params = {}
    params['namespace'] = 'aistor'
    params['name'] = 'minio-object-store-operator'
    params['operator-group-name'] = 'minio-operator-group'
    params['delete-namespace'] = True
    params['create_subscription'] = 'create_minio_subscription'
    params['delete_subscription'] = 'delete_minio_subscription'
    params['resource_keys'] = [
        'admin_job',
        'policy_binding',
        'object_store'
    ]
    params['resource_output'] = [
        ['admin job', 'admin_job'],
        ['policy binding', 'policy_binding'],
        ['object store', 'object_store']
    ]
    params['title'] = 'OpenShift Workflow - MinIO Operator'
    return params


def collect_state_info(params, my_output):
    params['summary']['resources'] = False

    for key in params['__default__']['resource_keys']:
        my_output.debug('- %s' % (key.replace('_', ' ')))
        params[key] = getattr(params['k8s_handler'], 'get_%ss' % (key))(cache_enabled=False)

    for key in params['__default__']['resource_keys']:
        params['summary'][key] = '---'
        if params[key] is not None:
            params['summary'][key] = len(params[key])
            if len(params[key]) > 0:
                params['summary']['resources'] = True

    return params


def wipe(params, my_output):
    for key in params['__default__']['resource_keys']:
        if params[key] is not None:
            if len(params[key]) > 0:
                success = getattr(
                    params['k8s_handler'],
                    'delete_%s' % (key)
                )(
                    my_output=my_output,
                    wait=True
                )
                if not success:
                    return False

    return True