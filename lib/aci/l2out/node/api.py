class L2OutNodeApi():
    def __init__(self):
        self.l2out_node_mo = {}

    def get_l2out_node_mo(self, tenant_name, l2out_name):
        key = '%s.%s' % (tenant_name, l2out_name)
        if key in self.l2out_node_mo:
            return self.l2out_node_mo[key]

        cache = self.get_object_cache(
            'l2extOut.%s' % (key)
        )
        if cache is not None:
            self.l2out_node_mo[key] = cache
            self.log.apic_mo(
                'l2extOut.%s' % (key),
                self.l2out_node_mo[key]
            )
            return self.l2out_node_mo[key]

        distinguished_name = 'uni/tn-%s/l2out-%s' % (tenant_name, l2out_name)
        query = 'rsp-subtree-include=full-deployment&target-node=all&target-path=L2ExtOutToNwIf'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_l2out_node_mo',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_l2out_node_mo',
                'Unexpected object count'
            )
            return None

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l2extOut']['attributes']
            attributes['pconsResourceCtx'] = self.get_mo_node_resource_ctx(
                'l2extOut',
                managed_object
            )
            self.l2out_node_mo[key] = attributes

        self.log.apic_mo(
            'l2extOut.%s' % (key),
            self.l2out_node_mo[key]
        )

        self.set_object_cache(
            'l2extOut.%s' % (key),
            self.l2out_node_mo[key]
        )

        return self.l2out_node_mo[key]
