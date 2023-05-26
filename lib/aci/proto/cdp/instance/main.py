from lib.aci.proto.cdp.instance.api import ProtocolCdpInstanceApi
from lib.aci.proto.cdp.instance.info import ProtocolCdpInstanceInfo


class ProtocolCdpInstance(ProtocolCdpInstanceApi, ProtocolCdpInstanceInfo):
    def __init__(self):
        ProtocolCdpInstanceApi.__init__(self)
        ProtocolCdpInstanceInfo.__init__(self)
