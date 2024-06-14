from lib.k8s.thanos_ruler.api import K8sThanosRulerApi
from lib.k8s.thanos_ruler.info import K8sThanosRulerInfo


class K8sThanosRuler(
        K8sThanosRulerApi,
        K8sThanosRulerInfo
        ):
    def __init__(self):
        K8sThanosRulerApi.__init__(self)
        K8sThanosRulerInfo.__init__(self)
