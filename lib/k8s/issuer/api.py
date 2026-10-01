class K8sIssuerApi():
    def __init__(self):
        self.issuer_mo = None
        self.issuer_namespace_mo = {}

    def get_issuer_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.issuer_mo,
            self.issuer_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.issuer_mo, self.issuer_namespace_mo = self.get_namespaced_resources(
            'Issuer', 
            'cert-manager.io/v1', 
            self.issuer_mo,
            self.issuer_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_issuer_mo(self, namespace, name):
        success, _ = self.delete_resource('Issuer', 'cert-manager.io/v1', name, namespace=namespace)
        return success