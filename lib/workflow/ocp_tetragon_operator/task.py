def get_rules():
    rules = {
        'create': {
            'operator': 'operator_create',
            'crd': 'crd_create'
        },
        'delete': {
            'wipe': 'wipe',
            'crd': 'crd_delete',
            'operator': 'operator_delete'
        }
    }
    return rules