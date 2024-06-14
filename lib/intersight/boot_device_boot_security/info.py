class BootDeviceBootSecurityInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}

        info['SecureBoot'] = managed_object['SecureBoot']
        info['Moid'] = managed_object['Moid']

        return info
