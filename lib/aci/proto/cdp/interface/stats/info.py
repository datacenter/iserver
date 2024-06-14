class ProtocolCdpInterfaceStatsInfo():
    def __init__(self):
        pass

    def get_protocol_cdp_interface_stats_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        keys = [
            'cksumErrRcvd',
            'failedSent',
            'malformRcvd',
            'unSupVerRcvd'
        ]
        for key in keys:
            if info[key] != '0':
                info['__Output'][key] = 'Red'

        return info
