from lib.k8s.vast_storage.api import K8sVastStorageApi
from lib.k8s.vast_storage.info import K8sVastStorageInfo
from lib.k8s.vast_storage.create import K8sVastStorageCreate
from lib.k8s.vast_storage.delete import K8sVastStorageDelete
from lib.k8s.vast_storage.wait import K8sVastStorageWait


class K8sVastStorage(
        K8sVastStorageApi,
        K8sVastStorageInfo,
        K8sVastStorageCreate,
        K8sVastStorageDelete,
        K8sVastStorageWait
        ):
    def __init__(self):
        K8sVastStorageApi.__init__(self)
        K8sVastStorageInfo.__init__(self)
        K8sVastStorageCreate.__init__(self)
        K8sVastStorageDelete.__init__(self)
        K8sVastStorageWait.__init__(self)
        