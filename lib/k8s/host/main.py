from lib.k8s.host.api import K8sHostApi
from lib.k8s.host.info import K8sHostInfo


class K8sHost(
        K8sHostApi,
        K8sHostInfo,
        ):
    def __init__(self):
        K8sHostApi.__init__(self)
        K8sHostInfo.__init__(self)

