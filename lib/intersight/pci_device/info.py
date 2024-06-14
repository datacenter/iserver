class PciDeviceInfo():
    def __init__(self):
        pass

    def get_pid(self, managed_object):
        if 'ComputeRackUnit' in managed_object and managed_object['ComputeRackUnit'] is not None:
            if managed_object['Pid'] in [None, 'N/A', 'UNKNOWN', '']:
                return None
            return managed_object['Pid']

        if 'ComputeBlade' in managed_object and managed_object['ComputeBlade'] is not None:
            if managed_object['Pid'] in [None, 'N/A', 'UNKNOWN', '']:
                return managed_object['Model']

            return managed_object['Pid']

        return None

    def get_model(self, managed_object):
        return managed_object['Model']

    def get_info(self, managed_object):
        info = {}

        keys = [
            'SlotId',
            'Vendor',
            'FirmwareVersion',
            'Dn',
            'Serial'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['Pid'] = self.get_pid(managed_object)
        info['Model'] = self.get_model(managed_object)

        return info
