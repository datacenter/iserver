class ProtocolBfdInterfaceApi():
    def __init__(self):
        self.bfd_interfaces_mo = {}

    def set_protocol_bfd_interface_mo(self, managed_object):
        # "dn": "topology/pod-1/node-2208/sys/bfd/inst/if-[vlan27]"

        interface_dn = managed_object['bfdIf']['attributes']['dn']
        pod_id = interface_dn.split('/')[1][4:]
        node_id = interface_dn.split('/')[2][5:]
        key = '%s.%s' % (pod_id, node_id)

        if key not in self.bfd_interfaces_mo:
            self.bfd_interfaces_mo[key] = []

        self.bfd_interfaces_mo[key].append(
            managed_object['bfdIf']['attributes']
        )

    def set_protocol_bfd_interface_log(self, key):
        if key not in self.bfd_interfaces_mo:
            return False

        self.log.apic_mo(
            'bfdIf.%s' % (key),
            self.bfd_interfaces_mo[key]
        )

        self.set_object_cache(
            'bfdIf',
            self.bfd_interfaces_mo[key],
            object_selector=key
        )

        return True

    def get_protocol_bfd_interfaces_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bfd_interfaces_mo:
            return self.bfd_interfaces_mo[key]

        cache = self.get_object_cache(
            'bfdIf',
            object_selector=key
        )
        if cache is not None:
            self.bfd_interfaces_mo[key] = cache
            self.log.apic_mo(
                'bfdIf.%s' % (key),
                self.bfd_interfaces_mo[key]
            )
            return self.bfd_interfaces_mo[key]

        # url: https://<apic>/api/node/mo/topology/pod-1/node-201/sys/bfd/inst.json?query-target=children&target-subtree-class=bfdIf&subscription=yes
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
            'bfdIf.%s' % (key),
            self.bfd_interfaces_mo[key]
        )

        self.set_object_cache(
            'bfdIf',
            self.bfd_interfaces_mo[key],
            object_selector=key
        )

        return self.bfd_interfaces_mo[key]
