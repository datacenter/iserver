class EpgNodeApi():
    def __init__(self):
        self.epg_node_mo = {}

    def get_epg_node_mo(self, tenant_name, ap_name, epg_name):
        key = '%s.%s.%s' % (tenant_name, ap_name, epg_name)
        if key in self.epg_node_mo:
            return self.epg_node_mo[key]

        cache = self.get_object_cache(
            'fvAEPg.%s' % (key)
        )
        if cache is not None:
            self.epg_node_mo[key] = cache
            self.log.apic_mo(
                'fvAEPg.%s' % (key),
                self.epg_node_mo[key]
            )
            return self.epg_node_mo[key]

        distinguished_name = 'uni/tn-%s/ap-%s/epg-%s' % (tenant_name, ap_name, epg_name)
        query = 'rsp-subtree-include=full-deployment&target-node=all&target-path=EPgToNwIf'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_epg_node_mo',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_epg_node_mo',
                'Unexpected object count'
            )
            return None

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fvAEPg']['attributes']
            attributes['pconsResourceCtx'] = self.get_mo_node_resource_ctx(
                'fvAEPg',
                managed_object
            )
            self.epg_node_mo[key] = attributes

        self.log.apic_mo(
            'fvAEPg.%s' % (key),
            self.epg_node_mo[key]
        )

        self.set_object_cache(
            'fvAEPg.%s' % (key),
            self.epg_node_mo[key]
        )

        return self.epg_node_mo[key]
