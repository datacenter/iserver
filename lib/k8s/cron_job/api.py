class K8sCronJobApi():
    def __init__(self):
        self.cron_job_mo = None
        self.cron_job_namespace_mo = {}
        
    def get_cron_job_mo(self, namespace=None, name=None, cache_enabled=True):
        cache_hit, response = self.get_namespaced_cache(
            cache_enabled, 
            namespace, 
            name,
            self.cron_job_mo,
            self.cron_job_namespace_mo
        )
        if cache_hit:
            return response
                
        response, self.cron_job_mo, self.cron_job_namespace_mo = self.get_namespaced_resources(
            'CronJob', 
            'batch/v1', 
            self.cron_job_mo,
            self.cron_job_namespace_mo,
            namespace=namespace,
            name=name
        )

        return response

    def delete_cron_job_mo(self, namespace, name):
        return self.delete_resource('CronJob', 'batch/v1', name, namespace=namespace)