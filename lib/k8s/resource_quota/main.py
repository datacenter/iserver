from lib.k8s.resource_quota.api import K8sResourceQuotaApi
from lib.k8s.resource_quota.info import K8sResourceQuotaInfo


class K8sResourceQuota(
        K8sResourceQuotaApi,
        K8sResourceQuotaInfo
        ):
    def __init__(self):
        K8sResourceQuotaApi.__init__(self)
        K8sResourceQuotaInfo.__init__(self)
