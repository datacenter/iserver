class K8sDeploymentApi():
    def __init__(self):
        self.deployment_mo = None
        self.deployment_namespace_mo = {}

    def get_deployment_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.deployment_mo,
            self.deployment_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.deployment_mo, self.deployment_namespace_mo = self.get_namespaced_resources(
            'Deployment', 
            'apps/v1', 
            self.deployment_mo,
            self.deployment_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_deployment_mo(self, namespace, name):
        return self.delete_resource('Deployment', 'apps/v1', name, namespace=namespace)
