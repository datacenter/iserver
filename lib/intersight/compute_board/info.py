class ComputeBoardInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}

        info['BoardId'] = managed_object['BoardId']
        info['CpuTypeController'] = managed_object['CpuTypeController']
        info['Dn'] = managed_object['Dn']
        info['Model'] = managed_object['Model']
        info['Moid'] = managed_object['Moid']
        info['OperPowerState'] = managed_object['OperPowerState']
        info['Serial'] = managed_object['Serial']
        info['Vendor'] = managed_object['Vendor']

        keys = [
            'EquipmentTpms',
            'GraphicsCards',
            'MemoryArrays',
            'PciCoprocessorCards',
            'PciSwitch',
            'Processors',
            'SecurityUnits',
            'StorageControllers',
            'StorageFlexFlashControllers',
            'StorageFlexUtilControllers'
        ]
        for key in keys:
            name_ids = '%sIds' % (key)
            info[name_ids] = []
            for item in managed_object[key]:
                info[name_ids].append(
                    item['Moid']
                )

            name_count = '%sCount' % (key)
            info[name_count] = len(info[name_ids])

        return info
