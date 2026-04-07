class K8sRouteAdvertisementCreate():
    def __init__(self):
        pass

    def create_route_advertisement(self, body, confirmation=False, my_output=None, wait=True):
        name = self.get(body, 'metadata:name')

        if not self.create_resource(body, object_name='route_advertisement', my_output=my_output, confirmation=confirmation):
            return None

        if not wait:
            return True

        success = self.wait_route_advertisement(
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
        
        return True

    def create_or_update_route_advertisement(self, body, confirmation=False, my_output=None, wait=True):
        name = self.get(body, 'metadata:name')

        if self.is_route_advertisement(name, cache_enabled=False):
            return self.update_route_advertisement(
                body,
                confirmation=confirmation, 
                my_output=my_output,
                wait=wait
            )

        return self.create_route_advertisement(
            body,
            confirmation=confirmation, 
            my_output=my_output,
            wait=wait
        )
