from lib.k8s.local_volume_discovery.api import K8sLocalVolumeDiscoveryApi
from lib.k8s.local_volume_discovery.info import K8sLocalVolumeDiscoveryInfo


class K8sLocalVolumeDiscovery(
        K8sLocalVolumeDiscoveryApi,
        K8sLocalVolumeDiscoveryInfo
        ):
    def __init__(self):
        K8sLocalVolumeDiscoveryApi.__init__(self)
        K8sLocalVolumeDiscoveryInfo.__init__(self)
