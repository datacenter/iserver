class InterfaceLacpStatsInfo():
    def __init__(self):
        pass

    def get_interface_lacp_stats_info(self, managed_object):
        keys = [
            'dn',
            'errPktRcvd',
            'markerRcvd',
            'markerRspRcvd',
            'markerRspSent',
            'markerSent',
            'pduRcvd',
            'pduSent',
            'pduTimeOut'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if int(info['errPktRcvd']) > 0:
            info['__Output']['errPktRcvd'] = 'Red'

        if int(info['pduTimeOut']) > 0:
            info['__Output']['pduTimeOut'] = 'Red'

        return info

    def get_interface_lacp_stats(self, pod_id, node_id, interface_id):
        managed_object = self.get_interface_lacp_stats_mo(pod_id, node_id, interface_id)
        if managed_object is None:
            return None

        return self.get_interface_lacp_stats_info(managed_object)
