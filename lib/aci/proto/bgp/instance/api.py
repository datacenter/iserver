class ProtocolBgpInstanceApi():
    def __init__(self):
        self.bgp_instance_mo = {}

    def get_protocol_bgp_instance_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bgp_instance_mo:
            return self.bgp_instance_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/bgp/inst' % (pod_id, node_id)
        managed_objects = self.get_managed_object(
            distinguished_name
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_bgp_instance_mo',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_protocol_bgp_instance_mo',
                'Unexpected object count'
            )
            return None

        self.bgp_instance_mo[key] = managed_objects['imdata'][0]['bgpInst']['attributes']

        self.log.apic_mo(
            'bgp.instance.%s' % (key),
            self.bgp_instance_mo[key]
        )

        return self.bgp_instance_mo[key]
