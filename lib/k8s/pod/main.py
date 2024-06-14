from lib.k8s.pod.api import K8sPodApi
from lib.k8s.pod.info import K8sPodInfo


class K8sPod(
        K8sPodApi,
        K8sPodInfo
        ):
    def __init__(self):
        K8sPodApi.__init__(self)
        K8sPodInfo.__init__(self)
