class ProtocolNdDomainApi():
    def __init__(self):
        self.nd_domain_mo = {}

    def get_protocol_nd_domain_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.nd_domain_mo:
            return self.nd_domain_mo[key]

        cache = self.get_object_cache(
            'ndDom',
            object_selector=key
        )
        if cache is not None:
            self.nd_domain_mo[key] = cache
            self.log.apic_mo(
                'ndDom.%s' % (key),
                self.nd_domain_mo[key]
            )
            return self.nd_domain_mo[key]

        class_name = 'topology/pod-%s/node-%s/ndDom' % (pod_id, node_id)
        managed_objects = self.get_class(
            class_name
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_nd_domain_mo',
                'API failed'
            )
            return None

        self.nd_domain_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.nd_domain_mo[key].append(
                managed_object['ndDom']['attributes']
            )

        self.log.apic_mo(
            'ndDom.%s' % (key),
            self.nd_domain_mo[key]
        )

        self.set_object_cache(
            'ndDom',
            self.nd_domain_mo[key],
            object_selector=key
        )

        return self.nd_domain_mo[key]
