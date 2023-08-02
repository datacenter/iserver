class VrfNodeApi():
    def __init__(self):
        self.vrf_node_mo = {}

    def get_vrf_node_mo(self, tenant_name, vrf_name):
        key = '%s.%s' % (tenant_name, vrf_name)
        if key in self.vrf_node_mo:
            return self.vrf_node_mo[key]

        cache = self.get_object_cache(
            'fvCtx.%s' % (key)
        )
        if cache is not None:
            self.vrf_node_mo[key] = cache
            self.log.apic_mo(
                'fvCtx.%s' % (key),
                self.vrf_node_mo[key]
            )
            return self.vrf_node_mo[key]

        distinguished_name = 'uni/tn-%s/ctx-%s' % (tenant_name, vrf_name)
        query = 'rsp-subtree-include=full-deployment&target-node=all&target-path=CtxToNwIf'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_vrf_node_mo',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_vrf_node_mo',
                'Unexpected object count'
            )
            return None

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fvCtx']['attributes']
            attributes['pconsResourceCtx'] = self.get_mo_node_resource_ctx(
                'fvCtx',
                managed_object
            )
            self.vrf_node_mo[key] = attributes

        self.log.apic_mo(
            'fvCtx.%s' % (key),
            self.vrf_node_mo[key]
        )

        self.set_object_cache(
            'fvCtx.%s' % (key),
            self.vrf_node_mo[key]
        )

        return self.vrf_node_mo[key]
