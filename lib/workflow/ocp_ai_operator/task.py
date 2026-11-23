def get_rules():
    rules = {
        'create': {
            'operator': 'operator_create',
            'cluster': 'cluster_create'
        },
        'delete': {
            'cluster': 'cluster_delete',
            'operator': 'operator_delete'
        }
    }
    return rules