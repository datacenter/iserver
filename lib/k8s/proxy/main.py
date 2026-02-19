from lib.k8s.proxy.api import K8sProxyApi
from lib.k8s.proxy.info import K8sProxyInfo


class K8sProxy(
        K8sProxyApi,
        K8sProxyInfo
        ):
    def __init__(self):
        K8sProxyApi.__init__(self)
        K8sProxyInfo.__init__(self)
