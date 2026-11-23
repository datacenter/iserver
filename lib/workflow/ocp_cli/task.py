def get_rules():
    rules = {
        'create': {
            'bashrc': 'bashrc_configure',
            'butane': 'butane_create',
            'cilium': 'cilium_create',
            'file': 'file_apply',
            'helm': 'helm_create',
            'hubble': 'hubble_create',
            'tridentctl': 'tridentctl_create',
            'virtctl': 'virtctl_create'
        },
        'delete': {
            'butane': 'butane_delete',
            'cilium': 'cilium_delete',
            'file': 'file_unapply',
            'helm': 'helm_delete',
            'hubble': 'hubble_delete',
            'tridentctl': 'tridentctl_delete',
            'virtctl': 'virtctl_delete'

        }
    }
    return rules