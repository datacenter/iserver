from lib.k8s.local_volume_discovery_result.api import K8sLocalVolumeDiscoveryResultApi
from lib.k8s.local_volume_discovery_result.info import K8sLocalVolumeDiscoveryResultInfo


class K8sLocalVolumeDiscoveryResult(
        K8sLocalVolumeDiscoveryResultApi,
        K8sLocalVolumeDiscoveryResultInfo
        ):
    def __init__(self):
        K8sLocalVolumeDiscoveryResultApi.__init__(self)
        K8sLocalVolumeDiscoveryResultInfo.__init__(self)
