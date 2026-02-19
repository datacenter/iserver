from lib.k8s.aaq.api import K8sAaqApi
from lib.k8s.aaq.info import K8sAaqInfo


class K8sAaq(
        K8sAaqApi,
        K8sAaqInfo
        ):
    def __init__(self):
        K8sAaqApi.__init__(self)
        K8sAaqInfo.__init__(self)
