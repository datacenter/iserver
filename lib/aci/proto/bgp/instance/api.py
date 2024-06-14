class ProtocolBgpInstanceApi():
    def __init__(self):
        self.bgp_instance_mo = {}

    def get_protocol_bgp_instance_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bgp_instance_mo:
            return self.bgp_instance_mo[key]

        cache = self.get_object_cache(
            'bgpInst',
            object_selector=key
        )
        if cache is not None:
            self.bgp_instance_mo[key] = cache
            self.log.apic_mo(
                'bgpInst.%s' % (key),
                self.bgp_instance_mo[key]
            )
            return self.bgp_instance_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/bgp' % (pod_id, node_id)
        query = 'query-target=children&rsp-subtree-include=health,fault-count'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_bgp_instance_mo',
                'API failed'
            )
            return None

        if int(managed_objects['totalCount']) > 1:
            self.log.error(
                'get_protocol_bgp_instance_mo',
                'Unexpected object count: %s' % (key)
            )
            return None

        if int(managed_objects['totalCount']) == 0:
            self.bgp_instance_mo[key] = {}
        else:
            attributes = managed_objects['imdata'][0]['bgpInst']['attributes']
            attributes['healthInst'] = self.get_mo_child_attributes(
                'bgpInst',
                managed_objects['imdata'][0],
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'bgpInst',
                managed_objects['imdata'][0],
                'faultCounts'
            )
            self.bgp_instance_mo[key] = attributes

        self.log.apic_mo(
            'bgpInst.%s' % (key),
            self.bgp_instance_mo[key]
        )

        self.set_object_cache(
            'bgpInst',
            self.bgp_instance_mo[key],
            object_selector=key
        )

        return self.bgp_instance_mo[key]
