class K8sVirtualMachineExportApi():
    def __init__(self):
        self.virtual_machine_export_mo = None

    def get_virtual_machine_export_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.virtual_machine_export_mo
        )
        if cache_hit:
            return response

        response, self.virtual_machine_export_mo = self.get_resources(
            'VirtualMachineExport', 
            'export.kubevirt.io/v1alpha1', 
            self.virtual_machine_export_mo,
            name=name
        )

        return response