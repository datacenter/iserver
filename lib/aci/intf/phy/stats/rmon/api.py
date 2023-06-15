class InterfacePhyRmonStatsApi():
    def __init__(self):
        self.interface_phy_rmon_stats_mo = {}

    def get_interface_phy_rmon_stats_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_phy_rmon_stats_mo:
            return self.interface_phy_rmon_stats_mo[key]

        cache = self.get_object_cache(
            'rmonEtherStats',
            object_selector=key
        )
        if cache is not None:
            self.interface_phy_rmon_stats_mo[key] = cache
            self.log.apic_mo(
                'rmonEtherStats.%s' % (key),
                self.interface_phy_rmon_stats_mo[key]
            )
            return self.interface_phy_rmon_stats_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys' % (
            pod_id,
            node_id
        )
        query = 'query-target=subtree&target-subtree-class=rmonEtherStats'

        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_phy_rmon_stats_mo',
                'API failed'
            )
            return None

        self.interface_phy_rmon_stats_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.interface_phy_rmon_stats_mo[key].append(
                managed_object['rmonEtherStats']['attributes']
            )

        self.log.apic_mo(
            'rmonEtherStats.%s' % (key),
            self.interface_phy_rmon_stats_mo[key]
        )

        self.set_object_cache(
            'rmonEtherStats',
            self.interface_phy_rmon_stats_mo[key],
            object_selector=key
        )

        return self.interface_phy_rmon_stats_mo[key]
