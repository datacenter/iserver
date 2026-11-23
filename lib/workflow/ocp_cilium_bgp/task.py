def get_rules():
    rules = {
        'create': {
            'feature': 'feature_enable',
            'cluster': 'cluster_create',
            'crd': 'apply_crd'
        },
        'delete': {
            'crd': 'delete_crd',
            'wipe': 'wipe',
            'feature': 'feature_disable'
        }
    }
    return rules