class K8sVirtualMachineInstancePresetApi():
    def __init__(self):
        self.virtual_machine_instance_preset_mo = None

    def get_virtual_machine_instance_preset_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.virtual_machine_instance_preset_mo
        )
        if cache_hit:
            return response

        response, self.virtual_machine_instance_preset_mo = self.get_resources(
            'VirtualMachineInstancePreset', 
            'kubevirt.io/v1', 
            self.virtual_machine_instance_preset_mo,
            name=name
        )

        return response