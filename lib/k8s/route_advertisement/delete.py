class K8sRouteAdvertisementDelete():
    def __init__(self):
        pass

    def delete_route_advertisement(self, name, my_output=None, wait=True):
        success = self.delete_resource(
            'RouteAdvertisements', 
            'k8s.ovn.org/v1',
            name, 
            object_name='route_advertisement',
            my_output=my_output
        )
        if not success:
            return False
        
        if not wait:
            return True
        
        success = self.wait_no_route_advertisement(
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False
                            
        return True
