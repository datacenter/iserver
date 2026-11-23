def get_rules():
    rules = {
        'create': {
            'wipe': 'wipe',
            'operator': 'operator_create',
            'cluster': 'cluster_create'
        },
        'delete': {
            'orphan': 'orphan',
            'unused': 'unused',
            'cluster': 'cluster_delete',
            'operator': 'operator_delete'
        }
    }
    return rules