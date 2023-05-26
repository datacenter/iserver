class PoolVlanApi():
    def __init__(self):
        self.mo_pool_vlan = None

    def get_pool_vlan_block_attributes(self, managed_object):
        attributes = []
        for child in managed_object['fvnsVlanInstP']['children']:
            for key in child:
                if key == 'fvnsEncapBlk':
                    attributes.append(
                        child['fvnsEncapBlk']['attributes']
                    )
        return attributes

    def get_pool_vlan_domain_attributes(self, managed_object):
        attributes = []
        for child in managed_object['fvnsVlanInstP']['children']:
            for key in child:
                if key == 'fvnsRtVlanNs':
                    attributes.append(
                        child['fvnsRtVlanNs']['attributes']
                    )
        return attributes

    def initialize_pool_vlan(self):
        if self.mo_pool_vlan is not None:
            return True

        query = 'rsp-subtree=children&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs'
        managed_objects = self.get_class(
            'fvnsVlanInstP',
            query=query
        )

        if managed_objects is None:
            return False

        # self.log.apic_mo(
        #     'fvnsVlanInstP.mo',
        #     managed_objects
        # )

        self.mo_pool_vlan = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fvnsVlanInstP']['attributes']
            attributes['fvnsEncapBlk'] = self.get_pool_vlan_block_attributes(
                managed_object
            )
            attributes['fvnsRtVlanNs'] = self.get_pool_vlan_domain_attributes(
                managed_object
            )
            self.mo_pool_vlan.append(
                attributes
            )

        self.log.apic_mo(
            'fvnsVlanInstP',
            self.mo_pool_vlan
        )

        return True
