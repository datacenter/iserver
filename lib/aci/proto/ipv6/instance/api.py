class ProtocolIpv6InstanceApi():
    def __init__(self):
        self.ipv6_instance_mo = {}

    def get_protocol_ipv6_instance_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.ipv6_instance_mo:
            return self.ipv6_instance_mo[key]

        cache = self.get_object_cache(
            'ipv6Inst',
            object_selector=key
        )
        if cache is not None:
            self.ipv6_instance_mo[key] = cache
            self.log.apic_mo(
                'ipv6Inst.%s' % (key),
                self.ipv6_instance_mo[key]
            )
            return self.ipv6_instance_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/ipv6' % (pod_id, node_id)
        query = 'query-target=children&rsp-subtree-include=health,fault-count'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_ipv6_instance_mo',
                'API failed'
            )
            return None

        if int(managed_objects['totalCount']) > 1:
            self.log.error(
                'get_protocol_ipv6_instance_mo',
                'Unexpected object count: %s' % (key)
            )
            return None

        if int(managed_objects['totalCount']) == 0:
            self.ipv6_instance_mo[key] = {}
        else:
            attributes = managed_objects['imdata'][0]['ipv6Inst']['attributes']
            attributes['healthInst'] = self.get_mo_child_attributes(
                'ipv6Inst',
                managed_objects['imdata'][0],
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'ipv6Inst',
                managed_objects['imdata'][0],
                'faultCounts'
            )
            self.ipv6_instance_mo[key] = attributes

        self.log.apic_mo(
            'ipv6Inst.%s' % (key),
            self.ipv6_instance_mo[key]
        )

        self.set_object_cache(
            'ipv6Inst',
            self.ipv6_instance_mo[key],
            object_selector=key
        )

        return self.ipv6_instance_mo[key]
