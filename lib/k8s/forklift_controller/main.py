from lib.k8s.forklift_controller.api import K8sForkliftControllerApi
from lib.k8s.forklift_controller.info import K8sForkliftControllerInfo
from lib.k8s.forklift_controller.create import K8sForkliftControllerCreate
from lib.k8s.forklift_controller.delete import K8sForkliftControllerDelete
from lib.k8s.forklift_controller.wait import K8sForkliftControllerWait


class K8sForkliftController(
        K8sForkliftControllerApi,
        K8sForkliftControllerInfo,
        K8sForkliftControllerCreate,
        K8sForkliftControllerDelete,
        K8sForkliftControllerWait
        ):
    def __init__(self):
        K8sForkliftControllerApi.__init__(self)
        K8sForkliftControllerInfo.__init__(self)
        K8sForkliftControllerCreate.__init__(self)
        K8sForkliftControllerDelete.__init__(self)
        K8sForkliftControllerWait.__init__(self)
