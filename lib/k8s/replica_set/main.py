from lib.k8s.replica_set.api import K8sReplicaSetApi
from lib.k8s.replica_set.info import K8sReplicaSetInfo
from lib.k8s.replica_set.wait import K8sReplicaSetWait


class K8sReplicaSet(
        K8sReplicaSetApi,
        K8sReplicaSetInfo,
        K8sReplicaSetWait
        ):
    def __init__(self):
        K8sReplicaSetApi.__init__(self)
        K8sReplicaSetInfo.__init__(self)
        K8sReplicaSetWait.__init__(self)
