class K8sOvirtVolumePopulatorApi():
    def __init__(self):
        self.ovirt_volume_populator_mo = None

    def get_ovirt_volume_populator_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.ovirt_volume_populator_mo
        )
        if cache_hit:
            return response

        response, self.ovirt_volume_populator_mo = self.get_resources(
            'OvirtVolumePopulator', 
            'forklift.cdi.kubevirt.io/v1beta1', 
            self.ovirt_volume_populator_mo,
            name=name
        )

        return response