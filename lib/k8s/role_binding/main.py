from lib.k8s.role_binding.api import K8sRoleBindingApi
from lib.k8s.role_binding.info import K8sRoleBindingInfo


class K8sRoleBinding(
        K8sRoleBindingApi,
        K8sRoleBindingInfo
        ):
    def __init__(self):
        K8sRoleBindingApi.__init__(self)
        K8sRoleBindingInfo.__init__(self)
