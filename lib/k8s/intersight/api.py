class K8sIntersightApi():
    def __init__(self):
        self.intersight_mo = None
        self.intersight_namespace_mo = {}

    def get_intersight_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.intersight_mo,
            self.intersight_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.intersight_mo, self.intersight_namespace_mo = self.get_namespaced_resources(
            'CiscoIntersight', 
            'intersight.cisco.com/v1', 
            self.intersight_mo,
            self.intersight_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_intersight_mo(self, namespace, name):
        return self.delete_resource('CiscoIntersight', 'intersight.cisco.com/v1', name, namespace=namespace)
