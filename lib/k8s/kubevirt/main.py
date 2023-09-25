from lib.k8s.kubevirt.api import K8sKubevirtApi
from lib.k8s.kubevirt.info import K8sKubevirtInfo


class K8sKubevirt(
        K8sKubevirtApi,
        K8sKubevirtInfo
        ):
    def __init__(self):
        K8sKubevirtApi.__init__(self)
        K8sKubevirtInfo.__init__(self)
