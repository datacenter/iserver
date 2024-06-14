class EquipmentFanModuleInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}
        for key in ['Moid', 'ModuleId', 'OperState', 'Presence', 'Dn']:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['Name'] = 'Fan Module %s' % (info['ModuleId'])
        if 'Fans' not in managed_object:
            print(managed_object)

        info['FanCount'] = len(managed_object['Fans'])
        info['FanMoids'] = []
        for fan in managed_object['Fans']:
            info['FanMoids'].append(fan['Moid'])

        if info['Presence'].lower() == 'equipped':
            info['__Output']['Presence'] = 'Green'
        else:
            info['__Output']['Presence'] = 'Red'

        if info['OperState'].lower() in ['operable', 'ok']:
            info['__Output']['OperState'] = 'Green'
        else:
            info['__Output']['OperState'] = 'Red'

        info['On'] = False
        if info['Presence'] == 'equipped' and info['OperState'] == 'operable':
            info['On'] = True

        if info['Presence'] == 'equipped' and info['OperState'].lower() == 'ok':
            info['On'] = True

        if info['On']:
            info['__Output']['On'] = 'Green'
            info['StateTick'] = '\u2713'
            info['__Output']['StateTick'] = 'Green'
        else:
            info['__Output']['On'] = 'Red'
            info['StateTick'] = '\u2717'
            info['__Output']['StateTick'] = 'Red'

        return info
