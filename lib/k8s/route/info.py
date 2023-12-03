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
