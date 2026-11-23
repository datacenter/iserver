from lib.k8s.cni.api import K8sCniApi
from lib.k8s.cni.info import K8sCniInfo


class K8sCni(
        K8sCniApi,
        K8sCniInfo
        ):
    def __init__(self):
        K8sCniApi.__init__(self)
        K8sCniInfo.__init__(self)
