from lib.k8s.namespace.api import K8sNamespaceApi
from lib.k8s.namespace.info import K8sNamespaceInfo


class K8sNamespace(
        K8sNamespaceApi,
        K8sNamespaceInfo
        ):
    def __init__(self):
        K8sNamespaceApi.__init__(self)
        K8sNamespaceInfo.__init__(self)
