from lib.k8s.isovalent_bgp_peer_config.api import K8sIsovalentBGPPeerConfigApi
from lib.k8s.isovalent_bgp_peer_config.info import K8sIsovalentBGPPeerConfigInfo
from lib.k8s.isovalent_bgp_peer_config.create import K8sIsovalentBGPPeerConfigCreate
from lib.k8s.isovalent_bgp_peer_config.delete import K8sIsovalentBGPPeerConfigDelete
from lib.k8s.isovalent_bgp_peer_config.wait import K8sIsovalentBGPPeerConfigWait


class K8sIsovalentBGPPeerConfig(
        K8sIsovalentBGPPeerConfigApi,
        K8sIsovalentBGPPeerConfigInfo,
        K8sIsovalentBGPPeerConfigCreate,
        K8sIsovalentBGPPeerConfigDelete,
        K8sIsovalentBGPPeerConfigWait
        ):
    def __init__(self):
        K8sIsovalentBGPPeerConfigApi.__init__(self)
        K8sIsovalentBGPPeerConfigInfo.__init__(self)
        K8sIsovalentBGPPeerConfigCreate.__init__(self)
        K8sIsovalentBGPPeerConfigDelete.__init__(self)
        K8sIsovalentBGPPeerConfigWait.__init__(self)