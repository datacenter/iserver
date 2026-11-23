def get_rules():
    rules = {
        'create': {
            'operator': 'operator_create',
            'driver': 'driver_create',
            'cluster': 'cluster_create',
            'storage': 'storage_create'
        },
        'delete': {
            'wipe': 'wipe',
            'storage': 'storage_delete',
            'cluster': 'cluster_delete',
            'driver': 'driver_delete',
            'operator': 'operator_delete'
        }
    }
    return rules