class EndpointHvInfo():
    def __init__(self):
        pass

    def get_endpoint_hv_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'rn',
            'state',
            'tCl',
            'tDn',
            'tType'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info
