from menu.common import get_confirmation


def get_default_params():
    params = {}
    params['namespace'] = 'openshift-mtv'
    params['name'] = 'mtv-operator'
    params['operator-group-name'] = 'mtv-operator-group'
    params['delete-namespace'] = True
    params['create_subscription'] = 'create_mtv_subscription'
    params['delete_subscription'] = 'delete_mtv_subscription'
    params['resource_keys'] = [
        'provider',
        'network_map',
        'storage_map',
        'plan',
        'migration'
    ]
    params['resource_output'] = [
        ['provider', 'provider'],
        ['network map', 'network_map'],
        ['storage map', 'storage_map'],
        ['plan', 'plan'],
        ['migration', 'migration']
    ]
    params['title'] = 'OpenShift Workflow - Migration Toolkit for Virtualization Operator'
    return params


def collect_state_info(params, my_output):
    params['summary']['ready'] = params['k8s_handler'].is_subscription_mtv_ready()
    params['summary'] = params['k8s_handler'].add_tick(
        params['summary'],
        'ready',
        True,
        'readyTick'
    )

    params['instance'] = {}
    params['instance']['__Output'] = {}
    params['instance']['readyTick'] = '\u2717'
    params['instance']['__Output']['readyTick'] = 'Red'
    
    instances = params['k8s_handler'].get_forklift_controllers(cache_enabled=False)
    if instances is not None and len(instances) == 1:
        params['instance'] = instances[0]
        params['instance'] = params['k8s_handler'].add_tick(
            params['instance'],
            'ready',
            True,
            'readyTick'
        )
    
    params['summary']['resources'] = False

    for key in params['__default__']['resource_keys']:
        my_output.debug('- %s' % (key.replace('_', ' ')))
        params[key] = getattr(params['k8s_handler'], 'get_%ss' % (key))(all_info=True, cache_enabled=False)

    for key in params['__default__']['resource_keys']:
        params['summary'][key] = '---'
        if params[key] is not None:
            params['summary'][key] = len(params[key])
            if len(params[key]) > 0:
                params['summary']['resources'] = True

    return params


def is_subscription_ready(params, my_output, details=False):
    subscription = params['k8s_handler'].get_subscription_by_package(
        params['__default__']['name'],
        return_mo=False,
        cache_enabled=False
    )
    if subscription is None:
        my_output.default('Mtv operator %s' % (my_output.add_color('not installed', 'Red')))
        return False

    if details:
        my_output.default('Mtv Operator', before_newline=True)
        my_output.default('- subscription: %s' % (subscription['namespace_name']))
        my_output.default('- channel: %s' % (subscription['channel']))
        my_output.default('- csv: %s' % (subscription['installed_csv']))
        if not params['k8s_handler'].is_subscription_mtv_ready():
            my_output.default('- %s' % (my_output.add_color('not ready', 'Red')))
            return False
            
        my_output.default('- %s' % (my_output.add_color('ready', 'Green')))
        return True
    
    my_output.default('Mtv operator %s' % (my_output.add_color('installed', 'Green')))

    if not params['k8s_handler'].is_subscription_mtv_ready():
        my_output.default('Mtv operator %s' % (my_output.add_color('not ready', 'Red')), before_newline=True)
        return False
        
    my_output.default('Mtv operator %s' % (my_output.add_color('ready', 'Green')), before_newline=True)
    return True


def is_instance_ready(params, my_output):
    instances = params['k8s_handler'].get_forklift_controllers(cache_enabled=False)
    if instances is None:
        my_output.error('Failed to get forklift instances')
        return False
    
    my_output.default('Mtv Forklift Controller', before_newline=True)

    if len(instances) == 0:
        my_output.default('- no instance found')
        return False
    
    if len(instances) > 1:
        my_output.default('- %s multiple instances found' % (my_output.add_color('unexpected', 'Red')))
        return False
    
    my_output.default('- namespace: %s' % (instances[0]['namespace']))
    my_output.default('- name: %s' % (instances[0]['name']))
    if instances[0]['ready']:
        my_output.default('- %s' % (my_output.add_color('ready', 'Green')))
    else:
        my_output.default('- %s' % (my_output.add_color('not ready', 'Red')))

    return True


def select_migration_plans(params, my_output, k8s_output_handler):
    object_filter = []
    if not params['wipe']:
        if params['namespace'] is not None:
            object_filter.append('namespace:%s' % (params['namespace']))
        if params['name'] is not None:
            object_filter.append('name:%s' % (params['name']))

    migration_plans = params['k8s_handler'].get_plans(
        object_filter=object_filter,
        nmap_info=True,
        smap_info=True        
    )
    if migration_plans is None:
        my_output.error('Failed to get migration plans', before_newline=True)
        return False, None
    
    if len(migration_plans) == 0:
        my_output.default('No migration plan found', before_newline=True)
        return True, None
    
    k8s_output_handler.print_plans_state(migration_plans)

    if params['confirmation']:
        if not get_confirmation():
            return False, None

    return True, migration_plans


def is_mtv_unconfigured(params, my_output, k8s_output_handler):
    providers = params['k8s_handler'].get_providers(
        storage_info=True, 
        network_info=True,
        plan_info=True,
        skip_host=True,
        cache_enabled=False
    )
    if providers is None:
        my_output.default('Failed to get provider', before_newline=True)
        return False

    if len(providers) > 0:
        k8s_output_handler.print_providers_state(providers)
        my_output.error('Delete providers first')
        return False
    
    my_output.default('No providers found', before_newline=True)

    maps = params['k8s_handler'].get_network_maps(
        plan_info=True, 
        cache_enabled=False
    )
    if maps is None:
        my_output.error('Failed to get network maps')
        return False
    
    if len(maps) > 0:
        k8s_output_handler.print_network_maps_state(maps)
        my_output.error('Delete network maps first')
        return False

    my_output.default('No network maps found', before_newline=True)

    maps = params['k8s_handler'].get_storage_maps(
        plan_info=True, 
        cache_enabled=False
    )
    if maps is None:
        my_output.error('Failed to get storage maps')
        return False

    if len(maps) > 0:
        k8s_output_handler.print_storage_maps_state(maps)
        my_output.error('Delete storage maps first')
        return False

    my_output.default('No storage maps found', before_newline=True)

    plans = params['k8s_handler'].get_plans(
        smap_info=True, 
        nmap_info=True, 
        cache_enabled=False
    )
    if plans is None:
        my_output.error('Failed to get migration plans')
        return False

    if len(plans) > 0:
        k8s_output_handler.print_plans_state(plans)
        my_output.error('Delete migration plans first')
        return False

    my_output.default('No migration plans', before_newline=True)

    migrations = params['k8s_handler'].get_migrations(
        cache_enabled=False
    )
    if migrations is None:
        my_output.default('Failed to get migrations')
        return False
    
    if len(plans) > 0:
        k8s_output_handler.print_migrations_state(migrations)
        my_output.error('Delete migrations first')
        return False

    my_output.default('No migrations', before_newline=True, after_newline=True)
    
    return True