class PowerControlStateInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'Moid',
            'AllocatedPower',
            'ExtendedPowerCapacity',
            'GridMaxPower',
            'MaxRequiredPower',
            'MinRequiredPower',
            'N1MaxPower',
            'N2MaxPower',
            'NonRedundantMaxPower',
            'PowerRebalancing',
            'PowerSaveMode'
        ]
        for key in keys:
            info[key] = managed_object[key]

        if info['PowerRebalancing'] == 'Enabled':
            info['__Output']['PowerRebalancing'] = 'Green'
        else:
            info['__Output']['PowerRebalancing'] = 'Red'

        if info['PowerSaveMode'] == 'Enabled':
            info['__Output']['PowerSaveMode'] = 'Green'
        else:
            info['__Output']['PowerSaveMode'] = 'Red'

        if info['ExtendedPowerCapacity'] == 'Enabled':
            info['__Output']['ExtendedPowerCapacity'] = 'Green'
        else:
            info['__Output']['ExtendedPowerCapacity'] = 'Red'

        if managed_object['AllocatedPower'] == 0:
            managed_object['AllocatedBudget'] = 'Not set'
        else:
            managed_object['AllocatedBudget'] = managed_object['AllocatedPower']

        keys = [
            'AllocatedPower',
            'GridMaxPower',
            'MaxRequiredPower',
            'MinRequiredPower',
            'N1MaxPower',
            'N2MaxPower',
            'NonRedundantMaxPower'
        ]

        for key in keys:
            info['%sUnit' % (key)] = '%s W' % (str(info[key]))

        return info
