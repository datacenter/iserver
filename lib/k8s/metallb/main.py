from lib.k8s.metallb.api import K8sMetalLbApi
from lib.k8s.metallb.info import K8sMetalLbInfo
from lib.k8s.metallb.create import K8sMetalLbCreate
from lib.k8s.metallb.delete import K8sMetalLbDelete
from lib.k8s.metallb.wait import K8sMetalLbWait


class K8sMetalLb(
        K8sMetalLbApi,
        K8sMetalLbInfo,
        K8sMetalLbCreate,
        K8sMetalLbDelete,
        K8sMetalLbWait
        ):
    def __init__(self):
        K8sMetalLbApi.__init__(self)
        K8sMetalLbInfo.__init__(self)
        K8sMetalLbCreate.__init__(self)
        K8sMetalLbDelete.__init__(self)
        K8sMetalLbWait.__init__(self)
