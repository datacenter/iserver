class ProtocolLacpInstanceApi():
    def __init__(self):
        self.lacp_instance_mo = {}

    def get_protocol_lacp_instance_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.lacp_instance_mo:
            return self.lacp_instance_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/lacp/inst' % (pod_id, node_id)
        managed_objects = self.get_managed_object(
            distinguished_name
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_lacp_instance_mo',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_protocol_lacp_instance_mo',
                'Unexpected object count'
            )
            return None

        self.lacp_instance_mo[key] = managed_objects['imdata'][0]['lacpInst']['attributes']

        self.log.apic_mo(
            'lacpInst.%s' % (key),
            self.lacp_instance_mo[key]
        )

        return self.lacp_instance_mo[key]
