class K8sIpAddressPoolApi():
    def __init__(self):
        self.ip_address_pool_mo = None
        self.ip_address_pool_namespace_mo = {}

    def get_ip_address_pool_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.ip_address_pool_mo,
            self.ip_address_pool_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.ip_address_pool_mo, self.ip_address_pool_namespace_mo = self.get_namespaced_resources(
            'IPAddressPool', 
            'metallb.io/v1beta1', 
            self.ip_address_pool_mo,
            self.ip_address_pool_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_ip_address_pool_mo(self, namespace, name):
        return self.delete_resource('IPAddressPool', 'metallb.io/v1beta1', name, namespace=namespace)
