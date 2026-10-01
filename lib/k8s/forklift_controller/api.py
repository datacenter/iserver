class K8sForkliftControllerApi():
    def __init__(self):
        self.forklift_controller_mo = None
        self.forklift_controller_namespace_mo = {}

    def get_forklift_controller_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.forklift_controller_mo,
            self.forklift_controller_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.forklift_controller_mo, self.forklift_controller_namespace_mo = self.get_namespaced_resources(
            'ForkliftController', 
            'forklift.konveyor.io/v1beta1', 
            self.forklift_controller_mo,
            self.forklift_controller_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_forklift_controller_mo(self, namespace, name):
        success, _ = self.delete_resource('ForkliftController', 'forklift.konveyor.io/v1beta1', name, namespace=namespace)
        return success