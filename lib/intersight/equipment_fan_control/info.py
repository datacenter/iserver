class EquipmentFanControlInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        keys = [
            'Moid',
            'Dn',
            'Mode'
        ]

        info = {}
        for key in keys:
            info[key] = managed_object[key]

        return info
