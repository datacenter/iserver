class K8sCronJobUpdate():
    def __init__(self):
        pass

    def update_cron_job(
            self, 
            namespace, 
            name, 
            schedule,
            job, 
            confirmation=False, 
            my_output=None
        ):
        cron_job_mo = self.get_cron_job(namespace, name, return_mo=True, cache_enabled=False)
        if cron_job_mo is None:
            if my_output is not None:
                my_output.error('CronJob not found')
            return False

        cron_job_mo['spec']['schedule'] = schedule
        cron_job_mo['spec']['jobTemplate']['spec']['template']['spec'] = job
        cron_job_mo = self.cleanup_managed_object(cron_job_mo, exclude=['resourceVersion'])
        return self.replace_resource(cron_job_mo, object_name='cron_job', my_output=my_output, confirmation=confirmation)
