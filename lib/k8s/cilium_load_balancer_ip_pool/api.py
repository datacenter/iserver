class CiliumLoadBalancerIpPoolApi():
    def __init__(self):
        self.cilium_load_balancer_ip_pool_mo = None

    def get_cilium_load_balancer_ip_pool_mo(self, name=None, cache_enabled=True):
        cache_hit, response = self.get_cache(
            cache_enabled, 
            name,
            self.cilium_load_balancer_ip_pool_mo
        )
        if cache_hit:
            return response

        response, self.cilium_load_balancer_ip_pool_mo = self.get_resources(
            'CiliumLoadBalancerIPPool', 
            'cilium.io/v2', 
            self.cilium_load_balancer_ip_pool_mo,
            name=name
        )

        return response

    def delete_cilium_load_balancer_ip_pool_mo(self, name):
        return self.delete_resource('CiliumLoadBalancerIPPool', 'cilium.io/v2', name)
    