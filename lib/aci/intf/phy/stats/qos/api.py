class InterfacePhyQosStatsApi():
    def __init__(self):
        self.interface_phy_qos_stats_mo = {}

    def get_interface_phy_qos_stats_mo(self, pod_id, node_id, cache_enabled=True):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if cache_enabled:
            if key in self.interface_phy_qos_stats_mo:
                return self.interface_phy_qos_stats_mo[key]

            cache = self.get_object_cache(
                'qosmIfClass',
                object_selector=key
            )
            if cache is not None:
                self.interface_phy_qos_stats_mo[key] = cache
                self.log.apic_mo(
                    'qosmIfClass.%s' % (key),
                    self.interface_phy_qos_stats_mo[key]
                )
                return self.interface_phy_qos_stats_mo[key]

        class_name = 'topology/pod-%s/node-%s/qosmIfClass' % (pod_id, node_id)
        managed_objects = self.get_class(
            class_name
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_phy_qos_stats_mo',
                'API failed'
            )
            return None

        self.interface_phy_qos_stats_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.interface_phy_qos_stats_mo[key].append(
                managed_object['qosmIfClass']['attributes']
            )

        self.log.apic_mo(
            'qosmIfClass.%s' % (key),
            self.interface_phy_qos_stats_mo[key]
        )

        self.set_object_cache(
            'qosmIfClass',
            self.interface_phy_qos_stats_mo[key],
            object_selector=key
        )

        return self.interface_phy_qos_stats_mo[key]
