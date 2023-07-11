class InterfaceSviEventApi():
    def __init__(self):
        self.interface_svi_event_mo = {}

    def get_interface_svi_event_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_svi_event_mo:
            return self.interface_svi_event_mo[key]

        cache = self.get_object_cache(
            'svi.eventLog',
            object_selector=key
        )
        if cache is not None:
            self.interface_svi_event_mo[key] = cache
            self.log.apic_mo(
                'svi.eventLog.%s' % (key),
                self.interface_svi_event_mo[key]
            )
            return self.interface_svi_event_mo[key]

        class_name = 'topology/pod-%s/node-%s/l2BD' % (pod_id, node_id)
        query = 'rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=event-logs,no-scoped,subtree'
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_svi_event_mo',
                'API failed'
            )
            return None

        self.interface_svi_event_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['eventRecord']['attributes']
            self.interface_svi_event_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'svi.eventLog.%s' % (key),
            self.interface_svi_event_mo[key]
        )

        self.set_object_cache(
            'svi.eventLog',
            self.interface_svi_event_mo[key],
            object_selector=key
        )

        return self.interface_svi_event_mo[key]
