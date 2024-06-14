class ProtocolCdpInterfaceApi():
    def __init__(self):
        self.cdp_interfaces_mo = {}

    def get_protocol_cdp_interfaces_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.cdp_interfaces_mo:
            return self.cdp_interfaces_mo[key]

        cache = self.get_object_cache(
            'cdpIf',
            object_selector=key
        )
        if cache is not None:
            self.cdp_interfaces_mo[key] = cache
            self.log.apic_mo(
                'cdpIf.%s' % (key),
                self.cdp_interfaces_mo[key]
            )
            return self.cdp_interfaces_mo[key]

        # url: https://<apic>/api/node/class/topology/pod-1/node-201/cdpIf.json?rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
        class_name = 'topology/pod-%s/node-%s/cdpIf' % (pod_id, node_id)
        query = 'rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required'
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_cdp_interfaces_mo',
                'API failed'
            )
            return None

        self.cdp_interfaces_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['cdpIf']['attributes']
            attributes['stats'] = self.get_mo_child_attributes(
                'cdpIf',
                managed_object,
                'cdpIfStats'
            )

            self.cdp_interfaces_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'cdpIf.%s' % (key),
            self.cdp_interfaces_mo[key]
        )

        self.set_object_cache(
            'cdpIf',
            self.cdp_interfaces_mo[key],
            object_selector=key
        )

        return self.cdp_interfaces_mo[key]
