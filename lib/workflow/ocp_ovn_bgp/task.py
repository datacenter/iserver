def get_rules():
    rules = {
        'create': {
            'feature': 'feature_enable',
            'config': 'configuration_create',
            'ra': 'ra_enable',
            'ra-config': 'ra_create'
        },
        'delete': {
            'config': 'configuration_delete',
            'ra-config': 'ra_delete',
            'ra': 'ra_disable',
            'wipe': 'wipe',
            'feature': 'feature_disable'
        }
    }
    return rules