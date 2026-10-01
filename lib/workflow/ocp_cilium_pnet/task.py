def get_rules():
    rules = {
        'create': {
            'feature': 'feature_enable',
            'multus': 'multus_enable',
            'webhook': 'webhook_enable',
            'network': 'network_create',
            'test': 'test'
        },
        'delete': {
            'wipe': 'wipe',
            'webhook': 'webhook_disable',
            'network': 'network_delete',
            'feature': 'feature_disable'
        }
    }
    return rules