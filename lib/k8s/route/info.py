class K8sRouteInfo():
    def __init__(self):
        self.route = None

    def get_route_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)

        info['route'] = self.get(managed_object, 'spec:host')
        info['service'] = None
        to_kind = self.get(managed_object, 'spec:to:kind')
        if to_kind == 'Service':
            info['service'] = self.get(managed_object, 'spec:to:name')

        info = self.add_tick(
            info, 
            'spec:tls:insecureEdgeTerminationPolicy', 
            'Allow', 
            'insecureT', 
            bool_attribute='insecure'
        )

        info['ready'] = False
        info['readyTick'] = '\u2717'
        info['__Output']['phase'] = 'Red'
        info['__Output']['readyTick'] = 'Red'

        try:
            conditions_mo = managed_object['status']['ingress'][0]['conditions']
        except BaseException:
            conditions_mo = None

        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                if condition_mo['type'] == 'Admitted' and condition_mo['status'] == 'True':
                    info['ready'] = True
                    info['readyTick'] = '\u2713'
                    info['__Output']['readyTick'] = 'Green'
        
        return info

    def get_routes(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'route', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos
    
    def is_route(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_route(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True
    
    def get_route(self, namespace, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'route', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )
    

