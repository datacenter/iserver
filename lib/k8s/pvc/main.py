from lib.k8s.pvc.api import K8sPvcApi
from lib.k8s.pvc.info import K8sPvcInfo
from lib.k8s.pvc.create import K8sPvcCreate
from lib.k8s.pvc.delete import K8sPvcDelete
from lib.k8s.pvc.wait import K8sPvcWait



class K8sPvc(
        K8sPvcApi,
        K8sPvcInfo,
        K8sPvcCreate,
        K8sPvcDelete,
        K8sPvcWait
        ):
    def __init__(self):
        K8sPvcApi.__init__(self)
        K8sPvcInfo.__init__(self)
        K8sPvcCreate.__init__(self)
        K8sPvcDelete.__init__(self)
        K8sPvcWait.__init__(self)
