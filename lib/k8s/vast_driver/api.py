class K8sVastDriverApi():
    def __init__(self):
        self.vast_driver_mo = None
        self.vast_driver_namespace_mo = {}

    def get_vast_driver_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.vast_driver_mo,
            self.vast_driver_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.vast_driver_mo, self.vast_driver_namespace_mo = self.get_namespaced_resources(
            'VastCSIDriver', 
            'storage.vastdata.com/v1', 
            self.vast_driver_mo,
            self.vast_driver_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_vast_driver_mo(self, namespace, name):
        return self.delete_resource('VastCSIDriver', 'storage.vastdata.com/v1', name, namespace=namespace)