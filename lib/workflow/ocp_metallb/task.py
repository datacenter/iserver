def get_rules():
    rules = {
        'create': {
            'operator': 'operator_create',
            'instance': 'instance_create',
            'adv': 'adv_create',
            'bfd': 'bfd_create',
            'community': 'community_create',
            'peer': 'peer_create',
            'pool': 'pool_create'
        },
        'delete': {
            'adv': 'adv_delete',
            'bfd': 'bfd_delete',
            'community': 'community_delete',
            'peer': 'peer_delete',
            'pool': 'pool_delete',
            'instance': 'instance_delete',
            'operator': 'operator_delete'
        }
    }
    return rules