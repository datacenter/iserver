class K8sCronJobCreate():
    def __init__(self):
        pass

    def get_cron_job_body(
            self, 
            namespace,
            name,
            schedule,
            job,
            concurrency='Forbid',
            backoff=0,
            ttl=1800
        ):
        body = {}
        body['apiVersion'] = 'batch/v1'
        body['kind'] = 'CronJob'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        body['metadata']['name'] = name
        body['spec'] = {}
        body['spec']['schedule'] = schedule
        body['spec']['concurrencyPolicy'] = concurrency
        body['spec']['jobTemplate'] = {}
        body['spec']['jobTemplate']['spec'] = {}
        body['spec']['jobTemplate']['spec']['backoffLimit'] = backoff
        body['spec']['jobTemplate']['spec']['ttlSecondsAfterFinished'] = ttl
        body['spec']['jobTemplate']['spec']['template'] = dict(spec=job)
        return body

    def create_cron_job(
            self, 
            namespace,
            name,
            schedule,
            job,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        body = self.get_cron_job_body(
            namespace,
            name,
            schedule,
            job
        )
        if not self.create_resource(body, object_name='cron_job', my_output=my_output, confirmation=confirmation):
            return False
        
        if not wait:
            return True
        
        success = self.wait_cron_job(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return True

    def create_or_update_cron_job(
            self, 
            namespace, 
            name,
            schedule, 
            job,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if self.is_cron_job(namespace, name, cache_enabled=False):
            return self.update_cron_job(
                namespace, 
                name,
                schedule, 
                job,
                confirmation=confirmation, 
                my_output=my_output
            )
        
        return self.create_cron_job(
            namespace, 
            name,
            schedule, 
            job,
            confirmation=confirmation, 
            my_output=my_output,
            wait=wait
        )
    