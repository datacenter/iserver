class K8sBfdProfileCreate():
    def __init__(self):
        pass

    def create_bfd_profile(self, body, my_output=None, confirmation=False, wait=True):
        if not self.create_resource(body, object_name='bfd_profile', my_output=my_output, confirmation=confirmation):
            return False
        
        if not wait:
            return True
        
        success = self.wait_bfd_profile(
            body['metadata']['namespace'],
            body['metadata']['name'],
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return True
    
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