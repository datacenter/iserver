from lib.md.aci.domain.aaa import MdAciDomainAaaOutput
from lib.md.aci.domain.l2 import MdAciDomainL2Output
from lib.md.aci.domain.l3 import MdAciDomainL3Output
from lib.md.aci.domain.phy import MdAciDomainPhyOutput
from lib.md.aci.domain.vmm import MdAciDomainVmmOutput


class MdAciDomainOutput(
        MdAciDomainAaaOutput,
        MdAciDomainL2Output,
        MdAciDomainL3Output,
        MdAciDomainPhyOutput,
        MdAciDomainVmmOutput
    ):
    def __init__(self):
        MdAciDomainAaaOutput.__init__(self)
        MdAciDomainL2Output.__init__(self)
        MdAciDomainL3Output.__init__(self)
        MdAciDomainPhyOutput.__init__(self)
        MdAciDomainVmmOutput.__init__(self)

    def print_aci_domain_addon(self, info, title=True):
        if info is None or len(info) == 0:
            return

        if title:
            self.my_output.print_stream('## Domain', 'output')

        order = [
            'Domain',
            'Type',
            'Switching',
            'Encap'
        ]
        self.print_table_header(order)

        for domain in info:
            line = ''
            line = self.add_column(line, domain['name'])
            line = self.add_column(line, domain['typeT'])
            line = self.add_column(line, domain['switchingMode'])
            line = self.add_column(line, domain['encapMode'])
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

    def print_aci_aaep_domain_addon(self, info, title=True):
        if info is None or len(info) == 0:
            return

        if title:
            self.my_output.print_stream('## AAEP Domain', 'output')

        order = [
            'Type',
            'Domain',
            'VLAN Pool',
            'VLAN Range'
        ]
        self.print_table_header(order)

        for domain in info:
            line = ''
            line = self.add_column(line, domain['domainType'])
            line = self.add_column(line, domain['domainName'])
            if domain['info'] is None:
                line = self.add_column(line, '---')
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, domain['info']['vlan'])
                if domain['info']['vlan_block'] is None or len(domain['info']['vlan_block']) == 0:
                    line = self.add_column(line, '---')
                else:
                    line = self.add_column(line, ', '.join(domain['info']['vlan_block']))

            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')
