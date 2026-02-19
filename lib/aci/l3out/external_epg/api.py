class L3OutExternalEpgApi():
    def __init__(self):
        self.l3out_external_epg_mo = {}

    def init_l3out_external_epg_mo(self):
        self.l3out_external_epg_mo = {}

    def get_l3out_external_epg_mo(self, tenant_name, l3out_name, epg_name, cache_enabled=True):
        key = '%s.%s.%s' % (tenant_name, l3out_name, epg_name)
        if key in self.l3out_external_epg_mo:
            return self.l3out_external_epg_mo[key]

        if cache_enabled:
            cache = self.get_object_cache(
                'l3OutExternalEpg.%s' % (key)
            )
            if cache is not None:
                self.l3out_external_epg_mo[key] = cache
                self.log.apic_mo(
                    'l3OutExternalEpg.%s' % (key),
                    self.l3out_external_epg_mo[key]
                )
                return self.l3out_external_epg_mo[key]

        distinguished_name = 'uni/tn-%s/out-%s/instP-%s' % (tenant_name, l3out_name, epg_name)
        query = 'query-target=subtree&target-subtree-class=l3extSubnet'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_l3out_external_epg_mo',
                'API failed'
            )
            return None

        self.l3out_external_epg_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l3extSubnet']['attributes']

            self.l3out_external_epg_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'l3OutExternalEpg.%s' % (key),
            self.l3out_external_epg_mo[key]
        )

        self.set_object_cache(
            'l3OutExternalEpg.%s' % (key),
            self.l3out_external_epg_mo[key]
        )

        return self.l3out_external_epg_mo[key]
