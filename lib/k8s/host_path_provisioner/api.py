class K8sHostPathProvisionerApi():
    def __init__(self):
        self.host_path_provisioner_mo = None

    def get_host_path_provisioner_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.host_path_provisioner_mo
        )
        if cache_hit:
            return response

        response, self.host_path_provisioner_mo = self.get_resources(
            'HostPathProvisioner', 
            'hostpathprovisioner.kubevirt.io/v1beta1', 
            self.host_path_provisioner_mo,
            name=name
        )

        return response