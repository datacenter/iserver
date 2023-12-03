from lib import filter_helper


class K8sEgressRouterInfo():
    def __init__(self):
        self.egress_router = None

    def get_egress_router_info(self, egress_router_mo):
        if egress_router_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            egress_router_mo
        )
        info.update(metadata_info)

        return info

    def get_egress_routers_info(self, cache_enabled=True):
        if cache_enabled:
            if self.egress_router is not None:
                return self.egress_router

        managed_objects = self.get_egress_router_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.egress_router = []
        for managed_object in managed_objects:
            egress_router_info = {}
            egress_router_info['info'] = self.get_egress_router_info(
                managed_object
            )
            egress_router_info['mo'] = managed_object
            self.egress_router.append(
                egress_router_info
            )

        return self.egress_router

    def match_egress_router(self, egress_router_info, egress_router_filter):
        if egress_router_filter is None or len(egress_router_filter) == 0:
            return True

        for ap_rule in egress_router_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_egress_router',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_egress_routers(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_egress_routers = self.get_egress_routers_info(cache_enabled=cache_enabled)
        if all_egress_routers is None:
            return None

        egress_routers = []

        for egress_router_info in all_egress_routers:
            if not self.match_egress_router(egress_router_info['info'], object_filter):
                continue

            if return_mo:
                egress_routers.append(
                    egress_router_info['mo']
                )
                continue

            egress_routers.append(
                egress_router_info['info']
            )

        return egress_routers
