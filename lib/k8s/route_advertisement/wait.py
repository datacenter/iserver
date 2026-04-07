class K8sRouteAdvertisementWait():
    def __init__(self):
        pass

    def wait_route_advertisement(self, name, match_properties={}, break_properties={}, my_output=None, prompt='RouteAdvertisement', max_time=60):
        return self.wait_managed_object(
            'route_advertisement',
            name,
            match_properties=match_properties,
            break_properties=break_properties,
            my_output=my_output,
            prompt='- wait for %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )

    def wait_no_route_advertisement(self, name, max_time=60, my_output=None, prompt='RouteAdvertisement'):
        return self.wait_no_managed_object(
            'route_advertisement',
            name,
            my_output=my_output,
            prompt='- wait for no %s %s [timeout:%ss]' % (prompt, name, max_time),
            max_time=max_time
        )
