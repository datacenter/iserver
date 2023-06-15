class InterfacePhyPcApi():
    def __init__(self):
        self.interface_phy_pc_mo = {}

    def get_interface_phy_pc_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_phy_pc_mo:
            return self.interface_phy_pc_mo[key]

        cache = self.get_object_cache(
            'pcAggrMbrIf',
            object_selector=key
        )
        if cache is not None:
            self.interface_phy_pc_mo[key] = cache
            self.log.apic_mo(
                'pcAggrMbrIf.%s' % (key),
                self.interface_phy_pc_mo[key]
            )
            return self.interface_phy_pc_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys' % (
            pod_id,
            node_id
        )
        query = 'query-target=subtree&target-subtree-class=pcAggrMbrIf'

        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_phy_pc_mo',
                'API failed'
            )
            return None

        self.interface_phy_pc_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.interface_phy_pc_mo[key].append(
                managed_object['pcAggrMbrIf']['attributes']
            )

        self.log.apic_mo(
            'pcAggrMbrIf.%s' % (key),
            self.interface_phy_pc_mo[key]
        )

        self.set_object_cache(
            'pcAggrMbrIf',
            self.interface_phy_pc_mo[key],
            object_selector=key
        )

        return self.interface_phy_pc_mo[key]
