class ApplicationProfileNodeApi():
    def __init__(self):
        self.application_profile_node_mo = {}

    def get_application_profile_node_mo(self, tenant_name, ap_name):
        key = '%s.%s' % (tenant_name, ap_name)
        if key in self.application_profile_node_mo:
            return self.application_profile_node_mo[key]

        cache = self.get_object_cache(
            'fvAp.%s' % (key)
        )
        if cache is not None:
            self.application_profile_node_mo[key] = cache
            self.log.apic_mo(
                'fvAp.%s' % (key),
                self.application_profile_node_mo[key]
            )
            return self.application_profile_node_mo[key]

        distinguished_name = 'uni/tn-%s/ap-%s' % (tenant_name, ap_name)
        query = 'rsp-subtree-include=full-deployment&target-node=all&target-path=ApToNwIf'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_application_profile_node_mo',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_application_profile_node_mo',
                'Unexpected object count'
            )
            return None

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['fvAp']['attributes']
            attributes['pconsResourceCtx'] = self.get_mo_node_resource_ctx(
                'fvAp',
                managed_object
            )
            self.application_profile_node_mo[key] = attributes

        self.log.apic_mo(
            'fvAp.%s' % (key),
            self.application_profile_node_mo[key]
        )

        self.set_object_cache(
            'fvAp.%s' % (key),
            self.application_profile_node_mo[key]
        )

        return self.application_profile_node_mo[key]
