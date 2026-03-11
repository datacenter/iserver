class K8sCronJobWait():
    def __init__(self):
        pass

    def wait_cron_job(self, namespace, name, match_properties={}, break_properties={}, my_output=None, prompt='CronJob', max_time=60):
        return self.wait_managed_object(
            'cron_job',
            name,
            namespace=namespace,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='- wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )

    def wait_no_cron_job(self, namespace, name, max_time=60, my_output=None, prompt='CronJob'):
        return self.wait_no_managed_object(
            'cron_job',
            name,
            namespace=namespace,
            my_output=my_output,
            prompt='- wait for no %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )
