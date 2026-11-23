from lib.k8s.role.api import K8sRoleApi
from lib.k8s.role.info import K8sRoleInfo
from lib.k8s.role.delete import K8sRoleDelete
from lib.k8s.role.wait import K8sRoleWait


class K8sRole(
        K8sRoleApi,
        K8sRoleInfo,
        K8sRoleDelete,
        K8sRoleWait
        ):
    def __init__(self):
        K8sRoleApi.__init__(self)
        K8sRoleInfo.__init__(self)
        K8sRoleDelete.__init__(self)
        K8sRoleWait.__init__(self)