from lib.k8s.identity.api import K8sIdentityApi
from lib.k8s.identity.info import K8sIdentityInfo


class K8sIdentity(
        K8sIdentityApi,
        K8sIdentityInfo
        ):
    def __init__(self):
        K8sIdentityApi.__init__(self)
        K8sIdentityInfo.__init__(self)
