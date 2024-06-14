class ManagementInterfaceInfo():
    def __init__(self):
        pass

    def get_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'Gateway',
            'HostName',
            'IpAddress',
            'Ipv4Address',
            'Ipv4Gateway',
            'Ipv4Mask',
            'Ipv6Address',
            'Ipv6Gateway',
            'Ipv6Prefix',
            'MacAddress',
            'Mask',
            'Moid',
            'DeviceMoId'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info
