from lib.k8s.pod.api import K8sPodApi
from lib.k8s.pod.info import K8sPodInfo
from lib.k8s.pod.object import K8sPodObject
from lib.k8s.pod.task import K8sPodTask


class K8sPod(K8sPodApi, K8sPodInfo, K8sPodObject, K8sPodTask):
    def __init__(self):
        K8sPodApi.__init__(self)
        K8sPodInfo.__init__(self)
        K8sPodObject.__init__(self)
        K8sPodTask.__init__(self)
