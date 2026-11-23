class ChassisProfileInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['Moid'] = managed_object['Moid']
        info['Name'] = managed_object['Name']

        return info
