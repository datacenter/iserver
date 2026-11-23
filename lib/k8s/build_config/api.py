class K8sBuildConfigApi():
    def __init__(self):
        self.build_config_mo = None
        self.build_config_namespace_mo = {}

    def get_build_config_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.build_config_mo,
            self.build_config_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.build_config_mo, self.build_config_namespace_mo = self.get_namespaced_resources(
            'BuildConfig', 
            'build.openshift.io/v1', 
            self.build_config_mo,
            self.build_config_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response
    
    def delete_build_config_mo(self, namespace, name):
        success, _ = self.delete_resource('BuildConfig', 'build.openshift.io/v1', name, namespace=namespace)
        return success