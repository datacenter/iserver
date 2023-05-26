class ProtocolHsrpInterfaceStatsInfo():
    def __init__(self):
        pass

    def get_protocol_hsrp_interface_stats_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        return info
