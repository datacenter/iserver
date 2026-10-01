class K8sRouteWait():
    def __init__(self):
        pass

    def wait_route_ready(self, namespace, name, max_time=60, my_output=None, prompt='Route'):
        return self.wait_managed_object(
            'route',
            name,
            namespace=namespace,
            match_properties={'ready':True},
            my_output=my_output,
            prompt='Wait for %s %s/%s [timeout:%ss]' % (prompt, namespace, name, max_time),
            max_time=max_time
        )