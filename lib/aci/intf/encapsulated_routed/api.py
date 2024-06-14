class InterfaceEncapsulatedRoutedApi():
    def __init__(self):
        self.interface_encap_routed_mo = {}

    def get_interface_encap_routed_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_encap_routed_mo:
            return self.interface_encap_routed_mo[key]

        cache = self.get_object_cache(
            'l3EncRtdIf',
            object_selector=key
        )
        if cache is not None:
            self.interface_encap_routed_mo[key] = cache
            self.log.apic_mo(
                'l3EncRtdIf.%s' % (key),
                self.interface_encap_routed_mo[key]
            )
            return self.interface_encap_routed_mo[key]

        # https://<apic>/api/node/class/topology/pod-1/node-201/l3EncRtdIf.json?rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&subscription=yes&order-by=l3EncRtdIf.mplsEnable|asc&page=0&page-size=15&_dc=1683801093405

        class_name = 'topology/pod-%s/node-%s/l3EncRtdIf' % (pod_id, node_id)
        query = 'rsp-subtree=children&rsp-subtree-class=ethpmEncRtdIf&rsp-subtree-include=health,fault-count,required'
        managed_objects = self.get_class(
            class_name,
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_encap_routed_mo',
                'API failed'
            )
            return None

        self.log.apic_mo(
            'l3EncRtdIf.mo.%s' % (key),
            managed_objects
        )

        self.interface_encap_routed_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l3EncRtdIf']['attributes']
            attributes['ethpmEncRtdIf'] = self.get_mo_child_attributes(
                'l3EncRtdIf',
                managed_object,
                'ethpmEncRtdIf'
            )
            attributes['healthInst'] = self.get_mo_child_attributes(
                'l3EncRtdIf',
                managed_object,
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'l3EncRtdIf',
                managed_object,
                'faultCounts'
            )
            self.interface_encap_routed_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'l3EncRtdIf.%s' % (key),
            self.interface_encap_routed_mo[key]
        )

        self.set_object_cache(
            'l3EncRtdIf',
            self.interface_encap_routed_mo[key],
            object_selector=key
        )

        return self.interface_encap_routed_mo[key]
