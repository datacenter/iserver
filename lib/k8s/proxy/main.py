from lib.k8s.proxy.api import K8sProxyApi
from lib.k8s.proxy.info import K8sProxyInfo
from lib.k8s.proxy.noproxy import K8sProxyNoproxy
from lib.k8s.proxy.update import K8sProxyUpdate
from lib.k8s.proxy.wait import K8sProxyWait


class K8sProxy(
        K8sProxyApi,
        K8sProxyInfo,
        K8sProxyNoproxy,
        K8sProxyUpdate,
        K8sProxyWait
        ):
    def __init__(self):
        K8sProxyApi.__init__(self)
        K8sProxyInfo.__init__(self)
        K8sProxyNoproxy.__init__(self)
        K8sProxyUpdate.__init__(self)
        K8sProxyWait.__init__(self)
