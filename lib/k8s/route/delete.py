class K8sRouteDelete():
    def __init__(self):
        pass

    def delete_route(self, namespace, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Route', before_newline=True, underline=True)
            my_output.default('- namespace: %s' % (namespace))
            my_output.default('- name: %s' % (name))

        info = self.get_route(namespace, name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True

        if not self.delete_route_mo(info['namespace'], info['name']):
            if my_output is not None:
                my_output.error('Failed to delete route')
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no route')

            if not self.wait_no_route(info['namespace'], info['name']):
                if my_output is not None:
                    my_output.error('Timed out')
                return False

        return True

    def delete_namespaced_routes(self, namespace, my_output=None, wait=True):
        routes = self.get_routes(object_filter=['namespace:%s' % (namespace)], cache_enabled=False)
        if routes is None:
            if my_output is not None:
                my_output.error('Failed to get routes')
            return False

        for route in routes:
            success = self.delete_route(
                route['namespace'],
                route['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                return False

        return True