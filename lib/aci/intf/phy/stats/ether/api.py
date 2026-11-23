class InterfacePhyEtherStatsApi():
    def __init__(self):
        self.interface_phy_ether_stats_mo = {}

    def get_interface_phy_ether_stats_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_phy_ether_stats_mo:
            return self.interface_phy_ether_stats_mo[key]

        cache = self.get_object_cache(
            'ethpmPhysIf',
            object_selector=key
        )
        if cache is not None:
            self.interface_phy_ether_stats_mo[key] = cache
            self.log.apic_mo(
                'ethpmPhysIf.%s' % (key),
                self.interface_phy_ether_stats_mo[key]
            )
            return self.interface_phy_ether_stats_mo[key]

        class_name = 'topology/pod-%s/node-%s/ethpmPhysIf' % (pod_id, node_id)
        managed_objects = self.get_class(
            class_name
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_phy_ether_stats_mo',
                'API failed'
            )
            return None

        self.interface_phy_ether_stats_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.interface_phy_ether_stats_mo[key].append(
                managed_object['ethpmPhysIf']['attributes']
            )

        self.log.apic_mo(
            'ethpmPhysIf.%s' % (key),
            self.interface_phy_ether_stats_mo[key]
        )

        self.set_object_cache(
            'ethpmPhysIf',
            self.interface_phy_ether_stats_mo[key],
            object_selector=key
        )

        return self.interface_phy_ether_stats_mo[key]
