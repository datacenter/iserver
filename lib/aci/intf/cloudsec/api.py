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

        distinguished_name = 'topology/pod-%s/node-%s' % (pod_id, node_id)
        query = 'query-target=subtree&target-subtree-class=cloudsecIf'
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
            self.interface_cloudsec_mo[key].append(
                attributes
            )

        self.log.apic_mo(
            'cloudsecIf.%s' % (key),
            self.interface_cloudsec_mo[key]
        )

        return self.interface_cloudsec_mo[key]
