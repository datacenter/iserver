from lib.k8s.cilium_load_balancer_ip_pool.api import CiliumLoadBalancerIpPoolApi
from lib.k8s.cilium_load_balancer_ip_pool.info import CiliumLoadBalancerIpPoolInfo
from lib.k8s.cilium_load_balancer_ip_pool.create import CiliumLoadBalancerIpPoolCreate
from lib.k8s.cilium_load_balancer_ip_pool.delete import CiliumLoadBalancerIpPoolDelete
from lib.k8s.cilium_load_balancer_ip_pool.wait import CiliumLoadBalancerIpPoolWait


class CiliumLoadBalancerIpPool(
        CiliumLoadBalancerIpPoolApi,
        CiliumLoadBalancerIpPoolInfo,
        CiliumLoadBalancerIpPoolCreate,
        CiliumLoadBalancerIpPoolDelete,
        CiliumLoadBalancerIpPoolWait
        ):
    def __init__(self):
        CiliumLoadBalancerIpPoolApi.__init__(self)
        CiliumLoadBalancerIpPoolInfo.__init__(self)
        CiliumLoadBalancerIpPoolCreate.__init__(self)
        CiliumLoadBalancerIpPoolDelete.__init__(self)
        CiliumLoadBalancerIpPoolWait.__init__(self)
