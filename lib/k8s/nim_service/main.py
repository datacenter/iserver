from lib.k8s.nim_service.api import K8sNimServiceApi
from lib.k8s.nim_service.info import K8sNimServiceInfo
from lib.k8s.nim_service.create import K8sNimServiceCreate
from lib.k8s.nim_service.delete import K8sNimServiceDelete
from lib.k8s.nim_service.wait import K8sNimServiceWait


class K8sNimService(
        K8sNimServiceApi,
        K8sNimServiceInfo,
        K8sNimServiceCreate,
        K8sNimServiceDelete,
        K8sNimServiceWait
        ):
    def __init__(self):
        K8sNimServiceApi.__init__(self)
        K8sNimServiceInfo.__init__(self)
        K8sNimServiceCreate.__init__(self)
        K8sNimServiceDelete.__init__(self)
        K8sNimServiceWait.__init__(self)
