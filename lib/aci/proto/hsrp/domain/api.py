class ProtocolHsrpDomainApi():
    def __init__(self):
        self.hsrp_domains_mo = {}

    def get_protocol_hsrp_domains_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.hsrp_domains_mo:
            return self.hsrp_domains_mo[key]

        class_name = 'topology/pod-%s/node-%s/hsrpDom' % (pod_id, node_id)
        managed_objects = self.get_class(
            class_name
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_hsrp_domains_mo',
                'API failed'
            )
            return None

        self.hsrp_domains_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.hsrp_domains_mo[key].append(
                managed_object['hsrpDom']['attributes']
            )

        self.log.apic_mo(
            'hsrpDom.%s' % (key),
            self.hsrp_domains_mo[key]
        )

        return self.hsrp_domains_mo[key]
