class K8sNamespaceApi():
    def __init__(self):
        self.namespace_mo = None

    def get_namespace_mo(self, name=None, cache_enabled=True, fast=False):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.namespace_mo
        )
        if cache_hit:
            return response

        response, self.namespace_mo = self.get_resources(
            'Namespace', 
            'v1', 
            self.namespace_mo,
            name=name,
            fast=fast
        )

        return response

    def delete_namespace_mo(self, name):
        success, _ = self.delete_resource('Namespace', 'v1', name, cluster_type='standard')
        return success
    
    def finalize_namespace_mo(self, body):
        api_handler = self.get_api()
        if api_handler is None:
            return False
        
        try:
            api_handler.replace_namespace_finalize(body['metadata']['name'], body)
            self.increase_change_counter()
        except BaseException:
            return False
        
        return True