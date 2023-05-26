class InterfacePhyPcApi():
    def __init__(self):
        self.interface_phy_pc_mo = {}

    def get_interface_phy_pc_mo(self, pod_id, node_id, interface_id):
        key = '%s.%s.%s' % (
            pod_id,
            node_id,
            interface_id.split('/')[1]
        )
        if key in self.interface_phy_pc_mo:
            return self.interface_phy_pc_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/phys-[%s]' % (
            pod_id,
            node_id,
            interface_id
        )
        query = 'query-target=children&target-subtree-class=pcAggrMbrIf'

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

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_interface_phy_pc_mo',
                'Unexpected object count'
            )
            return None

        self.interface_phy_pc_mo[key] = managed_objects['imdata'][0]['pcAggrMbrIf']['attributes']

        self.log.apic_mo(
            'pcAggrMbrIf.%s' % (key),
            self.interface_phy_pc_mo[key]
        )

        return self.interface_phy_pc_mo[key]
