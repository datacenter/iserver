class K8sCatalogSourceDelete():
    def __init__(self):
        pass

    def delete_catalog_source(self, namespace, name, my_output=None, wait=True):
        pods = self.get_pods(
            object_filter=['owner:%s' % ('CatalogSource/%s' % (name))],
            cache_enabled=False
        )
        if pods is None:
            if my_output is not None:
                my_output.error('Failed to get catalog source pods information')

        success = self.delete_resource_and_wait(
            'CatalogSource', 
            'operators.coreos.com/v1alpha1',
            name, 
            'catalog_source',
            namespace=namespace, 
            wait=wait, 
            max_time=60, 
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True
    
        for pod in pods:
            success = self.wait_no_pod(
                pod['namespace'], 
                pod['name'], 
                my_output=my_output
            )
            if not success:
                return False
            
        return True