from lib.intersight.intersight_common import IntersightCommon
from lib.intersight.pci_node.info import PciNodeInfo


class PciNode(IntersightCommon, PciNodeInfo):
    def __init__(self, iaccount, log_id=None):
        self.iobject = 'pci node'
        IntersightCommon.__init__(self, iaccount, self.iobject, log_id=log_id)
        PciNodeInfo.__init__(self)
