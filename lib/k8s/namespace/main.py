from lib.k8s.namespace.api import K8sNamespaceApi
from lib.k8s.namespace.info import K8sNamespaceInfo
from lib.k8s.namespace.object import K8sNamespaceObject
from lib.k8s.namespace.task import K8sNamespaceTask


class K8sNamespace(K8sNamespaceApi, K8sNamespaceInfo, K8sNamespaceObject, K8sNamespaceTask):
    def __init__(self):
        K8sNamespaceApi.__init__(self)
        K8sNamespaceInfo.__init__(self)
        K8sNamespaceObject.__init__(self)
        K8sNamespaceTask.__init__(self)
