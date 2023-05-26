class ProtocolBgpDomainApi():
    def __init__(self):
        self.bgp_domains_mo = {}

    def get_protocol_bgp_domains_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bgp_domains_mo:
            return self.bgp_domains_mo[key]

        class_name = 'topology/pod-%s/node-%s/bgpDom' % (pod_id, node_id)
        managed_objects = self.get_class(
            class_name
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_bgp_domains_mo',
                'API failed'
            )
            return None

        self.bgp_domains_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.bgp_domains_mo[key].append(
                managed_object['bgpDom']['attributes']
            )

        self.log.apic_mo(
            'bgpDom.%s' % (key),
            self.bgp_domains_mo[key]
        )

        return self.bgp_domains_mo[key]
