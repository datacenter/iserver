class InterfaceAdjacencyLacpApi():
    def __init__(self):
        self.adjacency_lacp_mo = {}

    def get_adjacency_lacp_mo(self, pod_id, node_id, interface_id):
        key = '%s.%s.%s' % (
            pod_id,
            node_id,
            interface_id
        )
        if key in self.adjacency_lacp_mo:
            return self.adjacency_lacp_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/lacp/inst/if-[%s]' % (
            pod_id,
            node_id,
            interface_id
        )

        query = 'query-target=children&target-subtree-class=lacpAdjEp'
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
            self.adjacency_lacp_mo[key].append(
                managed_object
            )

        self.log.apic_mo(
            'lacpAdjEp.%s' % (key),
            self.adjacency_lacp_mo[key]
        )

        return self.adjacency_lacp_mo[key]
