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

        cache = self.get_object_cache(
            'tunnelIf',
            object_selector=key
        )
        if cache is not None:
            self.interface_tunnel_mo[key] = cache
            self.log.apic_mo(
                'tunnelIf.%s' % (key),
                self.interface_tunnel_mo[key]
            )
            return self.interface_tunnel_mo[key]

        class_name = 'topology/pod-%s/node-%s/tunnelIf' % (pod_id, node_id)
        query = 'rsp-subtree=children&rsp-subtree-include=health,fault-count,required'
        managed_objects = self.get_class(
            class_name,
            query=query
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
            attributes['healthInst'] = self.get_mo_child_attributes(
                'tunnelIf',
                managed_object,
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'tunnelIf',
                managed_object,
                'faultCounts'
            )
            self.interface_tunnel_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'tunnelIf.%s' % (key),
            self.interface_tunnel_mo[key]
        )

        self.set_object_cache(
            'tunnelIf',
            self.interface_tunnel_mo[key],
            object_selector=key
        )

        return self.interface_tunnel_mo[key]
