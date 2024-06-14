class BootHddDeviceInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}

        info['Moid'] = managed_object['Moid']
        info['Name'] = managed_object['Name']
        info['Order'] = managed_object['Order']
        info['State'] = managed_object['State']
        info['Type'] = managed_object['Type']

        return info
