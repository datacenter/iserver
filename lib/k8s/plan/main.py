from lib.k8s.plan.api import K8sPlanApi
from lib.k8s.plan.info import K8sPlanInfo
from lib.k8s.plan.create import K8sPlanCreate
from lib.k8s.plan.delete import K8sPlanDelete
from lib.k8s.plan.wait import K8sPlanWait


class K8sPlan(
        K8sPlanApi,
        K8sPlanInfo,
        K8sPlanCreate,
        K8sPlanDelete,
        K8sPlanWait
        ):
    def __init__(self):
        K8sPlanApi.__init__(self)
        K8sPlanInfo.__init__(self)
        K8sPlanCreate.__init__(self)
        K8sPlanDelete.__init__(self)
        K8sPlanWait.__init__(self)
