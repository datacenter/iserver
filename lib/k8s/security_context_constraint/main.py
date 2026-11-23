from lib.k8s.security_context_constraint.api import K8sSecurityContextConstraintApi
from lib.k8s.security_context_constraint.info import K8sSecurityContextConstraintInfo


class K8sSecurityContextConstraint(
        K8sSecurityContextConstraintApi,
        K8sSecurityContextConstraintInfo
        ):
    def __init__(self):
        K8sSecurityContextConstraintApi.__init__(self)
        K8sSecurityContextConstraintInfo.__init__(self)
