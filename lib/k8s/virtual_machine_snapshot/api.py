class K8sVirtualMachineSnapshotApi():
    def __init__(self):
        self.virtual_machine_snapshot_mo = None

    def get_virtual_machine_snapshot_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.virtual_machine_snapshot_mo
        )
        if cache_hit:
            return response

        response, self.virtual_machine_snapshot_mo = self.get_resources(
            'VirtualMachineSnapshot', 
            'snapshot.kubevirt.io/v1alpha1', 
            self.virtual_machine_snapshot_mo,
            name=name
        )

        return response