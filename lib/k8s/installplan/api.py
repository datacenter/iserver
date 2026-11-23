class K8sInstallplanApi():
    def __init__(self):
        self.installplan_mo = None
        self.installplan_namespace_mo = {}

    def get_installplan_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.installplan_mo,
            self.installplan_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.installplan_mo, self.installplan_namespace_mo = self.get_namespaced_resources(
            'InstallPlan', 
            'operators.coreos.com/v1alpha1', 
            self.installplan_mo,
            self.installplan_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response