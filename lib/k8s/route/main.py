from lib.k8s.route.api import K8sRouteApi
from lib.k8s.route.info import K8sRouteInfo


class K8sRoute(
        K8sRouteApi,
        K8sRouteInfo
        ):
    def __init__(self):
        K8sRouteApi.__init__(self)
        K8sRouteInfo.__init__(self)
