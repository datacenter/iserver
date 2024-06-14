class ServerProfileInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'Name',
            'ModTime',
            'Moid',
            'ServerAssignmentMode',
            'TargetPlatform',
            'Type'
        ]

        for key in keys:
            info[key] = managed_object[key]

        info['ConfigState'] = managed_object['ConfigContext']['ConfigState']
        info['ConfigChangeState'] = managed_object['ConfigChangeContext']['ConfigChangeState']

        if info['ConfigState'].lower() == 'out-of-sync':
            info['__Output']['ConfigState'] = 'Red'

        if info['ConfigState'].lower() == 'assigned':
            info['__Output']['ConfigState'] = 'Yellow'

        if info['ConfigState'].lower() == 'validating':
            info['__Output']['ConfigState'] = 'Blue'

        if info['ConfigState'].lower() == 'associated':
            info['__Output']['ConfigState'] = 'Green'

        info['ConfigChangeDetails'] = []
        for config_change_details in managed_object['ConfigChangeDetails']:
            config_change_info = {}
            config_change_info['EntityMoid'] = config_change_details['ConfigChangeContext']['EntityMoid']
            config_change_info['EntityType'] = config_change_details['ConfigChangeContext']['EntityType']
            info['ConfigChangeDetails'].append(
                config_change_info
            )

        return info
