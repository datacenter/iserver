class K8sCronJobInfo():
    def __init__(self):
        self.cron_job = None

    def get_cron_job_info(self, managed_object):
        info = self.get_base_info(
            managed_object
        )
        info['secret'] = self.get(managed_object, 'secrets', on_error=[], on_none=[])
        info['secretCount'] = len(info['secret'])
        return info

    def get_cron_jobs(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'cron_job', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def is_cron_job(self, namespace, name, cache_enabled=True):
        if self.get_cron_job(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True
    
    def get_cron_job(self, namespace, name, return_mo=False, cache_enabled=True):
        return self.get_info(
            'cron_job', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
