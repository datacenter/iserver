class K8sJobDelete():
    def __init__(self):
        pass

    def delete_namespaced_jobs(self, namespace, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete namespaced jobs', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))

        jobs = self.get_jobs(
            object_filter=['namespace:%s' % (namespace)]
        )
        if jobs is None:
            if my_output is not None:
                my_output.error('REST API failed')
            return False
        
        for job in jobs:
            my_output.default('- %s' % (job['name']))
            success = self.delete_job_mo(job['namespace'], job['name'])
            if not success:
                if my_output is not None:
                    my_output.error('REST API failed')

                if wait:
                    if my_output is not None:
                        my_output.default('- wait for no job...')

                    if not self.wait_no_job(job['namespace'], job['name']):
                        if my_output is not None:
                            my_output.error('Timed out')
                        return False
                    
        return True