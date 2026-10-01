def get_rules():
    rules = {
        'create': {
            'feature': 'feature_enable',
            'issuer': 'issuer_create',
            'crt': 'crt_create'
        },
        'delete': {
            'wipe': 'wipe',
            'crt': 'crt_delete',
            'issuer': 'issuer_delete',
            'feature': 'feature_disable'
        }
    }
    return rules