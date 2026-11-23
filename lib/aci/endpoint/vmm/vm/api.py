class EndpointVmmVmApi():
    def __init__(self):
        self.endpoint_vmm_vm_mo = None

    def get_endpoint_vmm_vm_mo(self):
        if self.endpoint_vmm_vm_mo is not None:
            return self.endpoint_vmm_vm_mo

        cache = self.get_object_cache(
            'compVm'
        )
        if cache is not None:
            self.endpoint_vmm_vm_mo = cache
            self.log.apic_mo(
                'compVm',
                self.endpoint_vmm_vm_mo
            )
            return self.endpoint_vmm_vm_mo

        managed_objects = self.get_class(
            'compVm'
        )
        if managed_objects is None:
            self.log.error(
                'get_endpoint_vmm_vm_mo',
                'API failed'
            )
            return None

        self.endpoint_vmm_vm_mo = []

        for managed_object in managed_objects['imdata']:
            attributes = managed_object['compVm']['attributes']
            self.endpoint_vmm_vm_mo.append(
                attributes
            )

        self.log.apic_mo(
            'compVm',
            self.endpoint_vmm_vm_mo
        )

        self.set_object_cache(
            'compVm',
            self.endpoint_vmm_vm_mo
        )

        return self.endpoint_vmm_vm_mo
