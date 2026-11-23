from lib.k8s.bgp_peer.api import K8sBgpPeerApi
from lib.k8s.bgp_peer.info import K8sBgpPeerInfo
from lib.k8s.bgp_peer.create import K8sBgpPeerCreate
from lib.k8s.bgp_peer.delete import K8sBgpPeerDelete
from lib.k8s.bgp_peer.update import K8sBgpPeerUpdate
from lib.k8s.bgp_peer.wait import K8sBgpPeerWait


class K8sBgpPeer(
        K8sBgpPeerApi,
        K8sBgpPeerInfo,
        K8sBgpPeerCreate,
        K8sBgpPeerDelete,
        K8sBgpPeerUpdate,
        K8sBgpPeerWait
        ):
    def __init__(self):
        K8sBgpPeerApi.__init__(self)
        K8sBgpPeerInfo.__init__(self)
        K8sBgpPeerCreate.__init__(self)
        K8sBgpPeerDelete.__init__(self)
        K8sBgpPeerUpdate.__init__(self)
        K8sBgpPeerWait.__init__(self)
