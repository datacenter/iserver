from lib.k8s.cluster_role.api import K8sClusterRoleApi
from lib.k8s.cluster_role.info import K8sClusterRoleInfo
from lib.k8s.cluster_role.create import K8sClusterRoleCreate
from lib.k8s.cluster_role.delete import K8sClusterRoleDelete
from lib.k8s.cluster_role.match import K8sClusterRoleMatch
from lib.k8s.cluster_role.update import K8sClusterRoleUpdate
from lib.k8s.cluster_role.wait import K8sClusterRoleWait


class K8sClusterRole(
        K8sClusterRoleApi,
        K8sClusterRoleInfo,
        K8sClusterRoleCreate,
        K8sClusterRoleDelete,
        K8sClusterRoleMatch,
        K8sClusterRoleUpdate,
        K8sClusterRoleWait
        ):
    def __init__(self):
        K8sClusterRoleApi.__init__(self)
        K8sClusterRoleInfo.__init__(self)
        K8sClusterRoleCreate.__init__(self)
        K8sClusterRoleDelete.__init__(self)
        K8sClusterRoleMatch.__init__(self)
        K8sClusterRoleUpdate.__init__(self)
        K8sClusterRoleWait.__init__(self)
