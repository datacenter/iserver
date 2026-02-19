from lib.xd.aci.domain.aaa import AciDomainAaa
from lib.xd.aci.domain.l2 import AciDomainL2
from lib.xd.aci.domain.l3 import AciDomainL3
from lib.xd.aci.domain.phy import AciDomainPhy
from lib.xd.aci.domain.vmm import AciDomainVmm


class AciDomain(
        AciDomainAaa,
        AciDomainL2,
        AciDomainL3,
        AciDomainPhy,
        AciDomainVmm
    ):
    def __init__(self):
        AciDomainAaa.__init__(self)
        AciDomainL2.__init__(self)
        AciDomainL3.__init__(self)
        AciDomainPhy.__init__(self)
        AciDomainVmm.__init__(self)

    def load_pre_aci_domain(self):
        if not self.load_pre_aci_domain_aaa():
            return False

        if not self.load_pre_aci_domain_l2():
            return False

        if not self.load_pre_aci_domain_l3():
            return False

        if not self.load_pre_aci_domain_phy():
            return False

        if not self.load_pre_aci_domain_vmm():
            return False

        return True

    def get_aci_domain_types(self):
        return ['aaa', 'l2', 'l3', 'phy', 'vmm']

    def get_aci_domain_type(self, managed_object_dn):
        # "dn": "uni/userext/domain-all"
        # "dn": "uni/l2dom-VNF-mgmt_L2Dom"
        # "dn": "uni/l3dom-cvim1_TEST_L3dom"
        # "dn": "uni/phys-cvim-brAPI_PhysDom"
        # "dn": "uni/vmmp-VMware/dom-EU-SPDC-CDC"
        if managed_object_dn.split('/')[1].split('-')[0] == 'userext':
            return 'aaa'

        if managed_object_dn.split('/')[1].split('-')[0] == 'l2dom':
            return 'l2'

        if managed_object_dn.split('/')[1].split('-')[0] == 'l3dom':
            return 'l3'

        if managed_object_dn.split('/')[1].split('-')[0] == 'phys':
            return 'phy'

        if managed_object_dn.split('/')[1].split('-')[0] == 'vmmp':
            return 'vmm'

        return None

    def prepare_aci_domain(self):
        self.my_output.debug('Get aci domain aaa...')
        if not self.prepare_aci_domain_aaa():
            self.my_output.error('Get aci domain aaa failed')
            return False

        self.my_output.debug('Get aci domain l2...')
        if not self.prepare_aci_domain_l2():
            self.my_output.error('Get aci domain l2 failed')
            return False

        self.my_output.debug('Get aci domain l3...')
        if not self.prepare_aci_domain_l3():
            self.my_output.error('Get aci domain l3 failed')
            return False

        self.my_output.debug('Get aci domain phy...')
        if not self.prepare_aci_domain_phy():
            self.my_output.error('Get aci domain phy failed')
            return False

        self.my_output.debug('Get aci domain vmm...')
        if not self.prepare_aci_domain_vmm():
            self.my_output.error('Get aci domain vmm failed')
            return False

        return True

    def run_aci_domain(self):
        if not self.run_aci_domain_aaa():
            return False

        if not self.run_aci_domain_l2():
            return False

        if not self.run_aci_domain_l3():
            return False

        if not self.run_aci_domain_phy():
            return False

        if not self.run_aci_domain_vmm():
            return False

        return True

    def load_post_aci_domain(self):
        if not self.load_post_aci_domain_aaa():
            return False

        if not self.load_post_aci_domain_l2():
            return False

        if not self.load_post_aci_domain_l3():
            return False

        if not self.load_post_aci_domain_phy():
            return False

        if not self.load_post_aci_domain_vmm():
            return False

        return True

