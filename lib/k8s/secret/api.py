class K8sSecretApi():
    def __init__(self):
        self.secret_mo = None
        self.secret_namespace_mo = {}

    def get_secret_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.secret_mo,
            self.secret_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.secret_mo, self.secret_namespace_mo = self.get_namespaced_resources(
            'Secret', 
            'v1', 
            self.secret_mo,
            self.secret_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_secret_mo(self, namespace, name):
        return self.delete_resource('Secret', 'v1', name, namespace=namespace)
