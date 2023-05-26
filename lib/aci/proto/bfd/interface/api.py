class ProtocolBfdInterfaceApi():
    def __init__(self):
        self.bfd_interfaces_mo = {}

    def get_protocol_bfd_interfaces_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bfd_interfaces_mo:
            return self.bfd_interfaces_mo[key]

        # url: https://apic11o-eu-spdc.cisco.com/api/node/mo/topology/pod-1/node-201/sys/bfd/inst.json?query-target=children&target-subtree-class=bfdIf&subscription=yes
        distinguished_name = 'topology/pod-%s/node-%s/sys/bfd/inst' % (pod_id, node_id)
        query = 'query-target=children&target-subtree-class=bfdIf'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_bfd_interfaces_mo',
                'API failed'
            )
            return None

        self.bfd_interfaces_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.bfd_interfaces_mo[key].append(
                managed_object['bfdIf']['attributes']
            )

        self.log.apic_mo(
            'bfd.interface.%s' % (key),
            self.bfd_interfaces_mo[key]
        )

        return self.bfd_interfaces_mo[key]
