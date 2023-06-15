class InterfacePhyRmonStatsInfo():
    def __init__(self):
        self.interface_phy_rmon_stats = {}

    def get_interface_phy_rmon_stats_info(self, managed_object):
        info = {}
        for key in managed_object:
            info[key] = managed_object[key]

        # "dn": "topology/pod-1/node-205/sys/phys-[eth1/1]/dbgEtherStats"
        info['pod_id'] = info['dn'].split('/')[1]
        info['node_id'] = info['dn'].split('/')[2]
        info['interface_id'] = None
        if info['dn'].split('/')[4].startswith('phys-'):
            info['interface_id'] = info['dn'].split('phys-[')[1].split(']')[0]

        if info['dn'].split('/')[4].startswith('aggr-'):
            info['interface_id'] = info['dn'].split('aggr-[')[1].split(']')[0]

        # topology/pod-1/node-205/sys/mgmt-[mgmt0]/dbgEtherStats
        if info['dn'].split('/')[4].startswith('mgmt-'):
            info['interface_id'] = info['dn'].split('mgmt-[')[1].split(']')[0]

        if info['dn'].split('/')[4].startswith('ctx-'):
            # topology/pod-1/node-205/sys/ctx-[vxlan-2523141]/encrtd-[eth1/24.52]/dbgEtherStats
            if info['dn'].split('/')[5].startswith('encrtd-'):
                info['interface_id'] = info['dn'].split('encrtd-[')[1].split(']')[0]
                info['context_id'] = info['dn'].split('ctx-[')[1].split(']')[0]

            # topology/pod-1/node-205/sys/ctx-[vxlan-2195458]/bd-[vxlan-16121819]/svi-[vlan11]/dbgEtherStats
            if info['dn'].split('/')[5].startswith('bd-'):
                info['interface_id'] = info['dn'].split('svi-[')[1].split(']')[0]
                info['context_id'] = info['dn'].split('ctx-[')[1].split(']')[0]

        # topology/pod-1/node-205/sys/inst-overlay-1/encrtd-[eth1/35.9]/dbgEtherStats
        if info['dn'].split('/')[4].startswith('inst-'):
            info['interface_id'] = info['dn'].split('encrtd-[')[1].split(']')[0]

        if info['interface_id'] is None:
            self.log.error(
                'get_interface_phy_rmon_info',
                'Unsupported dn: %s' % (info['dn'])
            )

        return info

    def get_interfaces_phy_rmon_stats_info(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_phy_rmon_stats:
            return self.interface_phy_rmon_stats[key]

        managed_objects = self.get_interface_phy_rmon_stats_mo(
            pod_id,
            node_id
        )
        if managed_objects is None:
            return None

        self.interface_phy_rmon_stats[key] = []
        for managed_object in managed_objects:
            self.interface_phy_rmon_stats[key].append(
                self.get_interface_phy_rmon_stats_info(
                    managed_object
                )
            )

        return self.interface_phy_rmon_stats[key]

    def get_interface_phy_rmon_stats(self, pod_id, node_id, interface_id):
        interfaces_info = self.get_interfaces_phy_rmon_stats_info(pod_id, node_id)
        if interfaces_info is None:
            return None

        for interface_info in interfaces_info:
            if interface_id == interface_info['interface_id']:
                return interface_info

        return None
