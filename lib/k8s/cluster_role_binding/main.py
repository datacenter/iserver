from lib.k8s.cluster_role_binding.api import K8sClusterRoleBindingApi
from lib.k8s.cluster_role_binding.info import K8sClusterRoleBindingInfo
from lib.k8s.cluster_role_binding.create import K8sClusterRoleBindingCreate
from lib.k8s.cluster_role_binding.delete import K8sClusterRoleBindingDelete
from lib.k8s.cluster_role_binding.update import K8sClusterRoleBindingUpdate
from lib.k8s.cluster_role_binding.wait import K8sClusterRoleBindingWait


class K8sClusterRoleBinding(
        K8sClusterRoleBindingApi,
        K8sClusterRoleBindingInfo,
        K8sClusterRoleBindingCreate,
        K8sClusterRoleBindingDelete,
        K8sClusterRoleBindingUpdate,
        K8sClusterRoleBindingWait
        ):
    def __init__(self):
        K8sClusterRoleBindingApi.__init__(self)
        K8sClusterRoleBindingInfo.__init__(self)
        K8sClusterRoleBindingCreate.__init__(self)
        K8sClusterRoleBindingDelete.__init__(self)
        K8sClusterRoleBindingUpdate.__init__(self)
        K8sClusterRoleBindingWait.__init__(self)
