from lib.k8s.ingress.api import K8sIngressApi
from lib.k8s.ingress.info import K8sIngressInfo


class K8sIngress(
        K8sIngressApi,
        K8sIngressInfo
        ):
    def __init__(self):
        K8sIngressApi.__init__(self)
        K8sIngressInfo.__init__(self)
