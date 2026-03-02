from lib import filter_helper


class CiliumLoadBalancerIpPoolInfo():
    def __init__(self):
        self.cilium_load_balancer_ip_pool = None

    def get_cilium_load_balancer_ip_pool_info(self, cilium_load_balancer_ip_pool_mo):
        if cilium_load_balancer_ip_pool_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            cilium_load_balancer_ip_pool_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(cilium_load_balancer_ip_pool_mo, 'spec')
        info['status'] = self.get(cilium_load_balancer_ip_pool_mo, 'status')
        return info

    def get_cilium_load_balancer_ip_pools_info(self, cache_enabled=True):
        if cache_enabled:
            if self.cilium_load_balancer_ip_pool is not None:
                return self.cilium_load_balancer_ip_pool

        managed_objects = self.get_cilium_load_balancer_ip_pool_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cilium_load_balancer_ip_pool = []
        for managed_object in managed_objects:
            cilium_load_balancer_ip_pool_info = {}
            cilium_load_balancer_ip_pool_info['info'] = self.get_cilium_load_balancer_ip_pool_info(
                managed_object
            )
            cilium_load_balancer_ip_pool_info['mo'] = managed_object
            self.cilium_load_balancer_ip_pool.append(
                cilium_load_balancer_ip_pool_info
            )

        return self.cilium_load_balancer_ip_pool

    def match_cilium_load_balancer_ip_pool(self, cilium_load_balancer_ip_pool_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, cilium_load_balancer_ip_pool_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_cilium_load_balancer_ip_pool',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cilium_load_balancer_ip_pools(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_cilium_load_balancer_ip_pools = self.get_cilium_load_balancer_ip_pools_info(cache_enabled=cache_enabled)
        if all_cilium_load_balancer_ip_pools is None:
            return None

        cilium_load_balancer_ip_pools = []

        for cilium_load_balancer_ip_pool_info in all_cilium_load_balancer_ip_pools:
            if not self.match_cilium_load_balancer_ip_pool(cilium_load_balancer_ip_pool_info['info'], object_filter):
                continue

            if return_mo:
                cilium_load_balancer_ip_pools.append(
                    cilium_load_balancer_ip_pool_info['mo']
                )
                continue

            cilium_load_balancer_ip_pools.append(
                cilium_load_balancer_ip_pool_info['info']
            )

        return cilium_load_balancer_ip_pools

    def is_cilium_load_balancer_ip_pool(self, name, cache_enabled=True):
        if self.get_cilium_load_balancer_ip_pool(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_cilium_load_balancer_ip_pool(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        cilium_load_balancer_ip_pools = self.get_cilium_load_balancer_ip_pools(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if cilium_load_balancer_ip_pools is None:
            return None

        if len(cilium_load_balancer_ip_pools) == 1:
            return cilium_load_balancer_ip_pools[0]

        return None
