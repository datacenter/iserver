from lib.aci.proto.isis.lsp.api import ProtocolIsisLspApi
from lib.aci.proto.isis.lsp.info import ProtocolIsisLspInfo


class ProtocolIsisLsp(ProtocolIsisLspApi, ProtocolIsisLspInfo):
    def __init__(self):
        ProtocolIsisLspApi.__init__(self)
        ProtocolIsisLspInfo.__init__(self)
