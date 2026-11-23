def get_rules():
    rules = {
        'create': {
            'feature': 'add',
            'sync': 'sync_add'
        },
        'delete': {
            'sync': 'sync_delete',
            'feature': 'delete'
        }
    }
    return rules