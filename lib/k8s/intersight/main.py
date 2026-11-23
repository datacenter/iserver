from lib.k8s.intersight.api import K8sIntersightApi
from lib.k8s.intersight.info import K8sIntersightInfo
from lib.k8s.intersight.create import K8sIntersightCreate
from lib.k8s.intersight.delete import K8sIntersightDelete
from lib.k8s.intersight.update import K8sIntersightUpdate
from lib.k8s.intersight.wait import K8sIntersightWait


class K8sIntersight(
        K8sIntersightApi,
        K8sIntersightInfo,
        K8sIntersightCreate,
        K8sIntersightDelete,
        K8sIntersightUpdate,
        K8sIntersightWait
        ):
    def __init__(self):
        K8sIntersightApi.__init__(self)
        K8sIntersightInfo.__init__(self)
        K8sIntersightCreate.__init__(self)
        K8sIntersightDelete.__init__(self)
        K8sIntersightUpdate.__init__(self)
        K8sIntersightWait.__init__(self)
