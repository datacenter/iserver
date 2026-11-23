from lib.k8s.lease.api import K8sLeaseApi
from lib.k8s.lease.info import K8sLeaseInfo


class K8sLease(
        K8sLeaseApi,
        K8sLeaseInfo,
        ):
    def __init__(self):
        K8sLeaseApi.__init__(self)
        K8sLeaseInfo.__init__(self)

