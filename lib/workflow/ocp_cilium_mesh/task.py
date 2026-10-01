def get_rules():
    rules = {
        'create': {
            'feature': 'feature_enable',
            'cluster': 'cluster_create',
            'timescape': 'timescape_enable'
        },
        'delete': {
            'cluster': 'cluster_delete',
            'feature': 'feature_disable',
            'timescape': 'timescape_disable'
        }
    }
    return rules