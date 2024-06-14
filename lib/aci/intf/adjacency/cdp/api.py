class InterfaceAdjacencyCdpApi():
    def __init__(self):
        self.adjacency_cdp_mo = {}

    def get_adjacency_cdp_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.adjacency_cdp_mo:
            return self.adjacency_cdp_mo[key]

        cache = self.get_object_cache(
            'cdpAdjEp',
            object_selector=key
        )
        if cache is not None:
            self.adjacency_cdp_mo[key] = cache
            self.log.apic_mo(
                'cdpAdjEp.%s' % (key),
                self.adjacency_cdp_mo[key]
            )
            return self.adjacency_cdp_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/cdp/inst' % (
            pod_id,
            node_id
        )

        query = 'query-target=subtree&target-subtree-class=cdpAdjEp&rsp-subtree-include=fault-count'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_adjacency_cdp_mo',
                'API failed'
            )
            return None

        self.adjacency_cdp_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['cdpAdjEp']['attributes']
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'cdpAdjEp',
                managed_object,
                'faultCounts'
            )
            self.adjacency_cdp_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'cdpAdjEp.%s' % (key),
            self.adjacency_cdp_mo[key]
        )

        self.set_object_cache(
            'cdpAdjEp',
            self.adjacency_cdp_mo[key],
            object_selector=key
        )

        return self.adjacency_cdp_mo[key]
