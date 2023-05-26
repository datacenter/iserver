class InterfaceLacpInstanceApi():
    def __init__(self):
        self.lacp_instance_mo = {}

    def get_lacp_instance_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.lacp_instance_mo:
            return self.lacp_instance_mo[key]

        class_name = 'topology/pod-%s/node-%s/lacpInst' % (
            pod_id,
            node_id
        )

        managed_objects = self.get_class(
            class_name
        )

        if managed_objects is None:
            self.log.error(
                'get_lacp_instance_mo',
                'API failed'
            )
            return None

        if managed_objects['totalCount'] != '1':
            self.log.error(
                'get_lacp_instance_mo',
                'Unexpected object count'
            )
            return None

        self.lacp_instance_mo[key] = managed_objects['imdata'][0]['lacpInst']['attributes']

        self.log.apic_mo(
            'lacp.instance.%s' % (key),
            self.lacp_instance_mo[key]
        )

        return self.lacp_instance_mo[key]
