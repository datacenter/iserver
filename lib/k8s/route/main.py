from lib.k8s.route.api import K8sRouteApi
from lib.k8s.route.info import K8sRouteInfo
from lib.k8s.route.cilium_timescape import K8sRouteCiliumTimescape
from lib.k8s.route.splunk_standalone import K8sRouteSplunkStandalone


class K8sRoute(
        K8sRouteApi,
        K8sRouteInfo,
        K8sRouteCiliumTimescape,
        K8sRouteSplunkStandalone
        ):
    def __init__(self):
        K8sRouteApi.__init__(self)
        K8sRouteInfo.__init__(self)
        K8sRouteCiliumTimescape.__init__(self)
        K8sRouteSplunkStandalone.__init__(self)
