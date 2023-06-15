class ProtocolCdpInstanceApi():
    def __init__(self):
        self.cdp_instance_mo = {}

    def get_protocol_cdp_instance_mo(self, pod_id, node_id):
        key = '%s.%s' % (pod_id, node_id)
        if key in self.cdp_instance_mo:
            return self.cdp_instance_mo[key]

        cache = self.get_object_cache(
            'cdpInst',
            object_selector=key
        )
        if cache is not None:
            self.cdp_instance_mo[key] = cache
            self.log.apic_mo(
                'cdpInst.%s' % (key),
                self.cdp_instance_mo[key]
            )
            return self.cdp_instance_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/cdp/inst' % (pod_id, node_id)
        managed_objects = self.get_managed_object(
            distinguished_name
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_cdp_instance_mo',
                'API failed'
            )
            return None

        if int(managed_objects['totalCount']) > 1:
            self.log.error(
                'get_protocol_cdp_instance_mo',
                'Unexpected object count: %s' % (key)
            )
            return None

        if int(managed_objects['totalCount']) == 0:
            self.cdp_instance_mo[key] = {}
        else:
            self.cdp_instance_mo[key] = managed_objects['imdata'][0]['cdpInst']['attributes']

        self.log.apic_mo(
            'cdpInst.%s' % (key),
            self.cdp_instance_mo[key]
        )

        self.set_object_cache(
            'cdpInst',
            self.cdp_instance_mo[key],
            object_selector=key
        )

        return self.cdp_instance_mo[key]
