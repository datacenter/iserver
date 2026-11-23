from lib.k8s.isovalent_bgp_cluster_config.api import K8sIsovalentBGPClusterConfigApi
from lib.k8s.isovalent_bgp_cluster_config.info import K8sIsovalentBGPClusterConfigInfo
from lib.k8s.isovalent_bgp_cluster_config.create import K8sIsovalentBGPClusterConfigCreate
from lib.k8s.isovalent_bgp_cluster_config.delete import K8sIsovalentBGPClusterConfigDelete
from lib.k8s.isovalent_bgp_cluster_config.wait import K8sIsovalentBGPClusterConfigWait


class K8sIsovalentBGPClusterConfig(
        K8sIsovalentBGPClusterConfigApi,
        K8sIsovalentBGPClusterConfigInfo,
        K8sIsovalentBGPClusterConfigCreate,
        K8sIsovalentBGPClusterConfigDelete,
        K8sIsovalentBGPClusterConfigWait
        ):
    def __init__(self):
        K8sIsovalentBGPClusterConfigApi.__init__(self)
        K8sIsovalentBGPClusterConfigInfo.__init__(self)
        K8sIsovalentBGPClusterConfigCreate.__init__(self)
        K8sIsovalentBGPClusterConfigDelete.__init__(self)
        K8sIsovalentBGPClusterConfigWait.__init__(self)
