class K8sOpenstackVolumePopulatorApi():
    def __init__(self):
        self.openstack_volume_populator_mo = None

    def get_openstack_volume_populator_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.openstack_volume_populator_mo
        )
        if cache_hit:
            return response

        response, self.openstack_volume_populator_mo = self.get_resources(
            'OpenstackVolumePopulator', 
            'forklift.cdi.kubevirt.io/v1beta1', 
            self.openstack_volume_populator_mo,
            name=name
        )

        return response