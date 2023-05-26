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

        distinguished_name = 'topology/pod-%s/node-%s/sys/cdp/inst' % (
            pod_id,
            node_id
        )

        query = 'query-target=subtree&target-subtree-class=cdpAdjEp'
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
            self.adjacency_cdp_mo[key].append(
                managed_object['cdpAdjEp']['attributes']
            )

        self.log.apic_mo(
            'cdpAdjEp.%s' % (key),
            self.adjacency_cdp_mo[key]
        )

        return self.adjacency_cdp_mo[key]
