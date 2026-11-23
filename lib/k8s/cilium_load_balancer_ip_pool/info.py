class CiliumLoadBalancerIpPoolInfo():
    def __init__(self):
        self.cilium_load_balancer_ip_pool = None

    def get_cilium_load_balancer_ip_pool_info(self, managed_object):
        return self.get_base_info(managed_object)

    def get_cilium_load_balancer_ip_pools(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'cilium_load_balancer_ip_pool', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_cilium_load_balancer_ip_pool(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'cilium_load_balancer_ip_pool', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_cilium_load_balancer_ip_pool(self, name, cache_enabled=True, optimized=True):
        if self.get_cilium_load_balancer_ip_pool(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_cilium_load_balancer_ip_pool(self, cache_enabled=True):
        infos = self.get_cilium_load_balancer_ip_pools(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True