class InterfaceAdjacencyLacpApi():
    def __init__(self):
        self.adjacency_lacp_mo = {}

    def get_adjacency_lacp_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.adjacency_lacp_mo:
            return self.adjacency_lacp_mo[key]

        cache = self.get_object_cache(
            'lacpAdjEp',
            object_selector=key
        )
        if cache is not None:
            self.adjacency_lacp_mo[key] = cache
            self.log.apic_mo(
                'lacpAdjEp.%s' % (key),
                self.adjacency_lacp_mo[key]
            )
            return self.adjacency_lacp_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/lacp/inst' % (
            pod_id,
            node_id
        )

        query = 'query-target=subtree&target-subtree-class=lacpAdjEp&rsp-subtree-include=fault-count'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_adjacency_lacp_mo',
                'API failed'
            )
            return None

        self.adjacency_lacp_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['lacpAdjEp']['attributes']
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'lacpAdjEp',
                managed_object,
                'faultCounts'
            )
            self.adjacency_lacp_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'lacpAdjEp.%s' % (key),
            self.adjacency_lacp_mo[key]
        )

        self.set_object_cache(
            'lacpAdjEp',
            self.adjacency_lacp_mo[key],
            object_selector=key
        )

        return self.adjacency_lacp_mo[key]
