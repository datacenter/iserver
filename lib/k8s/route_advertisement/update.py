class K8sRouteAdvertisementUpdate():
    def __init__(self):
        pass

    def update_route_advertisement(self, body, confirmation=False, my_output=None, wait=True):
        if not self.replace_resource(body, object_name='route_advertisement', my_output=my_output, confirmation=confirmation):
            return False

        return True
