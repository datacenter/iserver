from lib.k8s.service.api import K8sServiceApi
from lib.k8s.service.info import K8sServiceInfo


class K8sService(K8sServiceApi, K8sServiceInfo):
    def __init__(self):
        K8sServiceApi.__init__(self)
        K8sServiceInfo.__init__(self)
