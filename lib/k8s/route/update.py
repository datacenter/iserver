class K8sRouteUpdate():
    def __init__(self):
        pass

    def update_route_security_mode(self, namespace, name, security_mode, confirmation=False, my_output=None, wait=True):
        route_mo = self.get_route(namespace, name, return_mo=True, optimized=True)
        if route_mo is None:
            if my_output is not None:
                my_output.error('Route not found: %s/%s' % (namespace, name))
            return False
        
        if security_mode:
            if self.get(route_mo, 'spec:tls:insecureEdgeTerminationPolicy') is None:
                if my_output is not None:
                    my_output.default('Route %s/%s %s' % (namespace, name, my_output.add_color('already secure', 'Green')))
                return True
            
            route_mo = self.cleanup_managed_object(route_mo, exclude=['resourceVersion'])
            del route_mo['spec']['tls']

            if not self.replace_resource(route_mo, object_name='route', my_output=my_output, confirmation=confirmation):
                return False
            
        if not security_mode:
            if self.get(route_mo, 'spec:tls:insecureEdgeTerminationPolicy') is not None:
                if my_output is not None:
                    my_output.default('Route %s/%s %s' % (namespace, name, my_output.add_color('already insecure', 'Green')))
                return True
            
            body = {}
            body['apiVersion'] = 'route.openshift.io/v1'
            body['kind'] = 'Route'
            body['metadata'] = {}
            body['metadata']['namespace'] = namespace
            body['metadata']['name'] = name
            body['metadata']['resourceVersion'] = route_mo['metadata']['resourceVersion']
            body['spec'] = {}
            body['spec']['tls'] = {}
            body['spec']['tls']['termination'] = 'edge'
            body['spec']['tls']['insecureEdgeTerminationPolicy'] = 'Allow'

            if not self.patch_resource(body, object_name='route', my_output=my_output, confirmation=confirmation):
                return False

        return True
