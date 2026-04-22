class K8sServiceApi():
    def __init__(self):
        self.service_mo = None
        self.service_namespace_mo = {}

    def get_service_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.service_mo,
            self.service_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.service_mo, self.service_namespace_mo = self.get_namespaced_resources(
            'Service', 
            'v1', 
            self.service_mo,
            self.service_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_service_mo(self, namespace, name):
        return self.delete_resource('Service', 'v1', name, namespace=namespace)