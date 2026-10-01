class K8sImageStreamApi():
    def __init__(self):
        self.image_stream_mo = None
        self.image_stream_namespace_mo = {}

    def get_image_stream_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.image_stream_mo,
            self.image_stream_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.image_stream_mo, self.image_stream_namespace_mo = self.get_namespaced_resources(
            'ImageStream', 
            'image.openshift.io/v1', 
            self.image_stream_mo,
            self.image_stream_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_image_stream_mo(self, namespace, name):
        success, _ = self.delete_resource('ImageStream', 'image.openshift.io/v1', name, namespace=namespace)
        return success