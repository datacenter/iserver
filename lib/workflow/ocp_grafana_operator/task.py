def get_rules():
    rules = {
        'create': {
            'operator': 'operator_create',
            'mon': 'monitoring_enable',
            'instance': 'instance_create',
            'dashboard': 'dashboard_create'
        },
        'delete': {
            'instance': 'instance_delete',
            'wipe': 'wipe',
            'mon': 'monitoring_disable',
            'operator': 'operator_delete'
        }
    }
    return rules