class ProtocolBfdInstanceApi():
    def __init__(self):
        self.bfd_instance_mo = {}

    def get_protocol_bfd_instance_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.bfd_instance_mo:
            return self.bfd_instance_mo[key]

        cache = self.get_object_cache(
            'bfdInst',
            object_selector=key
        )
        if cache is not None:
            self.bfd_instance_mo[key] = cache
            self.log.apic_mo(
                'bfdInst.%s' % (key),
                self.bfd_instance_mo[key]
            )
            return self.bfd_instance_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/bfd/inst' % (pod_id, node_id)
        managed_objects = self.get_managed_object(
            distinguished_name
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_bfd_instance_mo',
                'API failed'
            )
            return None

        if int(managed_objects['totalCount']) > 1:
            self.log.error(
                'get_protocol_bfd_instance_mo',
                'Unexpected object count: %s' % (key)
            )
            return None

        if int(managed_objects['totalCount']) == 0:
            self.bfd_instance_mo[key] = {}
        else:
            self.bfd_instance_mo[key] = managed_objects['imdata'][0]['bfdInst']['attributes']

        self.log.apic_mo(
            'bfdInst.%s' % (key),
            self.bfd_instance_mo[key]
        )

        self.set_object_cache(
            'bfdInst',
            self.bfd_instance_mo[key],
            object_selector=key
        )

        return self.bfd_instance_mo[key]
