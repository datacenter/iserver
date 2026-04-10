class K8sBgpAdvertisementCreate():
    def __init__(self):
        pass

    def create_bgp_advertisement(self, body, my_output=None, confirmation=False, wait=True):
        if not self.create_resource(body, object_name='bgp_advertisement', my_output=my_output, confirmation=confirmation):
            return False
        
        if not wait:
            return True
        
        success = self.wait_bgp_advertisement(
            body['metadata']['namespace'],
            body['metadata']['name'],
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return True
    
    def create_or_update_bgp_advertisement(
            self, 
            body, 
            replace=True,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if self.is_bgp_advertisement(body['metadata']['namespace'], body['metadata']['name'], cache_enabled=False):
            return self.update_bgp_advertisement(
                body,
                replace=replace,
                confirmation=confirmation, 
                my_output=my_output
            )

        return self.create_bgp_advertisement(
            body,
            confirmation=confirmation, 
            my_output=my_output,
            wait=wait
        )