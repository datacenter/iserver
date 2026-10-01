def get_rules():
    rules = {
        'create': {
            'instance': 'instance_create',
            'poller': 'poller_create'
        },
        'delete': {
            'poller': 'poller_delete',
            'instance': 'instance_delete'
        }
    }
    return rules