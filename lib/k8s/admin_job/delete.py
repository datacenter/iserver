class K8sAdminJobDelete():
    def __init__(self):
        pass

    def delete_admin_job(self, namespace, name, my_output=None, wait=True):
        success = self.delete_resource_and_wait(
            'AdminJob', 
            'aistor.min.io/v1alpha1',
            name, 
            'admin_job',
            namespace=namespace, 
            wait=wait, 
            max_time=60, 
            my_output=my_output
        )
        return success
    
    def delete_admin_jobs(self, my_output=None, wait=True):
        jobs = self.get_admin_jobs(
            cache_enabled=False
        )
        if jobs is None:
            if my_output is not None:
                my_output.error('Failed to get admin job')
            return False
        
        for job in jobs:
            success = self.delete_admin_job(
                job['namespace'],
                job['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                return False

        return True