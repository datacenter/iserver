class EndpointVmmVnicApi():
    def __init__(self):
        self.endpoint_vmm_vnic_mo = None

    def get_endpoint_vmm_vnic_mo(self):
        if self.endpoint_vmm_vnic_mo is not None:
            return self.endpoint_vmm_vnic_mo

        cache = self.get_object_cache(
            'compVNic'
        )
        if cache is not None:
            self.endpoint_vmm_vnic_mo = cache
            self.log.apic_mo(
                'compVNic',
                self.endpoint_vmm_vnic_mo
            )
            return self.endpoint_vmm_vnic_mo

        managed_objects = self.get_class(
            'compVNic'
        )
        if managed_objects is None:
            self.log.error(
                'get_endpoint_vmm_vnic_mo',
                'API failed'
            )
            return None

        self.endpoint_vmm_vnic_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['compVNic']['attributes']
            self.endpoint_vmm_vnic_mo.append(
                attributes
            )

        self.log.apic_mo(
            'compVNic',
            self.endpoint_vmm_vnic_mo
        )

        self.set_object_cache(
            'compVNic',
            self.endpoint_vmm_vnic_mo
        )

        return self.endpoint_vmm_vnic_mo
