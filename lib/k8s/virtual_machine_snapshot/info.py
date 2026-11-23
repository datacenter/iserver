class K8sVirtualMachineSnapshotInfo():
    def __init__(self):
        self.virtual_machine_snapshot = None

    def get_virtual_machine_snapshot_info(self, managed_object):
        return self.get_base_info(managed_object)
        
    def get_virtual_machine_snapshots(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'virtual_machine_snapshot', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_virtual_machine_snapshot(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'virtual_machine_snapshot', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_virtual_machine_snapshot(self, name, cache_enabled=True, optimized=True):
        if self.get_virtual_machine_snapshot(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_virtual_machine_snapshot(self, cache_enabled=True):
        infos = self.get_virtual_machine_snapshots(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True