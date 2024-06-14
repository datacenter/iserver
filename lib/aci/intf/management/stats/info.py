class InterfaceManagementStatsInfo():
    def __init__(self):
        self.interface_management_stats = {}

    def get_interface_management_stats_info(self, managed_object):
        keys = [
            'addr',
            'dn',
            'ipv4CfgFailedBmp',
            'ipv4CfgFailedTs',
            'ipv4CfgState',
            'operSt',
            'operStQual',
            'pref',
            'type',
            'vpcPeer'
        ]

        info = {}
        info['__Output'] = {}
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['operSt'] == 'up':
            info['__Output']['operSt'] = 'Green'
            if info['operStQual'] == 'up':
                info['operStQual'] = 'link-up-connected'
        else:
            info['__Output']['operSt'] = 'Red'

        info['pod_id'] = info['dn'].split('/')[1]
        info['node_id'] = info['dn'].split('/')[2]
        info['interface_id'] = info['dn'].split('if-[')[1].split(']')[0]

        return info

    def get_interfaces_management_stats_info(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_management_stats:
            return self.interface_management_stats[key]

        managed_objects = self.get_interface_management_stats_mo(
            pod_id,
            node_id
        )
        if managed_objects is None:
            return None

        self.interface_management_stats[key] = []
        for managed_object in managed_objects:
            self.interface_management_stats[key].append(
                self.get_interface_management_stats_info(
                    managed_object
                )
            )

        return self.interface_management_stats[key]

    def get_interface_management_stats(self, pod_id, node_id, interface_id):
        interfaces_info = self.get_interfaces_management_stats_info(pod_id, node_id)
        if interfaces_info is None:
            return None

        for interface_info in interfaces_info:
            if interface_id == interface_info['interface_id']:
                return interface_info

        return None
