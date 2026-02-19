class K8sAdminJobDelete():
    def __init__(self):
        self.admin_job = None

    def delete_admin_jobs(self, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete admin job', before_newline=True, underline=True)

        servings = self.get_admin_jobs(
            cache_enabled=False
        )
        if servings is None:
            if my_output is not None:
                my_output.error('Failed to get admin job')
            return False

        if len(servings) == 0:
            if my_output is not None:
                my_output.default('- no admin job found')
            return True
        
        for serving in servings:
            if my_output is not None:
                my_output.default('- %s' % (serving['namespace_name']))

            success = self.delete_admin_job_mo(
                serving['namespace'],
                serving['name']
            )
            if not success:
                if my_output is not None:
                    my_output.error('admin job delete failed')

                return False

            if wait:
                if my_output is not None:
                    my_output.default('- wait for no admin job')

                if not self.wait_no_admin_job(serving['namespace'], serving['name']):
                    if my_output is not None:
                        my_output.error('Time out')
                    return False
            
        return True
