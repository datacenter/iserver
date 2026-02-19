from lib.k8s.ceph_block_pool_rados_namespace.api import K8sCephBlockPoolRadosNamespaceApi
from lib.k8s.ceph_block_pool_rados_namespace.info import K8sCephBlockPoolRadosNamespaceInfo


class K8sCephBlockPoolRadosNamespace(
        K8sCephBlockPoolRadosNamespaceApi,
        K8sCephBlockPoolRadosNamespaceInfo
        ):
    def __init__(self):
        K8sCephBlockPoolRadosNamespaceApi.__init__(self)
        K8sCephBlockPoolRadosNamespaceInfo.__init__(self)
