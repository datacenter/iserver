class InterfacePhyEpgStatsInfo():
    def __init__(self):
        pass

    def get_interface_phy_epg_stats_info(self, managed_object):
        info = {}
        for key in managed_object:
            info[key] = managed_object[key]
        return info

    def get_interface_phy_epg_stats(self, pod_id, node_id, interface_id, vlan_info=False, vlans=None):
        epg_stats_mo = self.get_interface_phy_epg_stats_mo(pod_id, node_id, interface_id)
        if epg_stats_mo is None:
            return None

        epg_stats = []
        for epg_stat_mo in epg_stats_mo:
            epg_stat_info = self.get_interface_phy_epg_stats_info(epg_stat_mo)
            if vlan_info:
                vlan_stats = self.get_vlan_stats(
                    pod_id,
                    node_id,
                    vlan_filter=[
                        'epg:%s' % (epg_stat_info['dn']),
                        'vlan:%s' % (vlans)
                    ]
                )
                epg_stat_info['vlan'] = None
                if vlan_stats is not None:
                    if len(vlan_stats) == 0:
                        epg_stat_info['vlan'] = None
                    if len(vlan_stats) == 1:
                        epg_stat_info['vlan'] = vlan_stats[0]
                    if len(vlan_stats) > 1:
                        self.log.error(
                            'get_interface_phy_epg_stats',
                            'Unexpected epg vlan stats: %s/%s/%s' % (
                                pod_id,
                                node_id,
                                interface_id
                            )
                        )
                        self.log.error(
                            'get_interface_phy_epg_stats',
                            vlan_stats
                        )

            epg_stats.append(
                epg_stat_info
            )

        return epg_stats
