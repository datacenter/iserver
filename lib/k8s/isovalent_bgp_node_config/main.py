from lib.k8s.isovalent_bgp_node_config.api import K8sIsovalentBGPNodeConfigApi
from lib.k8s.isovalent_bgp_node_config.info import K8sIsovalentBGPNodeConfigInfo


class K8sIsovalentBGPNodeConfig(
        K8sIsovalentBGPNodeConfigApi,
        K8sIsovalentBGPNodeConfigInfo
        ):
    def __init__(self):
        K8sIsovalentBGPNodeConfigApi.__init__(self)
        K8sIsovalentBGPNodeConfigInfo.__init__(self)
