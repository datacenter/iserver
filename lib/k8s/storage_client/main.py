from lib.k8s.storage_client.api import K8sStorageClientApi
from lib.k8s.storage_client.info import K8sStorageClientInfo


class K8sStorageClient(
        K8sStorageClientApi,
        K8sStorageClientInfo
        ):
    def __init__(self):
        K8sStorageClientApi.__init__(self)
        K8sStorageClientInfo.__init__(self)
