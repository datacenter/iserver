class K8sPackageApi():
    def __init__(self):
        self.package_mo = None
        self.package_namespace_mo = {}

    def get_package_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.package_mo,
            self.package_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.package_mo, self.package_namespace_mo = self.get_namespaced_resources(
            'PackageManifest', 
            'packages.operators.coreos.com/v1', 
            self.package_mo,
            self.package_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response