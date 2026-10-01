class K8sBgpPeerCreate():
    def __init__(self):
        pass

    def create_bgp_peer(self, body, my_output=None, confirmation=False, wait=True):
        success = self.create_resource_and_wait(
            body, 
            'bgp_peer', 
            wait=wait,
            my_output=my_output, 
            confirmation=confirmation
        )
        return success
    
    def create_or_update_bgp_peer(
            self, 
            body, 
            replace=True,
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if self.is_bgp_peer(body['metadata']['namespace'], body['metadata']['name'], cache_enabled=False):
            return self.update_bgp_peer(
                body,
                replace=replace,
                confirmation=confirmation, 
                my_output=my_output
            )

        return self.create_bgp_peer(
            body,
            confirmation=confirmation, 
            my_output=my_output,
            wait=wait
        )