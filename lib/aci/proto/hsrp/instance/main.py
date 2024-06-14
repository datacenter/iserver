from lib.aci.proto.hsrp.instance.api import ProtocolHsrpInstanceApi
from lib.aci.proto.hsrp.instance.info import ProtocolHsrpInstanceInfo


class ProtocolHsrpInstance(ProtocolHsrpInstanceApi, ProtocolHsrpInstanceInfo):
    def __init__(self):
        ProtocolHsrpInstanceApi.__init__(self)
        ProtocolHsrpInstanceInfo.__init__(self)
