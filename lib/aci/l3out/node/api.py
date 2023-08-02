class L3OutNodeApi():
    def __init__(self):
        self.l3out_node_mo = {}

    def get_l3out_node_mo(self, tenant_name, l3out_name):
        key = '%s.%s' % (tenant_name, l3out_name)
        if key in self.l3out_node_mo:
            return self.l3out_node_mo[key]

        cache = self.get_object_cache(
            'l3extOut.%s' % (key)
        )
        if cache is not None:
            self.l3out_node_mo[key] = cache
            self.log.apic_mo(
                'l3extOut.%s' % (key),
                self.l3out_node_mo[key]
            )
            return self.l3out_node_mo[key]

        distinguished_name = 'uni/tn-%s/l3out-%s' % (tenant_name, l3out_name)
        query = 'rsp-subtree-include=full-deployment&target-node=all&target-path=L3ExtOutToNwIf'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_l3out_node_mo',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_l3out_node_mo',
                'Unexpected object count'
            )
            return None

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l3extOut']['attributes']
            attributes['pconsResourceCtx'] = self.get_mo_node_resource_ctx(
                'l3extOut',
                managed_object
            )
            self.l3out_node_mo[key] = attributes

        self.log.apic_mo(
            'l3extOut.%s' % (key),
            self.l3out_node_mo[key]
        )

        self.set_object_cache(
            'l3extOut.%s' % (key),
            self.l3out_node_mo[key]
        )

        return self.l3out_node_mo[key]
