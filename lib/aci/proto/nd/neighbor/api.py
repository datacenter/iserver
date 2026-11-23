class ProtocolNdNeighborApi():
    def __init__(self):
        self.nd_neighbor_mo = {}

    def get_protocol_nd_neighbor_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.nd_neighbor_mo:
            return self.nd_neighbor_mo[key]

        cache = self.get_object_cache(
            'ndAdjEp',
            object_selector=key
        )
        if cache is not None:
            self.nd_neighbor_mo[key] = cache
            self.log.apic_mo(
                'ndAdjEp.%s' % (key),
                self.nd_neighbor_mo[key]
            )
            return self.nd_neighbor_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/nd/inst' % (pod_id, node_id)
        query = 'query-target=subtree&target-subtree-class=ndAdjEp'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_nd_neighbor_mo',
                'API failed'
            )
            return None

        self.nd_neighbor_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.nd_neighbor_mo[key].append(
                managed_object['ndAdjEp']['attributes']
            )

        self.log.apic_mo(
            'ndAdjEp.%s' % (key),
            self.nd_neighbor_mo[key]
        )

        self.set_object_cache(
            'ndAdjEp',
            self.nd_neighbor_mo[key],
            object_selector=key
        )

        return self.nd_neighbor_mo[key]
