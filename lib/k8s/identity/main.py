from lib.k8s.identity.api import K8sIdentityApi
from lib.k8s.identity.info import K8sIdentityInfo
from lib.k8s.identity.delete import K8sIdentityDelete
from lib.k8s.identity.wait import K8sIdentityWait


class K8sIdentity(
        K8sIdentityApi,
        K8sIdentityInfo,
        K8sIdentityDelete,
        K8sIdentityWait
        ):
    def __init__(self):
        K8sIdentityApi.__init__(self)
        K8sIdentityInfo.__init__(self)
        K8sIdentityDelete.__init__(self)
        K8sIdentityWait.__init__(self)
