class EquipmentPsuInfo():
    def __init__(self):
        pass

    def is_psu_on(self, managed_object):
        if managed_object is None:
            return False

        if managed_object['Presence'] != 'equipped':
            return False

        if managed_object['Voltage'] == 'ok':
            return True

        try:
            if int(managed_object['Voltage']) > 0:
                return True
        except BaseException:
            pass

        return False

    def get_info(self, managed_object):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}

        keys = [
            'Moid',
            'Name',
            'Model',
            'Serial',
            'Vendor',
            'Dn',
            'Model',
            'Vendor',
            'Voltage',
            'Presence',
            'Pid'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['Id'] = info['Dn'].split('-')[-1]
        if info['Name'] is None or len(info['Name']) == 0:
            info['Name'] = 'PSU #%s' % (info['Id'])

        if info['Pid'] is None or len(info['Pid']) == 0:
            info['Pid'] = info['Model']

        info['On'] = self.is_psu_on(
            managed_object
        )

        if info['On']:
            info['StateTick'] = '\u2713'
            info['__Output']['StateTick'] = 'Green'
        else:
            info['StateTick'] = '\u2717'
            info['__Output']['StateTick'] = 'Red'

        if info['Voltage'].lower() == 'ok':
            info['__Output']['Voltage'] = 'Green'
        else:
            info['__Output']['Voltage'] = 'Red'

        if info['Presence'].lower() == 'equipped':
            info['PresenceTick'] = '\u2713'
            info['__Output']['PresenceTick'] = 'Green'
        else:
            info['PresenceTick'] = '\u2717'
            info['__Output']['PresenceTick'] = 'Red'

        return info
