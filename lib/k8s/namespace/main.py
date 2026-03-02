from lib.k8s.namespace.api import K8sNamespaceApi
from lib.k8s.namespace.info import K8sNamespaceInfo
from lib.k8s.namespace.create import K8sNamespaceCreate
from lib.k8s.namespace.delete import K8sNamespaceDelete
from lib.k8s.namespace.wait import K8sNamespaceWait

class K8sNamespace(
        K8sNamespaceApi,
        K8sNamespaceInfo,
        K8sNamespaceCreate,
        K8sNamespaceDelete,
        K8sNamespaceWait
        ):
    def __init__(self):
        K8sNamespaceApi.__init__(self)
        K8sNamespaceInfo.__init__(self)
        K8sNamespaceCreate.__init__(self)
        K8sNamespaceDelete.__init__(self)
        K8sNamespaceWait.__init__(self)
