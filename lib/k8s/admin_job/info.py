class K8sAdminJobInfo():
    def __init__(self):
        self.admin_job = None

    def get_admin_job_info(self, managed_object):
        return self.get_base_info(managed_object)
    
    def get_admin_jobs(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'admin_job', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_admin_job(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'admin_job', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_admin_job(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_admin_job(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_admin_job(self, cache_enabled=True):
        infos = self.get_admin_jobs(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True