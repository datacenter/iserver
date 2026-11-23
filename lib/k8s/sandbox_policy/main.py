from lib.k8s.sandbox_policy.api import K8sSandboxPolicyApi
from lib.k8s.sandbox_policy.info import K8sSandboxPolicyInfo
from lib.k8s.sandbox_policy.create import K8sSandboxPolicyCreate
from lib.k8s.sandbox_policy.delete import K8sSandboxPolicyDelete
from lib.k8s.sandbox_policy.wait import K8sSandboxPolicyWait


class K8sSandboxPolicy(
        K8sSandboxPolicyApi,
        K8sSandboxPolicyInfo,
        K8sSandboxPolicyCreate,
        K8sSandboxPolicyDelete,
        K8sSandboxPolicyWait
        ):
    def __init__(self):
        K8sSandboxPolicyApi.__init__(self)
        K8sSandboxPolicyInfo.__init__(self)
        K8sSandboxPolicyCreate.__init__(self)
        K8sSandboxPolicyDelete.__init__(self)
        K8sSandboxPolicyWait.__init__(self)