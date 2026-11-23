def get_rules():
    rules = {
        'create': {
            'operator': 'operator_create',
            'instance': 'instance_create',
            'vc': 'vcenter_provider_create',
            'nmap': 'network_map_create',
            'smap': 'storage_map_create',
            'plan': 'plan_create',
            'run': 'migration_run'
        },
        'delete': {
            'plan': 'plan_delete',
            'smap': 'storage_map_delete',
            'nmap': 'network_map_delete',
            'vc': 'provider_delete',
            'instance': 'instance_delete',
            'operator': 'operator_delete'
        }
    }
    return rules