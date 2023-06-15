class ProtocolIsisLspApi():
    def __init__(self):
        self.isis_domain_lsps_mo = {}

    def get_protocol_isis_domain_lsps_mo(self, pod_id, node_id, instance_name, domain_name):
        key = '%s.%s.%s.%s' % (
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        if key in self.isis_domain_lsps_mo:
            return self.isis_domain_lsps_mo[key]

        cache = self.get_object_cache(
            'isisLspRec',
            object_selector=key
        )
        if cache is not None:
            self.isis_domain_lsps_mo[key] = cache
            self.log.apic_mo(
                'isisLspRec.%s' % (key),
                self.isis_domain_lsps_mo[key]
            )
            return self.isis_domain_lsps_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s/sys/isis/inst-%s/dom-%s' % (
            pod_id,
            node_id,
            instance_name,
            domain_name
        )
        query = 'query-target=subtree&target-subtree-class=isisLspRec'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query,
            node_mo=True
        )

        if managed_objects is None:
            self.log.error(
                'get_protocol_isis_domain_lsps_mo',
                'API failed'
            )
            return None

        self.isis_domain_lsps_mo[key] = []
        for managed_object in managed_objects['imdata']:
            self.isis_domain_lsps_mo[key].append(
                managed_object['isisLspRec']['attributes']
            )

        self.log.apic_mo(
            'isisLspRec.%s' % (key),
            self.isis_domain_lsps_mo[key]
        )

        self.set_object_cache(
            'isisLspRec',
            self.isis_domain_lsps_mo[key],
            object_selector=key
        )

        return self.isis_domain_lsps_mo[key]
