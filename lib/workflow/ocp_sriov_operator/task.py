def get_rules():
    rules = {
        'create': {
            'operator': 'operator_create',
            'instance': 'instance_create'
        },
        'delete': {
            'instance': 'instance_delete',
            'operator': 'operator_delete'
        }
    }
    return rules