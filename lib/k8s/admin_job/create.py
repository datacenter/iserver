class K8sAdminJobCreate():
    def __init__(self):
        pass

    def create_admin_job(self, body, my_output=None, confirmation=False, wait=True):
        success = self.create_resource_and_wait(
            body, 
            'admin_job', 
            wait=wait,
            my_output=my_output, 
            confirmation=confirmation
        )
        if not success:
            return False

        return True    