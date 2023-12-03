class EquipmentFanInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        keys = [
            'Dn',
            'FanId',
            'FanModuleId',
            'Model',
            'ModuleId',
            'OperState',
            'PartNumber',
            'Pid',
            'Presence',
            'Serial',
            'Sku',
            'Vendor',
            'TrayId'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            if isinstance(managed_object[key], str):
                info[key] = managed_object[key].strip()
                continue

            info[key] = managed_object[key]

        if info['FanModuleId'] == 0:
            fan_module_id_fixed = False
            if 'chassis-' in info['Dn'] and '-tray-' in info['Dn'] and '-mod-' in info['Dn'] and '-fan-' in info['Dn']:
                # chassis-1-tray-1-mod-1-fan-1
                info['FanModuleId'] = int(info['Dn'].split('-mod-')[1].split('-fan-')[0])
                fan_module_id_fixed = True

            if len(info['Dn'].split('/')) == 4:
                # sys/rack-unit-1/fan-module-1-6/fan-2
                fan_module_dn = info['Dn'].split('/')[2]
                info['FanModuleId'] = int(fan_module_dn.split('-')[-1])
                fan_module_id_fixed = True

            if not fan_module_id_fixed:
                self.log.error(
                    'equipment_fan',
                    'Unsupported dn format: %s' % (info['Dn'])
                )

        info['Name'] = 'Fan Module %s - Fan %s' % (
            info['FanModuleId'],
            info['FanId']
        )

        if info['Pid'] is None or len(info['Pid']) == 0:
            info['Pid'] = info['Model']

        info['On'] = False
        if managed_object['Presence'].lower() == 'equipped' and managed_object['OperState'].lower() == 'operable':
            info['On'] = True

        if managed_object['Presence'].lower() == 'equipped' and managed_object['OperState'].lower() == 'ok':
            info['On'] = True

        if info['Presence'].lower() == 'equipped':
            info['__Output']['Presence'] = 'Green'
        else:
            info['__Output']['Presence'] = 'Red'

        if info['OperState'].lower() in ['operable', 'ok']:
            info['__Output']['OperState'] = 'Green'
        else:
            info['__Output']['OperState'] = 'Red'

        if info['On']:
            info['__Output']['On'] = 'Green'
            info['StateTick'] = '\u2713'
            info['__Output']['StateTick'] = 'Green'
        else:
            info['__Output']['On'] = 'Red'
            info['StateTick'] = '\u2717'
            info['__Output']['StateTick'] = 'Red'

        return info
