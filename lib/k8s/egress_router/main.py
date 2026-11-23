from lib.k8s.egress_router.api import K8sEgressRouterApi
from lib.k8s.egress_router.info import K8sEgressRouterInfo


class K8sEgressRouter(
        K8sEgressRouterApi,
        K8sEgressRouterInfo
        ):
    def __init__(self):
        K8sEgressRouterApi.__init__(self)
        K8sEgressRouterInfo.__init__(self)
