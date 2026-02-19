from lib.k8s.object_transfer.api import K8sObjectTransferApi
from lib.k8s.object_transfer.info import K8sObjectTransferInfo


class K8sObjectTransfer(
        K8sObjectTransferApi,
        K8sObjectTransferInfo
        ):
    def __init__(self):
        K8sObjectTransferApi.__init__(self)
        K8sObjectTransferInfo.__init__(self)
