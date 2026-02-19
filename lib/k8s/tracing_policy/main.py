from lib.k8s.tracing_policy.api import K8sTracingPolicyApi
from lib.k8s.tracing_policy.info import K8sTracingPolicyInfo


class K8sTracingPolicy(
        K8sTracingPolicyApi,
        K8sTracingPolicyInfo
        ):
    def __init__(self):
        K8sTracingPolicyApi.__init__(self)
        K8sTracingPolicyInfo.__init__(self)
