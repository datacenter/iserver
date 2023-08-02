class InterfaceLoopbackApi():
    def __init__(self):
        self.interface_lb_mo = {}

    def get_interface_loopback_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_lb_mo:
            return self.interface_lb_mo[key]

        cache = self.get_object_cache(
            'l3LbRtdIf',
            object_selector=key
        )
        if cache is not None:
            self.interface_lb_mo[key] = cache
            self.log.apic_mo(
                'l3LbRtdIf.%s' % (key),
                self.interface_lb_mo[key]
            )
            return self.interface_lb_mo[key]

        class_name = 'topology/pod-%s/node-%s/l3LbRtdIf' % (pod_id, node_id)
        query = 'rsp-subtree=children&rsp-subtree-class=ethpmLbRtdIf&rsp-subtree-include=health,fault-count,required'

        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_loopback_mo',
                'API failed'
            )
            return None

        self.interface_lb_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['l3LbRtdIf']['attributes']
            attributes['ethpmLbRtdIf'] = self.get_mo_child_attributes(
                'l3LbRtdIf',
                managed_object,
                'ethpmLbRtdIf'
            )
            attributes['healthInst'] = self.get_mo_child_attributes(
                'l3LbRtdIf',
                managed_object,
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'l3LbRtdIf',
                managed_object,
                'faultCounts'
            )
            self.interface_lb_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'l3LbRtdIf.%s' % (key),
            self.interface_lb_mo[key]
        )

        self.set_object_cache(
            'l3LbRtdIf',
            self.interface_lb_mo[key],
            object_selector=key
        )

        return self.interface_lb_mo[key]
