from lib.k8s.tuned.api import K8sTunedApi
from lib.k8s.tuned.info import K8sTunedInfo


class K8sTuned(
        K8sTunedApi,
        K8sTunedInfo
        ):
    def __init__(self):
        K8sTunedApi.__init__(self)
        K8sTunedInfo.__init__(self)
