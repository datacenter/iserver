class BridgeDomainEventApi():
    def __init__(self):
        self.bridge_domain_event_mo = None

    def get_bridge_domain_event_mo(self):
        if self.bridge_domain_event_mo is not None:
            return self.bridge_domain_event_mo

        cache = self.get_object_cache(
            'fvBD.eventLog'
        )
        if cache is not None:
            self.bridge_domain_event_mo = cache
            self.log.apic_mo(
                'fvBD.eventLog',
                self.bridge_domain_event_mo
            )
            return self.bridge_domain_event_mo

        query = 'rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=%s' % (self.api_event_limit)
        managed_objects = self.get_class(
            'fvBD',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_bridge_domain_event_mo',
                'API failed'
            )
            return None

        self.bridge_domain_event_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['eventRecord']['attributes']
            self.bridge_domain_event_mo.append(
                attributes
            )

        self.log.apic_mo(
            'fvBD.eventLog',
            self.bridge_domain_event_mo
        )

        self.set_object_cache(
            'fvBD.eventLog',
            self.bridge_domain_event_mo
        )

        return self.bridge_domain_event_mo
