from lib.k8s.bgp_advertisement.api import K8sBgpAdvertisementApi
from lib.k8s.bgp_advertisement.info import K8sBgpAdvertisementInfo
from lib.k8s.bgp_advertisement.create import K8sBgpAdvertisementCreate
from lib.k8s.bgp_advertisement.delete import K8sBgpAdvertisementDelete
from lib.k8s.bgp_advertisement.update import K8sBgpAdvertisementUpdate
from lib.k8s.bgp_advertisement.wait import K8sBgpAdvertisementWait


class K8sBgpAdvertisement(
        K8sBgpAdvertisementApi,
        K8sBgpAdvertisementInfo,
        K8sBgpAdvertisementCreate,
        K8sBgpAdvertisementDelete,
        K8sBgpAdvertisementUpdate,
        K8sBgpAdvertisementWait
        ):
    def __init__(self):
        K8sBgpAdvertisementApi.__init__(self)
        K8sBgpAdvertisementInfo.__init__(self)
        K8sBgpAdvertisementCreate.__init__(self)
        K8sBgpAdvertisementDelete.__init__(self)
        K8sBgpAdvertisementUpdate.__init__(self)
        K8sBgpAdvertisementWait.__init__(self)
