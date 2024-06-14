class ProtocolNdInterfaceApi():
    def __init__(self):
        self.nd_interface_mo = {}

    def get_protocol_nd_interface_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.nd_interface_mo:
            return self.nd_interface_mo[key]

        cache = self.get_object_cache(
            'ndIf',
            object_selector=key
        )
        if cache is not None:
            self.nd_interface_mo[key] = cache
            self.log.apic_mo(
                'ndIf.%s' % (key),
                self.nd_interface_mo[key]
            )
            return self.nd_interface_mo[key]

        # url: https://<apic>/api/node/class/topology/pod-1/node-201/ndIf.json?rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required
        class_name = 'topology/pod-%s/node-%s/ndIf' % (pod_id, node_id)
        query = 'rsp-subtree=children&rsp-subtree-class=ndIf,ndIfStats&rsp-subtree-include=required'
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_nd_interface_mo',
                'API failed'
            )
            return None

        self.nd_interface_mo[key] = []
        for managed_object in managed_objects['imdata']:
            if 'ndIf' in managed_object:
                nd_interface = managed_object['ndIf']['attributes']
                for child in managed_object['ndIf']['children']:
                    if 'ndIfStats' in child:
                        nd_interface['ndIfStats'] = child['ndIfStats']['attributes']

                self.nd_interface_mo[key].append(
                    nd_interface
                )

        self.log.apic_mo(
            'ndIf.%s' % (key),
            self.nd_interface_mo[key]
        )

        self.set_object_cache(
            'ndIf',
            self.nd_interface_mo[key],
            object_selector=key
        )

        return self.nd_interface_mo[key]
