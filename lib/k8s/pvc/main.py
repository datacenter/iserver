from lib.k8s.pvc.api import K8sPvcApi
from lib.k8s.pvc.info import K8sPvcInfo
from lib.k8s.pvc.task.main import K8sPvcTask


class K8sPvc(
        K8sPvcApi,
        K8sPvcInfo,
        K8sPvcTask
        ):
    def __init__(self):
        K8sPvcApi.__init__(self)
        K8sPvcInfo.__init__(self)
        K8sPvcTask.__init__(self)
