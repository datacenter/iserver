class SystemFaultApi():
    def __init__(self):
        self.system_fault_mo = None

    def get_system_fault_mo(self):
        if self.system_fault_mo is not None:
            return self.system_fault_mo

        cache = self.get_object_cache(
            'faultInst'
        )
        if cache is not None:
            self.system_fault_mo = cache
            self.log.apic_mo(
                'faultInst',
                self.system_fault_mo
            )
            return self.system_fault_mo

        managed_objects = self.get_class(
            'faultInst',
            node_class=True
        )
        if managed_objects is None:
            return None

        self.system_fault_mo = []
        for managed_object in managed_objects['imdata']:
            self.system_fault_mo.append(
                managed_object['faultInst']['attributes']
            )

        self.log.apic_mo(
            'faultInst',
            self.system_fault_mo
        )

        self.set_object_cache(
            'faultInst',
            self.system_fault_mo
        )

        return self.system_fault_mo
