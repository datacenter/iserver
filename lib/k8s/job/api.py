class K8sJobApi():
    def __init__(self):
        self.job_mo = None
        self.job_namespace_mo = {}

    def get_job_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.job_mo,
            self.job_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.job_mo, self.job_namespace_mo = self.get_namespaced_resources(
            'Job', 
            'batch/v1', 
            self.job_mo,
            self.job_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_job_mo(self, namespace, name):
        success, _ = self.delete_resource('Job', 'batch/v1', name, namespace=namespace)
        return success