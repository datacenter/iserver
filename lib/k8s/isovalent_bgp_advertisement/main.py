from lib.k8s.isovalent_bgp_advertisement.api import K8sIsovalentBGPAdvertisementApi
from lib.k8s.isovalent_bgp_advertisement.info import K8sIsovalentBGPAdvertisementInfo
from lib.k8s.isovalent_bgp_advertisement.create import K8sIsovalentBGPAdvertisementCreate
from lib.k8s.isovalent_bgp_advertisement.delete import K8sIsovalentBGPAdvertisementDelete
from lib.k8s.isovalent_bgp_advertisement.wait import K8sIsovalentBGPAdvertisementWait


class K8sIsovalentBGPAdvertisement(
        K8sIsovalentBGPAdvertisementApi,
        K8sIsovalentBGPAdvertisementInfo,
        K8sIsovalentBGPAdvertisementCreate,
        K8sIsovalentBGPAdvertisementDelete,
        K8sIsovalentBGPAdvertisementWait
        ):
    def __init__(self):
        K8sIsovalentBGPAdvertisementApi.__init__(self)
        K8sIsovalentBGPAdvertisementInfo.__init__(self)
        K8sIsovalentBGPAdvertisementCreate.__init__(self)
        K8sIsovalentBGPAdvertisementDelete.__init__(self)
        K8sIsovalentBGPAdvertisementWait.__init__(self)
