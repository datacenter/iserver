class ApplicationProfileEventApi():
    def __init__(self):
        self.application_profile_event_mo = None

    def get_application_profile_event_mo(self):
        if self.application_profile_event_mo is not None:
            return self.application_profile_event_mo

        cache = self.get_object_cache(
            'fvAp.eventLog'
        )
        if cache is not None:
            self.application_profile_event_mo = cache
            self.log.apic_mo(
                'fvAp.eventLog',
                self.application_profile_event_mo
            )
            return self.application_profile_event_mo

        query = 'rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=%s' % (self.api_event_limit)
        managed_objects = self.get_class(
            'fvAp',
            query=query,
            node_class=True
        )

        if managed_objects is None:
            self.log.error(
                'get_application_profile_event_mo',
                'API failed'
            )
            return None

        self.application_profile_event_mo = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['eventRecord']['attributes']
            self.application_profile_event_mo.append(
                attributes
            )

        self.log.apic_mo(
            'fvAp.eventLog',
            self.application_profile_event_mo
        )

        self.set_object_cache(
            'fvAp.eventLog',
            self.application_profile_event_mo
        )

        return self.application_profile_event_mo
