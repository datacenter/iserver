from lib.aci.proto.bfd.session.peer.api import ProtocolBfdSessionPeerApi
from lib.aci.proto.bfd.session.peer.info import ProtocolBfdSessionPeerInfo


class ProtocolBfdSessionPeer(ProtocolBfdSessionPeerApi, ProtocolBfdSessionPeerInfo):
    def __init__(self):
        ProtocolBfdSessionPeerApi.__init__(self)
        ProtocolBfdSessionPeerInfo.__init__(self)
