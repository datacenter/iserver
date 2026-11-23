from lib.aci.domain.aaa.main import DomainAaa
from lib.aci.domain.l2.main import DomainL2
from lib.aci.domain.l3.main import DomainL3
from lib.aci.domain.phy.main import DomainPhy
from lib.aci.domain.vmm.main import DomainVmm


class Domain(
    DomainAaa,
    DomainL2,
    DomainL3,
    DomainPhy,
    DomainVmm
    ):
    def __init__(self):
        DomainAaa.__init__(self)
        DomainL2.__init__(self)
        DomainL3.__init__(self)
        DomainPhy.__init__(self)
        DomainVmm.__init__(self)

    def get_domain_type_from_tcl(self, domain_type):
        mapping = {}
        mapping['l3extDomP'] = 'L3'
        mapping['physDomP'] = 'Physical'
        mapping['l2extDomP'] = 'L2'
        mapping['vmmDomP'] = 'VMM'

        if domain_type in mapping:
            return mapping[domain_type]

        return domain_type
