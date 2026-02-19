import time
from lib import filter_helper


class K8sRouteInfo():
    def __init__(self):
        self.route = None

    def get_route_info(self, route_mo):
        if route_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            route_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(route_mo, 'spec')
        info['status'] = self.get(route_mo, 'status')

        info['route'] = self.get(route_mo, 'spec:host')
        info['service'] = None
        to_kind = self.get(route_mo, 'spec:to:kind')
        if to_kind == 'Service':
            info['service'] = self.get(route_mo, 'spec:to:name')

        info['ready'] = False
        info['readyTick'] = '\u2717'
        info['__Output']['phase'] = 'Red'
        info['__Output']['readyTick'] = 'Red'

        try:
            conditions_mo = route_mo['status']['ingress'][0]['conditions']
        except BaseException:
            conditions_mo = None

        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                if condition_mo['type'] == 'Admitted' and condition_mo['status'] == 'True':
                    info['ready'] = True
                    info['readyTick'] = '\u2713'
                    info['__Output']['readyTick'] = 'Green'
        
        return info

    def get_routes_info(self, cache_enabled=True):
        if cache_enabled:
            if self.route is not None:
                return self.route

        managed_objects = self.get_route_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.route = []
        for managed_object in managed_objects:
            route_info = {}
            route_info['info'] = self.get_route_info(
                managed_object
            )
            route_info['mo'] = managed_object
            self.route.append(
                route_info
            )

        return self.route

    def match_route(self, route_info, route_filter):
        if route_filter is None or len(route_filter) == 0:
            return True

        for ap_rule in route_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, route_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (route_info['namespace'], route_info['name'])):
                    return False

            if key == 'service':
                key_found = True
                if not filter_helper.match_string(value, route_info['service']):
                    return False                
                
            if not key_found:
                self.log.error(
                    'match_route',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_routes(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_routes = self.get_routes_info(cache_enabled=cache_enabled)
        if all_routes is None:
            return None

        routes = []

        for route_info in all_routes:
            if not self.match_route(route_info['info'], object_filter):
                continue

            if return_mo:
                routes.append(
                    route_info['mo']
                )
                continue

            routes.append(
                route_info['info']
            )

        return routes

    def is_route(self, namespace, name, cache_enabled=True):
        if self.get_route(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True
    
    def get_route(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        routes = self.get_routes(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if routes is None:
            return None

        if len(routes) == 1:
            return routes[0]

        return None

    def wait_route_ready(self, namespace, name, max_time=60):
        start_time = int(time.time())
        while True:
            info = self.get_route(
                namespace,
                name,
                cache_enabled=False
            )
            if info is not None:
                if info['ready']:
                    return True

            duration = int(time.time()) - start_time
            if duration > max_time:
                self.log.error(
                    'k8s.wait_route_ready',
                    'Max time reached: %s/%s' % (namespace, name)
                )
                return False

            time.sleep(5)
