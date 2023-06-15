class InterfaceLacpStatsInfo():
    def __init__(self):
        self.interface_lacp_stats = {}

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

        # "dn": "topology/pod-1/node-205/sys/lacp/inst/if-[eth1/27]/ifstats"
        info['pod_id'] = info['dn'].split('/')[1]
        info['node_id'] = info['dn'].split('/')[2]
        info['interface_id'] = info['dn'].split('if-[')[1].split(']')[0]

        return info

    def get_interfaces_lacp_stats_info(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_lacp_stats:
            return self.interface_lacp_stats[key]

        managed_objects = self.get_interface_lacp_stats_mo(
            pod_id,
            node_id
        )
        if managed_objects is None:
            return None

        self.interface_lacp_stats[key] = []
        for managed_object in managed_objects:
            self.interface_lacp_stats[key].append(
                self.get_interface_lacp_stats_info(
                    managed_object
                )
            )

        return self.interface_lacp_stats[key]

    def get_interface_lacp_stats(self, pod_id, node_id, interface_id):
        interfaces_info = self.get_interfaces_lacp_stats_info(pod_id, node_id)
        if interfaces_info is None:
            return None

        for interface_info in interfaces_info:
            if interface_id == interface_info['interface_id']:
                return interface_info

        return None
