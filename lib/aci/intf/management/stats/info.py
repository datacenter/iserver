class InterfaceManagementStatsInfo():
    def __init__(self):
        pass

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

        return info

    def get_interface_management_stats(self, pod_id, node_id, interface_id):
        managed_object = self.get_interface_management_stats_mo(pod_id, node_id, interface_id)
        if managed_object is None:
            return None

        return self.get_interface_management_stats_info(managed_object)
