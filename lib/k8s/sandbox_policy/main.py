from lib.k8s.sandbox_policy.api import K8sSandboxPolicyApi
from lib.k8s.sandbox_policy.info import K8sSandboxPolicyInfo


class K8sSandboxPolicy(
        K8sSandboxPolicyApi,
        K8sSandboxPolicyInfo
        ):
    def __init__(self):
        K8sSandboxPolicyApi.__init__(self)
        K8sSandboxPolicyInfo.__init__(self)
