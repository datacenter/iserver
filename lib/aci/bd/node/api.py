class BridgeDomainNodeApi():
    def __init__(self):
        self.bridge_domain_node_mo = {}

    def get_bridge_domain_node_mo(self, tenant_name, bd_name):
        key = '%s.%s' % (tenant_name, bd_name)
        if key in self.bridge_domain_node_mo:
            return self.bridge_domain_node_mo[key]

        cache = self.get_object_cache(
            'fvBD.%s' % (key)
        )
        if cache is not None:
            self.bridge_domain_node_mo[key] = cache
            self.log.apic_mo(
                'fvBD.%s' % (key),
                self.bridge_domain_node_mo[key]
            )
            return self.bridge_domain_node_mo[key]

        distinguished_name = 'uni/tn-%s/BD-%s' % (tenant_name, bd_name)
        query = 'rsp-subtree-include=full-deployment&target-node=all&target-path=BDToNwIf'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_bridge_domain_node_mo',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_bridge_domain_node_mo',
                'Unexpected object count'
            )
            return None

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fvBD']['attributes']
            attributes['pconsResourceCtx'] = self.get_mo_node_resource_ctx(
                'fvBD',
                managed_object
            )
            self.bridge_domain_node_mo[key] = attributes

        self.log.apic_mo(
            'fvBD.%s' % (key),
            self.bridge_domain_node_mo[key]
        )

        self.set_object_cache(
            'fvBD.%s' % (key),
            self.bridge_domain_node_mo[key]
        )

        return self.bridge_domain_node_mo[key]
