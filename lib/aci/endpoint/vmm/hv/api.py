class EndpointVmmHvApi():
    def __init__(self):
        self.endpoint_vmm_hv_mo = None

    def get_endpoint_vmm_hv_mo(self):
        if self.endpoint_vmm_hv_mo is not None:
            return self.endpoint_vmm_hv_mo

        cache = self.get_object_cache(
            'compHv'
        )
        if cache is not None:
            self.endpoint_vmm_hv_mo = cache
            self.log.apic_mo(
                'compHv',
                self.endpoint_vmm_hv_mo
            )
            return self.endpoint_vmm_hv_mo

        managed_objects = self.get_class(
            'compHv'
        )
        if managed_objects is None:
            self.log.error(
                'get_endpoint_vmm_hv_mo',
                'API failed'
            )
            return None

        self.endpoint_vmm_hv_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['compHv']['attributes']
            self.endpoint_vmm_hv_mo.append(
                attributes
            )

        self.log.apic_mo(
            'compHv',
            self.endpoint_vmm_hv_mo
        )

        self.set_object_cache(
            'compHv',
            self.endpoint_vmm_hv_mo
        )

        return self.endpoint_vmm_hv_mo
