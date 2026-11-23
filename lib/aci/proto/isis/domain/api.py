class ProtocolIsisDomainApi():
    def __init__(self):
        self.isis_domains_mo = {}

    def get_protocol_isis_domains_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.isis_domains_mo:
            return self.isis_domains_mo[key]

        cache = self.get_object_cache(
            'isisDom',
            object_selector=key
        )
        if cache is not None:
            self.isis_domains_mo[key] = cache
            self.log.apic_mo(
                'isisDom.%s' % (key),
                self.isis_domains_mo[key]
            )
            return self.isis_domains_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/isis' % (pod_id, node_id)
        query = 'query-target=subtree&target-subtree-class=isisDom'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_isis_domains_mo',
                'API failed'
            )
            return None

        self.isis_domains_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.isis_domains_mo[key].append(
                managed_object['isisDom']['attributes']
            )

        self.log.apic_mo(
            'isisDom.%s' % (key),
            self.isis_domains_mo[key]
        )

        self.set_object_cache(
            'isisDom',
            self.isis_domains_mo[key],
            object_selector=key
        )

        return self.isis_domains_mo[key]
