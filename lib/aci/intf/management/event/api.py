class InterfaceManagementEventApi():
    def __init__(self):
        self.interface_management_event_mo = {}

    def get_interface_management_event_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.interface_management_event_mo:
            return self.interface_management_event_mo[key]

        cache = self.get_object_cache(
            'mgmtMgmtIf.eventLog',
            object_selector=key
        )
        if cache is not None:
            self.interface_management_event_mo[key] = cache
            self.log.apic_mo(
                'mgmtMgmtIf.eventLog.%s' % (key),
                self.interface_management_event_mo[key]
            )
            return self.interface_management_event_mo[key]

        class_name = 'topology/pod-%s/node-%s/mgmtMgmtIf' % (pod_id, node_id)
        query = 'rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=%s' % (self.api_event_limit)
        managed_objects = self.get_class(
            class_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_management_event_mo',
                'API failed'
            )
            return None

        self.interface_management_event_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['eventRecord']['attributes']
            self.interface_management_event_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'mgmtMgmtIf.eventLog.%s' % (key),
            self.interface_management_event_mo[key]
        )

        self.set_object_cache(
            'mgmtMgmtIf.eventLog',
            self.interface_management_event_mo[key],
            object_selector=key
        )

        return self.interface_management_event_mo[key]
