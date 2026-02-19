class EndpointIpInfo():
    def __init__(self):
        pass

    def get_endpoint_ip_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'addr',
            'baseEpgDn',
            'vrfDn'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info
