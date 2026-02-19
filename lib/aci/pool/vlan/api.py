class PoolVlanApi():
    def __init__(self):
        self.pool_vlan_mo = None

    def init_pool_vlan_mo(self):
        self.pool_vlan_mo = None

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

    def get_pool_vlan_mo(self, node_info=False, cache_enabled=True):
        if self.pool_vlan_mo is not None:
            return self.pool_vlan_mo

        if cache_enabled:
            cache = self.get_object_cache(
                'fvnsVlanInstP'
            )
            if cache is not None:
                self.pool_vlan_mo = cache
                self.log.apic_mo(
                    'fvnsVlanInstP',
                    self.pool_vlan_mo
                )
                return self.pool_vlan_mo

        query = 'rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=fvnsEncapBlk,fvnsRtVlanNs'
        managed_objects = self.get_class(
            'fvnsVlanInstP',
            query=query
        )

        if managed_objects is None:
            return None

        self.pool_vlan_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fvnsVlanInstP']['attributes']
            attributes['fvnsEncapBlk'] = self.get_pool_vlan_block_attributes(
                managed_object
            )
            attributes['fvnsRtVlanNs'] = self.get_pool_vlan_domain_attributes(
                managed_object
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'fvnsVlanInstP',
                managed_object,
                'faultCounts'
            )

            if node_info:
                extras = [
                    'VlanNsToInterface',
                    'VlanNsToVirtualMachines',
                    'VlanNsToVmmPortGroups'
                ]
                for extra in extras:
                    distinguished_name = 'uni/infra/vlanns-[%s]-%s' % (
                        attributes['name'],
                        attributes['allocMode']
                    )
                    query = 'rsp-subtree-include=full-deployment&target-node=all&target-path=%s' % (extra)
                    extra_mo = self.get_managed_object(
                        distinguished_name,
                        query=query,
                        node_mo=True
                    )

                    if extra_mo['totalCount'] != '1':
                        self.log.error(
                            'get_pool_vlan_mo',
                            'Unexpected object count: %s' % (extra)
                        )
                        return None

                    if extra == 'VlanNsToInterface':
                        attributes[extra] = self.get_mo_node_resource_ctx(
                            'fvnsVlanInstP',
                            extra_mo['imdata'][0]
                        )
                    else:
                        attributes[extra] = self.get_mo_ctlr_resource_ctx(
                            'fvnsVlanInstP',
                            extra_mo['imdata'][0]
                        )

            self.pool_vlan_mo.append(
                attributes
            )

        self.log.apic_mo(
            'fvnsVlanInstP',
            self.pool_vlan_mo
        )

        self.set_object_cache(
            'fvnsVlanInstP',
            self.pool_vlan_mo
        )

        return self.pool_vlan_mo
