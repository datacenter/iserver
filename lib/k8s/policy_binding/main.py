from lib.k8s.policy_binding.api import K8sPolicyBindingApi
from lib.k8s.policy_binding.info import K8sPolicyBindingInfo
from lib.k8s.policy_binding.create import K8sPolicyBindingCreate
from lib.k8s.policy_binding.delete import K8sPolicyBindingDelete
from lib.k8s.policy_binding.wait import K8sPolicyBindingWait


class K8sPolicyBinding(
        K8sPolicyBindingApi,
        K8sPolicyBindingInfo,
        K8sPolicyBindingCreate,
        K8sPolicyBindingDelete,
        K8sPolicyBindingWait
        ):
    def __init__(self):
        K8sPolicyBindingApi.__init__(self)
        K8sPolicyBindingInfo.__init__(self)
        K8sPolicyBindingCreate.__init__(self)
        K8sPolicyBindingDelete.__init__(self)
        K8sPolicyBindingWait.__init__(self)
