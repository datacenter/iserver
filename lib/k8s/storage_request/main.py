from lib.k8s.storage_request.api import K8sStorageRequestApi
from lib.k8s.storage_request.info import K8sStorageRequestInfo


class K8sStorageRequest(
        K8sStorageRequestApi,
        K8sStorageRequestInfo
        ):
    def __init__(self):
        K8sStorageRequestApi.__init__(self)
        K8sStorageRequestInfo.__init__(self)
