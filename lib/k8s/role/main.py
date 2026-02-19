from lib.k8s.role.api import K8sRoleApi
from lib.k8s.role.info import K8sRoleInfo


class K8sRole(
        K8sRoleApi,
        K8sRoleInfo
        ):
    def __init__(self):
        K8sRoleApi.__init__(self)
        K8sRoleInfo.__init__(self)
