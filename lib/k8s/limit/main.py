from lib.k8s.limit.api import K8sLimitApi
from lib.k8s.limit.info import K8sLimitInfo


class K8sLimit(
        K8sLimitApi,
        K8sLimitInfo
        ):
    def __init__(self):
        K8sLimitApi.__init__(self)
        K8sLimitInfo.__init__(self)
