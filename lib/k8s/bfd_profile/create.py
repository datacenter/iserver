class K8sBfdProfileCreate():
    def __init__(self):
        pass

    def create_bfd_profile(self, body, my_output=None, confirmation=False, wait=True):
        success = self.create_resource_and_wait(
            body, 
            'bfd_profile', 
            wait=wait,
            my_output=my_output, 
            confirmation=confirmation
        )
        return success
    
    def create_or_update_bfd_profile(
            self, 
            body, 
            replace=True,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if self.is_bfd_profile(body['metadata']['namespace'], body['metadata']['name'], cache_enabled=False):
            return self.update_bfd_profile(
                body,
                replace=replace,
                confirmation=confirmation, 
                my_output=my_output
            )

        return self.create_bfd_profile(
            body,
            confirmation=confirmation, 
            my_output=my_output,
            wait=wait
        )