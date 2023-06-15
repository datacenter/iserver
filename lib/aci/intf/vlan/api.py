class InterfaceVlanStatsApi():
    def __init__(self):
        self.vlan_stats_mo = {}

    def get_vlan_stats_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.vlan_stats_mo:
            return self.vlan_stats_mo[key]

        cache = self.get_object_cache(
            'vlanCktEp',
            object_selector=key
        )
        if cache is not None:
            self.vlan_stats_mo[key] = cache
            self.log.apic_mo(
                'vlanCktEp.%s' % (key),
                self.vlan_stats_mo[key]
            )
            return self.vlan_stats_mo[key]

        class_name = 'topology/pod-%s/node-%s/vlanCktEp' % (pod_id, node_id)
        managed_objects = self.get_class(
            class_name
        )

        if managed_objects is None:
            self.log.error(
                'get_vlan_stats_mo',
                'API failed'
            )
            return None

        self.vlan_stats_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.vlan_stats_mo[key].append(
                managed_object['vlanCktEp']['attributes']
            )

        self.log.apic_mo(
            'vlanCktEp.%s' % (key),
            self.vlan_stats_mo[key]
        )

        self.set_object_cache(
            'vlanCktEp',
            self.vlan_stats_mo[key],
            object_selector=key
        )

        return self.vlan_stats_mo[key]
