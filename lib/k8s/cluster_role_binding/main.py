from lib.k8s.cluster_role_binding.api import K8sClusterRoleBindingApi
from lib.k8s.cluster_role_binding.info import K8sClusterRoleBindingInfo


class K8sClusterRoleBinding(
        K8sClusterRoleBindingApi,
        K8sClusterRoleBindingInfo
        ):
    def __init__(self):
        K8sClusterRoleBindingApi.__init__(self)
        K8sClusterRoleBindingInfo.__init__(self)
