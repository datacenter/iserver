class InterfaceCloudSecApi():
    def __init__(self):
        self.interface_cloudsec_mo = {}

    def get_interface_cloudsec_mo(self, pod_id, node_id):
        key = '%s.%s' % (
            pod_id,
            node_id
        )
        if key in self.interface_cloudsec_mo:
            return self.interface_cloudsec_mo[key]

        cache = self.get_object_cache(
            'cloudsecIf',
            object_selector=key
        )
        if cache is not None:
            self.interface_cloudsec_mo[key] = cache
            self.log.apic_mo(
                'cloudsecIf.%s' % (key),
                self.interface_cloudsec_mo[key]
            )
            return self.interface_cloudsec_mo[key]

        distinguished_name = 'topology/pod-%s/node-%s' % (pod_id, node_id)
        query = 'query-target=children&target-subtree-class=cloudsecIf&rsp-subtree-include=health,fault-count,required'
        managed_objects = self.get_managed_object(
            distinguished_name,
            query=query
        )

        if managed_objects is None:
            self.log.error(
                'get_interface_cloudsec_mo',
                'API failed'
            )
            return None

        self.interface_cloudsec_mo[key] = []
        for managed_object in managed_objects['imdata']:
            attributes = managed_object['cloudsecIf']['attributes']
            attributes['healthInst'] = self.get_mo_child_attributes(
                'cloudsecIf',
                managed_object,
                'healthInst'
            )
            attributes['faultCounts'] = self.get_mo_child_attributes(
                'cloudsecIf',
                managed_object,
                'faultCounts'
            )
            self.interface_cloudsec_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'cloudsecIf.%s' % (key),
            self.interface_cloudsec_mo[key]
        )

        self.set_object_cache(
            'cloudsecIf',
            self.interface_cloudsec_mo[key],
            object_selector=key
        )

        return self.interface_cloudsec_mo[key]
