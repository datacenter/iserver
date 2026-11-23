class InterfacePhyEeeApi():
    def __init__(self):
        self.interface_phy_eee_mo = {}

    def get_interface_phy_eee_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_phy_eee_mo:
            return self.interface_phy_eee_mo[key]

        cache = self.get_object_cache(
            'l1EeeP',
            object_selector=key
        )
        if cache is not None:
            self.interface_phy_eee_mo[key] = cache
            self.log.apic_mo(
                'l1EeeP.%s' % (key),
                self.interface_phy_eee_mo[key]
            )
            return self.interface_phy_eee_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys' % (
            pod_id,
            node_id
        )
        query = 'query-target=subtree&target-subtree-class=l1EeeP'

        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_phy_eee_mo',
                'API failed'
            )
            return None

        self.interface_phy_eee_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.interface_phy_eee_mo[key].append(
                managed_object['l1EeeP']['attributes']
            )

        self.log.apic_mo(
            'l1EeeP.%s' % (key),
            self.interface_phy_eee_mo[key]
        )

        self.set_object_cache(
            'l1EeeP',
            self.interface_phy_eee_mo[key],
            object_selector=key
        )

        return self.interface_phy_eee_mo[key]
