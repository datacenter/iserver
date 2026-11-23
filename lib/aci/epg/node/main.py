from lib.aci.epg.node.api import EpgNodeApi
from lib.aci.epg.node.info import EpgNodeInfo


class EpgNode(EpgNodeApi, EpgNodeInfo):
    def __init__(self):
        EpgNodeApi.__init__(self)
        EpgNodeInfo.__init__(self)
