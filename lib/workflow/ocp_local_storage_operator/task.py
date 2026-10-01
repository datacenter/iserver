def get_rules():
    rules = {
        'create': {
            'operator': 'operator_create',
            'volume': 'volume_create'
        },
        'delete': {
            'volume': 'volume_delete',
            'operator': 'operator_delete'
        }
    }
    return rules