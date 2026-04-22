from lib.k8s.route.api import K8sRouteApi
from lib.k8s.route.info import K8sRouteInfo
from lib.k8s.route.match import K8sRouteMatch
from lib.k8s.route.update import K8sRouteUpdate
from lib.k8s.route.wait import K8sRouteWait
from lib.k8s.route.cilium_timescape import K8sRouteCiliumTimescape
from lib.k8s.route.intersight import K8sRouteIntersight
from lib.k8s.route.splunk_standalone import K8sRouteSplunkStandalone


class K8sRoute(
        K8sRouteApi,
        K8sRouteInfo,
        K8sRouteMatch,
        K8sRouteUpdate,
        K8sRouteWait,
        K8sRouteCiliumTimescape,
        K8sRouteIntersight,
        K8sRouteSplunkStandalone
        ):
    def __init__(self):
        K8sRouteApi.__init__(self)
        K8sRouteInfo.__init__(self)
        K8sRouteMatch.__init__(self)
        K8sRouteUpdate.__init__(self)
        K8sRouteWait.__init__(self)
        K8sRouteCiliumTimescape.__init__(self)
        K8sRouteIntersight.__init__(self)
        K8sRouteSplunkStandalone.__init__(self)
