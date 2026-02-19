from lib.k8s.storage_profile.api import K8sStorageProfileApi
from lib.k8s.storage_profile.info import K8sStorageProfileInfo


class K8sStorageProfile(
        K8sStorageProfileApi,
        K8sStorageProfileInfo
        ):
    def __init__(self):
        K8sStorageProfileApi.__init__(self)
        K8sStorageProfileInfo.__init__(self)
