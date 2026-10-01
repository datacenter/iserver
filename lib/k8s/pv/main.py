from lib.k8s.pv.api import K8sPvApi
from lib.k8s.pv.info import K8sPvInfo
from lib.k8s.pv.delete import K8sPvDelete
from lib.k8s.pv.wait import K8sPvWait


class K8sPv(
        K8sPvApi,
        K8sPvInfo,
        K8sPvDelete,
        K8sPvWait
        ):
    def __init__(self):
        K8sPvApi.__init__(self)
        K8sPvInfo.__init__(self)
        K8sPvDelete.__init__(self)
        K8sPvWait.__init__(self)
