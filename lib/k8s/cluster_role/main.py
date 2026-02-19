from lib.k8s.cluster_role.api import K8sClusterRoleApi
from lib.k8s.cluster_role.info import K8sClusterRoleInfo


class K8sClusterRole(
        K8sClusterRoleApi,
        K8sClusterRoleInfo
        ):
    def __init__(self):
        K8sClusterRoleApi.__init__(self)
        K8sClusterRoleInfo.__init__(self)
