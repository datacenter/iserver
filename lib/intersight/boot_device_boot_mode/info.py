class BootDeviceBootModeInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}

        info['ConfiguredBootMode'] = managed_object['ConfiguredBootMode']
        info['Moid'] = managed_object['Moid']

        return info
