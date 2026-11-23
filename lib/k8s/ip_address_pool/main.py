from lib.k8s.ip_address_pool.api import K8sIpAddressPoolApi
from lib.k8s.ip_address_pool.info import K8sIpAddressPoolInfo
from lib.k8s.ip_address_pool.create import K8sIpAddressPoolCreate
from lib.k8s.ip_address_pool.delete import K8sIpAddressPoolDelete
from lib.k8s.ip_address_pool.wait import K8sIpAddressPoolWait


class K8sIpAddressPool(
        K8sIpAddressPoolApi,
        K8sIpAddressPoolInfo,
        K8sIpAddressPoolCreate,
        K8sIpAddressPoolDelete,
        K8sIpAddressPoolWait
        ):
    def __init__(self):
        K8sIpAddressPoolApi.__init__(self)
        K8sIpAddressPoolInfo.__init__(self)
        K8sIpAddressPoolCreate.__init__(self)
        K8sIpAddressPoolDelete.__init__(self)
        K8sIpAddressPoolWait.__init__(self)
