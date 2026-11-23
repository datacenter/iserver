from lib.k8s.network_map.api import K8sNetworkMapApi
from lib.k8s.network_map.info import K8sNetworkMapInfo
from lib.k8s.network_map.create import K8sNetworkMapCreate
from lib.k8s.network_map.delete import K8sNetworkMapDelete
from lib.k8s.network_map.wait import K8sNetworkMapWait


class K8sNetworkMap(
        K8sNetworkMapApi,
        K8sNetworkMapInfo,
        K8sNetworkMapCreate,
        K8sNetworkMapDelete,
        K8sNetworkMapWait
        ):
    def __init__(self):
        K8sNetworkMapApi.__init__(self)
        K8sNetworkMapInfo.__init__(self)
        K8sNetworkMapCreate.__init__(self)
        K8sNetworkMapDelete.__init__(self)
        K8sNetworkMapWait.__init__(self)
