from lib import log_helper


class ProtocolNdInterfaceStats():
    def __init__(self, log_id=None):
        self.log = log_helper.Log(log_id=log_id)

    def get_protocol_nd_interface_stats_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        return info
