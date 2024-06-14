class AddressIpv6Api():
    def __init__(self):
        self.node_address_ipv6_mo = {}

    def get_node_address_ipv6_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.node_address_ipv6_mo:
            return self.node_address_ipv6_mo[key]

        cache = self.get_object_cache(
            'ipv6Addr',
            object_selector=key
        )
        if cache is not None:
            self.node_address_ipv6_mo[key] = cache
            self.log.apic_mo(
                'ipv6Addr.%s' % (key),
                self.node_address_ipv6_mo[key]
            )
            return self.node_address_ipv6_mo[key]

        class_name = 'topology/pod-%s/node-%s/ipv6Addr' % (pod_id, node_id)
        managed_objects = self.get_class(
            class_name
        )

        if managed_objects is None:
            self.log.error(
                'get_node_address_ipv6_mo',
                'API failed'
            )
            return None

        self.node_address_ipv6_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.node_address_ipv6_mo[key].append(
                managed_object
            )

        self.log.apic_mo(
            'ipv6Addr.%s' % (key),
            self.node_address_ipv6_mo[key]
        )

        self.set_object_cache(
            'ipv6Addr',
            self.node_address_ipv6_mo[key],
            object_selector=key
        )

        return self.node_address_ipv6_mo[key]
