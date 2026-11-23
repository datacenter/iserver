class CondHclStatusInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        info['ComponentStatus'] = managed_object['ComponentStatus']
        info['HardwareStatus'] = managed_object['HardwareStatus']
        info['HclFirmwareVersion'] = managed_object['HclFirmwareVersion']
        info['HclModel'] = managed_object['HclModel']
        info['HclOsVendor'] = managed_object['HclOsVendor']
        info['HclOsVersion'] = managed_object['HclOsVersion']
        info['HclProcessor'] = managed_object['HclProcessor']
        info['Moid'] = managed_object['Moid']
        info['Reason'] = managed_object['Reason']
        info['ServerReason'] = managed_object['ServerReason']
        info['SoftwareStatus'] = managed_object['SoftwareStatus']
        info['Status'] = managed_object['Status']

        for key in ['Status', 'SoftwareStatus', 'HardwareStatus', 'ComponentStatus']:
            if info[key] == 'Incomplete':
                info['__Output'][key] = 'Red'

            if info[key] == 'Not-Listed':
                info['__Output'][key] = 'Yellow'

            if info[key] == 'Validated':
                info['__Output'][key] = 'Green'

            if info[key] == 'Not-Evaluated':
                info['__Output'][key] = 'Yellow'

        return info
