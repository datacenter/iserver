class K8sNimPipelineApi():
    def __init__(self):
        self.nim_pipeline_mo = None
        self.nim_pipeline_namespace_mo = {}

    def get_nim_pipeline_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.nim_pipeline_mo,
            self.nim_pipeline_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.nim_pipeline_mo, self.nim_pipeline_namespace_mo = self.get_namespaced_resources(
            'NIMPipeline', 
            'apps.nvidia.com/v1alpha1', 
            self.nim_pipeline_mo,
            self.nim_pipeline_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_nim_pipeline_mo(self, namespace, name):
        success, _ = self.delete_resource('NIMPipeline', 'apps.nvidia.com/v1alpha1', name, namespace=namespace)
        return success