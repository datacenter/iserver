class ProtocolIsisNeighborApi():
    def __init__(self):
        self.isis_domain_neighbors_mo = {}

    def get_protocol_isis_domain_neighbors_mo(self, pod_id, node_id, instance_name, domain_name):
        key = '%s.%s.%s.%s' % (
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        if key in self.isis_domain_neighbors_mo:
            return self.isis_domain_neighbors_mo[key]

        cache = self.get_object_cache(
            'isisAdjEp',
            object_selector=key
        )
        if cache is not None:
            self.isis_domain_neighbors_mo[key] = cache
            self.log.apic_mo(
                'isisAdjEp.%s' % (key),
                self.isis_domain_neighbors_mo[key]
            )
            return self.isis_domain_neighbors_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/isis/inst-%s/dom-%s' % (
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        query = 'query-target=subtree&target-subtree-class=isisAdjEp&rsp-subtree=children&rsp-subtree-class=isisPeerIpAddr'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_isis_domain_neighbors_mo',
                'API failed'
            )
            return None

        self.isis_domain_neighbors_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['isisAdjEp']['attributes']
            attributes['isisPeerIpAddr'] = self.get_mo_child_attributes(
                'isisAdjEp',
                managed_object,
                'isisPeerIpAddr'
            )
            self.isis_domain_neighbors_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'isisAdjEp.%s' % (key),
            self.isis_domain_neighbors_mo[key]
        )

        self.set_object_cache(
            'isisAdjEp',
            self.isis_domain_neighbors_mo[key],
            object_selector=key
        )

        return self.isis_domain_neighbors_mo[key]
