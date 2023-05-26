class InterfacePhyEeeApi():
    def __init__(self):
        self.interface_phy_eee_mo = {}

    def get_interface_phy_eee_mo(self, pod_id, node_id, interface_id):
        key = '%s.%s.%s' % (
            pod_id,
            node_id,
            interface_id.split('/')[1]
        )
        if key in self.interface_phy_eee_mo:
            return self.interface_phy_eee_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/phys-[%s]' % (
            pod_id,
            node_id,
            interface_id
        )
        query = 'query-target=children&target-subtree-class=l1EeeP'

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

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_interface_phy_eee_mo',
                'Unexpected object count'
            )
            return None

        self.interface_phy_eee_mo[key] = managed_objects['imdata'][0]['l1EeeP']['attributes']

        self.log.apic_mo(
            'l1EeeP.%s' % (key),
            self.interface_phy_eee_mo[key]
        )

        return self.interface_phy_eee_mo[key]
