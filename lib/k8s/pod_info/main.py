from lib.k8s.pod_info.api import K8sPodInfoApi
from lib.k8s.pod_info.info import K8sPodInfoInfo


class K8sPodInfo(
        K8sPodInfoApi,
        K8sPodInfoInfo
        ):
    def __init__(self):
        K8sPodInfoApi.__init__(self)
        K8sPodInfoInfo.__init__(self)
