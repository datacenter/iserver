from lib import filter_helper


class K8sVirtualMachineRestoreInfo():
    def __init__(self):
        self.virtual_machine_restore = None

    def get_virtual_machine_restore_info(self, managed_object):
        return self.get_base_info(managed_object)
        
    def get_virtual_machine_restores(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'virtual_machine_restore', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_virtual_machine_restore(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'virtual_machine_restore', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_virtual_machine_restore(self, name, cache_enabled=True, optimized=True):
        if self.get_virtual_machine_restore(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_virtual_machine_restore(self, cache_enabled=True):
        infos = self.get_virtual_machine_restores(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True