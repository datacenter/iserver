from lib.aci.proto.bfd.session.api import ProtocolBfdSessionApi
from lib.aci.proto.bfd.session.info import ProtocolBfdSessionInfo
from lib.aci.proto.bfd.session.stats.main import ProtocolBfdSessionStats
from lib.aci.proto.bfd.session.peer.main import ProtocolBfdSessionPeer


class ProtocolBfdSession(ProtocolBfdSessionApi, ProtocolBfdSessionInfo, ProtocolBfdSessionStats, ProtocolBfdSessionPeer):
    def __init__(self):
        ProtocolBfdSessionApi.__init__(self)
        ProtocolBfdSessionInfo.__init__(self)
        ProtocolBfdSessionStats.__init__(self)
        ProtocolBfdSessionPeer.__init__(self)
