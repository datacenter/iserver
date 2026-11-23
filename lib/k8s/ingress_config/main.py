from lib.k8s.ingress_config.api import K8sIngressConfigApi
from lib.k8s.ingress_config.info import K8sIngressConfigInfo


class K8sIngressConfig(
        K8sIngressConfigApi,
        K8sIngressConfigInfo
        ):
    def __init__(self):
        K8sIngressConfigApi.__init__(self)
        K8sIngressConfigInfo.__init__(self)
