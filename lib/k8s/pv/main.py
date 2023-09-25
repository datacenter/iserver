from lib.k8s.pv.api import K8sPvApi
from lib.k8s.pv.info import K8sPvInfo


class K8sPv(
        K8sPvApi,
        K8sPvInfo
        ):
    def __init__(self):
        K8sPvApi.__init__(self)
        K8sPvInfo.__init__(self)
