def get_rules():
    rules = {
        'create': {
            'operator': 'operator_create',
            'instance': 'instance_create',
            'import': 'import_enable'
        },
        'delete': {
            'import': 'import_disable',
            'instance': 'instance_delete',
            'operator': 'operator_delete'
        }
    }
    return rules