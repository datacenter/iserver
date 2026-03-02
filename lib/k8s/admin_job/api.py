class K8sAdminJobApi():
    def __init__(self):
        self.admin_job_mo = None
        self.admin_job_namespace_mo = {}

    def get_admin_job_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.admin_job_mo,
            self.admin_job_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.admin_job_mo, self.admin_job_namespace_mo = self.get_namespaced_resources(
            'AdminJob', 
            'aistor.min.io/v1alpha1', 
            self.admin_job_mo,
            self.admin_job_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_admin_job_mo(self, namespace, name):
        return self.delete_resource('AdminJob', 'aistor.min.io/v1alpha1', name, namespace=namespace)
