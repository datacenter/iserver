class BiosBootModeInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}

        info['ActualBootMode'] = managed_object['ActualBootMode']
        info['Moid'] = managed_object['Moid']

        return info
