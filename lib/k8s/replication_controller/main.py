from lib.k8s.replication_controller.api import K8sReplicationControllerApi
from lib.k8s.replication_controller.info import K8sReplicationControllerInfo


class K8sReplicationController(
        K8sReplicationControllerApi,
        K8sReplicationControllerInfo
        ):
    def __init__(self):
        K8sReplicationControllerApi.__init__(self)
        K8sReplicationControllerInfo.__init__(self)
