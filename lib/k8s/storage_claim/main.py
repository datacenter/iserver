from lib.k8s.storage_claim.api import K8sStorageClaimApi
from lib.k8s.storage_claim.info import K8sStorageClaimInfo


class K8sStorageClaim(
        K8sStorageClaimApi,
        K8sStorageClaimInfo
        ):
    def __init__(self):
        K8sStorageClaimApi.__init__(self)
        K8sStorageClaimInfo.__init__(self)
