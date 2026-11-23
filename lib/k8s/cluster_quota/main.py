from lib.k8s.cluster_quota.api import K8sClusterQuotaApi
from lib.k8s.cluster_quota.info import K8sClusterQuotaInfo


class K8sClusterQuota(
        K8sClusterQuotaApi,
        K8sClusterQuotaInfo
        ):
    def __init__(self):
        K8sClusterQuotaApi.__init__(self)
        K8sClusterQuotaInfo.__init__(self)
