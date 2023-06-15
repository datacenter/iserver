class ProtocolCdpNeighborApi():
    def __init__(self):
        self.cdp_neighbors_mo = {}

    def get_protocol_cdp_neighbors_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.cdp_neighbors_mo:
            return self.cdp_neighbors_mo[key]

        cache = self.get_object_cache(
            'cdpAdjEp',
            object_selector=key
        )
        if cache is not None:
            self.cdp_neighbors_mo[key] = cache
            self.log.apic_mo(
                'cdpAdjEp.%s' % (key),
                self.cdp_neighbors_mo[key]
            )
            return self.cdp_neighbors_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/cdp/inst' % (pod_id, node_id)
        query = 'query-target=subtree&target-subtree-class=cdpAdjEp'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_cdp_neighbors_mo',
                'API failed'
            )
            return None

        self.cdp_neighbors_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.cdp_neighbors_mo[key].append(
                managed_object['cdpAdjEp']['attributes']
            )

        self.log.apic_mo(
            'cdpAdjEp.%s' % (key),
            self.cdp_neighbors_mo[key]
        )

        self.set_object_cache(
            'cdpAdjEp',
            self.cdp_neighbors_mo[key],
            object_selector=key
        )

        return self.cdp_neighbors_mo[key]
