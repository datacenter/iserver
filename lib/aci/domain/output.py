from lib.aci.domain.aaa.output import DomainAaaOutput
from lib.aci.domain.l2.output import DomainL2Output
from lib.aci.domain.l3.output import DomainL3Output
from lib.aci.domain.phy.output import DomainPhyOutput
from lib.aci.domain.vmm.output import DomainVmmOutput


class DomainOutput(DomainAaaOutput, DomainL2Output, DomainL3Output, DomainPhyOutput, DomainVmmOutput):
    def __init__(self):
        DomainAaaOutput.__init__(self)
        DomainL2Output.__init__(self)
        DomainL3Output.__init__(self)
        DomainPhyOutput.__init__(self)
        DomainVmmOutput.__init__(self)
