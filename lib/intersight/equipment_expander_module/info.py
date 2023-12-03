class EquipmentExpanderModuleInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        info['Moid'] = managed_object['Moid']
        info['Dn'] = managed_object['Dn']
        info['Model'] = managed_object['Model']

        if managed_object['Presence'] == 'equipped' and managed_object['OperState'].lower() in  ['ok', 'operable']:
            info['On'] = True
            info['OperTick'] = '\u2713'
            info['__Output']['OperTick'] = 'Green'
        else:
            info['On'] = False
            info['OperTick'] = '\u2717'
            info['__Output']['OperTick'] = 'Red'

        info['FanMoids'] = []
        for fan in managed_object['FanModules']:
            info['FanMoids'].append(fan['Moid'])
        info['FansCount'] = len(
            info['FanMoids']
        )

        info['Name'] = 'X-Fabric #%s' % (
            managed_object['ModuleId']
        )

        info['ModuleId'] = managed_object['ModuleId']
        info['OperState'] = managed_object['OperState']
        info['PartNumber'] = managed_object['PartNumber'].strip()
        info['Pid'] = managed_object['Model']

        info['Presence'] = managed_object['Presence']
        if info['Presence'] == 'equipped':
            info['__Output']['Presence'] = 'Green'
        else:
            info['__Output']['Presence'] = 'Red'

        info['Serial'] = managed_object['Serial']
        info['Vendor'] = managed_object['Vendor']

        return info
