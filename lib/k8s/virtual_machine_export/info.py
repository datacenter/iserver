class K8sVirtualMachineExportInfo():
    def __init__(self):
        self.virtual_machine_export = None

    def get_virtual_machine_export_info(self, managed_object):
        return self.get_base_info(managed_object)
        
    def get_virtual_machine_exports(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'virtual_machine_export', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_virtual_machine_export(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'virtual_machine_export', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_virtual_machine_export(self, name, cache_enabled=True, optimized=True):
        if self.get_virtual_machine_export(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_virtual_machine_export(self, cache_enabled=True):
        infos = self.get_virtual_machine_exports(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True