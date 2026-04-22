class K8sRouteApi():
    def __init__(self):
        self.route_mo = None
        self.route_namespace_mo = {}

    def get_route_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.route_mo,
            self.route_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.route_mo, self.route_namespace_mo = self.get_namespaced_resources(
            'Route', 
            'route.openshift.io/v1', 
            self.route_mo,
            self.route_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_route_mo(self, namespace, name):
        return self.delete_resource('Route', 'route.openshift.io/v1', name, namespace=namespace)