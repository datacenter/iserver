from lib.k8s.hyperconverged.api import K8sHyperConvergedApi
from lib.k8s.hyperconverged.info import K8sHyperConvergedInfo
from lib.k8s.hyperconverged.create import K8sHyperConvergedCreate
from lib.k8s.hyperconverged.delete import K8sHyperConvergedDelete
from lib.k8s.hyperconverged.patch import K8sHyperConvergedPatch
from lib.k8s.hyperconverged.wait import K8sHyperConvergedWait


class K8sHyperConverged(
        K8sHyperConvergedApi,
        K8sHyperConvergedInfo,
        K8sHyperConvergedCreate,
        K8sHyperConvergedDelete,
        K8sHyperConvergedPatch,
        K8sHyperConvergedWait
        ):
    def __init__(self):
        K8sHyperConvergedApi.__init__(self)
        K8sHyperConvergedInfo.__init__(self)
        K8sHyperConvergedCreate.__init__(self)
        K8sHyperConvergedDelete.__init__(self)
        K8sHyperConvergedPatch.__init__(self)
        K8sHyperConvergedWait.__init__(self)
