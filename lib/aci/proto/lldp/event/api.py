class ProtocolLldpEventApi():
    def __init__(self):
        self.lldp_event_mo = {}

    def get_protocol_lldp_event_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.lldp_event_mo:
            return self.lldp_event_mo[key]

        cache = self.get_object_cache(
            'lldpInst.eventLog',
            object_selector=key
        )
        if cache is not None:
            self.lldp_event_mo[key] = cache
            self.log.apic_mo(
                'lldpInst.eventLog.%s' % (key),
                self.lldp_event_mo[key]
            )
            return self.lldp_event_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/lldp/inst' % (pod_id, node_id)
        query = 'rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=%s' % (self.api_event_limit)
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_lldp_event_mo',
                'API failed'
            )
            return None

        self.lldp_event_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['eventRecord']['attributes']
            self.lldp_event_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'lldpInst.eventLog.%s' % (key),
            self.lldp_event_mo[key]
        )

        self.set_object_cache(
            'lldpInst.eventLog',
            self.lldp_event_mo[key],
            object_selector=key
        )

        return self.lldp_event_mo[key]
