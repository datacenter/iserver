class InterfaceAdjacencyLldpApi():
    def __init__(self):
        self.adjacency_lldp_mo = {}

    def get_adjacency_lldp_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.adjacency_lldp_mo:
            return self.adjacency_lldp_mo[key]

        cache = self.get_object_cache(
            'lldpAdjEp',
            object_selector=key
        )
        if cache is not None:
            self.adjacency_lldp_mo[key] = cache
            self.log.apic_mo(
                'lldpAdjEp.%s' % (key),
                self.adjacency_lldp_mo[key]
            )
            return self.adjacency_lldp_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/lldp/inst' % (
            pod_id,
            node_id
        )

        query = 'query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query

        )

        if managed_objects is None:
            self.log.error(
                'get_adjacency_lldp_mo',
                'API failed'
            )
            return None

        self.adjacency_lldp_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['lldpAdjEp']['attributes']
            attributes['healthInst'] = self.get_mo_child_attributes(
                'lldpAdjEp',
                managed_object,
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'lldpAdjEp',
                managed_object,
                'faultCounts'
            )
            self.adjacency_lldp_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'lldpAdjEp.%s' % (key),
            self.adjacency_lldp_mo[key]
        )

        self.set_object_cache(
            'lldpAdjEp',
            self.adjacency_lldp_mo[key],
            object_selector=key
        )

        return self.adjacency_lldp_mo[key]
