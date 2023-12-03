class EquipmentTpmInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'ActivationStatus',
            'AdminState',
            'FirmwareVersion',
            'Model',
            'Moid',
            'Presence',
            'Serial',
            'TpmId',
            'Vendor',
            'Version'
        ]

        for key in keys:
            info[key] = managed_object[key]

        if info['ActivationStatus'].lower() == 'activated':
            info['__Output']['ActivationStatus'] = 'Green'

        if info['ActivationStatus'].lower() == 'unknown':
            info['__Output']['ActivationStatus'] = 'Yellow'

        if info['AdminState'].lower() == 'unknown':
            info['__Output']['AdminState'] = 'Yellow'

        if info['AdminState'].lower() == 'enabled':
            info['__Output']['AdminState'] = 'Green'

        if info['AdminState'].lower() == 'disabled':
            info['__Output']['AdminState'] = 'Red'

        if info['Presence'].lower() == 'empty':
            info['__Output']['Presence'] = 'Yellow'
        else:
            info['__Output']['Presence'] = 'Green'

        return info
