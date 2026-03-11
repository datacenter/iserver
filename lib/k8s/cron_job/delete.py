class K8sCronJobDelete():
    def __init__(self):
        pass

    def delete_cron_job(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource(
            'CronJob', 
            'batch/v1',
            name, 
            namespace=namespace, 
            object_name='cron_job',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True
        
        success = self.wait_no_cron_job(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
                            
        return True
