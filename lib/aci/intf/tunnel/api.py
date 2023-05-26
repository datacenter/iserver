class InterfaceTunnelApi():
    def __init__(self):
        self.interface_tunnel_mo = {}

    def get_interface_tunnel_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_tunnel_mo:
            return self.interface_tunnel_mo[key]

        class_name = 'topology/pod-%s/node-%s/tunnelIf' % (pod_id, node_id)
        managed_objects = self.get_class(
            class_name
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_tunnel_mo',
                'API failed'
            )
            return None

        self.interface_tunnel_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['tunnelIf']['attributes']
            self.interface_tunnel_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'tunnelIf.%s' % (key),
            self.interface_tunnel_mo[key]
        )

        return self.interface_tunnel_mo[key]
