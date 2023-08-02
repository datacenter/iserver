from lib.aci.domain.l3.node.api import DomainL3NodeApi
from lib.aci.domain.l3.node.info import DomainL3NodeInfo


class DomainL3Node(DomainL3NodeApi, DomainL3NodeInfo):
    def __init__(self):
        DomainL3NodeApi.__init__(self)
        DomainL3NodeInfo.__init__(self)
