from lib.aci.proto.isis.tree.api import ProtocolIsisTreeApi
from lib.aci.proto.isis.tree.info import ProtocolIsisTreeInfo


class ProtocolIsisTree(ProtocolIsisTreeApi, ProtocolIsisTreeInfo):
    def __init__(self):
        ProtocolIsisTreeApi.__init__(self)
        ProtocolIsisTreeInfo.__init__(self)
