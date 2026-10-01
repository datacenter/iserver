def get_rules():
    rules = {
        'create': {
            'attach': 'attach',
            'detach': 'detach',
            'inspect': 'inspect',
            'node': 'create_host',
            'power-on': 'power_on',
            'power-off': 'power_off',
            'reboot': 'reboot',
            'register': 'register'
        },
        'delete': {
            'node': 'delete_host'
        }
    }
    return rules