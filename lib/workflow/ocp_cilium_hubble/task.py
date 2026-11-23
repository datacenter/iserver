def get_rules():
    rules = {
        'create': {
            'relay': 'relay_enable',
            'timescape': 'timescape_enable'
        },
        'delete': {
            'relay': 'relay_disable',
            'timescape': 'timescape_disable'
        }
    }
    return rules