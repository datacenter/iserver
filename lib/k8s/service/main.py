from lib.k8s.service.api import K8sServiceApi
from lib.k8s.service.info import K8sServiceInfo
from lib.k8s.service.cilium_timescape import K8sServiceCiliumTimescape
from lib.k8s.service.create import K8sServiceCreate
from lib.k8s.service.delete import K8sServiceDelete
from lib.k8s.service.wait import K8sServiceWait

class K8sService(
        K8sServiceApi, 
        K8sServiceInfo, 
        K8sServiceCiliumTimescape,
        K8sServiceCreate,
        K8sServiceDelete,
        K8sServiceWait
    ):
    def __init__(self):
        K8sServiceApi.__init__(self)
        K8sServiceInfo.__init__(self)
        K8sServiceCiliumTimescape.__init__(self)
        K8sServiceCreate.__init__(self)
        K8sServiceDelete.__init__(self)
        K8sServiceWait.__init__(self)
