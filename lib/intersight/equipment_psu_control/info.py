class EquipmentPsuControlInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'Model',
            'Serial',
            'Vendor',
            'Dn',
            'InputPowerState',
            'OperState',
            'OutputPowerState',
            'Redundancy'
        ]
        for key in keys:
            info[key] = managed_object[key]

        keys = [
            'InputPowerState',
            'OperState',
            'OutputPowerState'
        ]
        for key in keys:
            info[key] = info[key].lower()
            if info[key] == '':
                info['%sTick' % (key)] = ''
                continue

            if info[key] == 'ok':
                info['%sTick' % (key)] = '\u2713'
                info['__Output']['%sTick' % (key)] = 'Green'
            else:
                info['%sTick' % (key)] = '\u2717'
                info['__Output']['%sTick' % (key)] = 'Red'

        return info
