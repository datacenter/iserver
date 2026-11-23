from lib.k8s.role_binding.api import K8sRoleBindingApi
from lib.k8s.role_binding.info import K8sRoleBindingInfo
from lib.k8s.role_binding.create import K8sRoleBindingCreate
from lib.k8s.role_binding.delete import K8sRoleBindingDelete
from lib.k8s.role_binding.wait import K8sRoleBindingWait


class K8sRoleBinding(
        K8sRoleBindingApi,
        K8sRoleBindingInfo,
        K8sRoleBindingCreate,
        K8sRoleBindingDelete,
        K8sRoleBindingWait
        ):
    def __init__(self):
        K8sRoleBindingApi.__init__(self)
        K8sRoleBindingInfo.__init__(self)
        K8sRoleBindingCreate.__init__(self)
        K8sRoleBindingDelete.__init__(self)
        K8sRoleBindingWait.__init__(self)
