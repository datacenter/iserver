def get_rules():
    rules = {
        'create': {
            'operator': 'operator_create',
            'policy': 'policy_create',
            'dashboard': 'dashboard_create'
        },
        'delete': {
            'dashboard': 'dashboard_delete',
            'policy': 'policy_delete',
            'operator': 'operator_delete'
        }
    }
    return rules