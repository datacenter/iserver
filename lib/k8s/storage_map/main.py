from lib.k8s.storage_map.api import K8sStorageMapApi
from lib.k8s.storage_map.info import K8sStorageMapInfo
from lib.k8s.storage_map.create import K8sStorageMapCreate
from lib.k8s.storage_map.delete import K8sStorageMapDelete
from lib.k8s.storage_map.wait import K8sStorageMapWait


class K8sStorageMap(
        K8sStorageMapApi,
        K8sStorageMapInfo,
        K8sStorageMapCreate,
        K8sStorageMapDelete,
        K8sStorageMapWait
        ):
    def __init__(self):
        K8sStorageMapApi.__init__(self)
        K8sStorageMapInfo.__init__(self)
        K8sStorageMapCreate.__init__(self)
        K8sStorageMapDelete.__init__(self)
        K8sStorageMapWait.__init__(self)
