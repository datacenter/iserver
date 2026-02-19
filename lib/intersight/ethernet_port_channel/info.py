class EthernetPortChannelInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        keys = [
            'AccessVlan',
            'AdminState',
            'AllowedVlans',
            'BandWidth',
            'Description',
            'Dn',
            'Moid',
            'Name',
            'NativeVlan',
            'OperSpeed',
            'OperState',
            'PortChannelId',
            'Role',
            'SwitchId'
        ]

        info = {}
        for key in keys:
            if key not in managed_object:
                info[key] = None
                continue

            info[key] = managed_object[key]

        return info
