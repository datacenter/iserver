from lib.k8s.route_advertisement.api import K8sRouteAdvertisementApi
from lib.k8s.route_advertisement.info import K8sRouteAdvertisementInfo
from lib.k8s.route_advertisement.create import K8sRouteAdvertisementCreate
from lib.k8s.route_advertisement.delete import K8sRouteAdvertisementDelete
from lib.k8s.route_advertisement.update import K8sRouteAdvertisementUpdate
from lib.k8s.route_advertisement.wait import K8sRouteAdvertisementWait


class K8sRouteAdvertisement(
        K8sRouteAdvertisementApi,
        K8sRouteAdvertisementInfo,
        K8sRouteAdvertisementCreate,
        K8sRouteAdvertisementDelete,
        K8sRouteAdvertisementUpdate,
        K8sRouteAdvertisementWait
        ):
    def __init__(self):
        K8sRouteAdvertisementApi.__init__(self)
        K8sRouteAdvertisementInfo.__init__(self)
        K8sRouteAdvertisementCreate.__init__(self)
        K8sRouteAdvertisementDelete.__init__(self)
        K8sRouteAdvertisementUpdate.__init__(self)
        K8sRouteAdvertisementWait.__init__(self)
