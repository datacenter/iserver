import os
from lib import file_helper
from lib.aci import helper as aci_helper
from lib.nexus import helper as nexus_helper
from lib.md.aci.aae import MdAciAaeOutput
from lib.md.aci.ap import MdAciApOutput
from lib.md.aci.bd import MdAciBdOutput
from lib.md.aci.cdp import MdAciCdpOutput
from lib.md.aci.contract.main import MdAciContractOutput
from lib.md.aci.domain.main import MdAciDomainOutput
from lib.md.aci.ep import MdAciEpOutput
from lib.md.aci.epg import MdAciEpgOutput
from lib.md.aci.l2out import MdAciL2OutOutput
from lib.md.aci.l3mpls import MdAciL3MplsOutput
from lib.md.aci.l3out import MdAciL3OutOutput
from lib.md.aci.lacp import MdAciLacpOutput
from lib.md.aci.lldp import MdAciLldpOutput
from lib.md.aci.node import MdAciNodeOutput
from lib.md.aci.phy.main import MdAciPhyOutput
from lib.md.aci.pool.main import MdAciPoolOutput
from lib.md.aci.server import MdAciServerOutput
from lib.md.aci.tenant import MdAciTenantOutput
from lib.md.aci.vrf import MdAciVrfOutput


class MdAciOutput(
        MdAciAaeOutput,
        MdAciApOutput,
        MdAciBdOutput,
        MdAciCdpOutput,
        MdAciContractOutput,
        MdAciDomainOutput,
        MdAciEpOutput,
        MdAciEpgOutput,
        MdAciL2OutOutput,
        MdAciL3MplsOutput,
        MdAciL3OutOutput,
        MdAciLacpOutput,
        MdAciLldpOutput,
        MdAciNodeOutput,
        MdAciPhyOutput,
        MdAciPoolOutput,
        MdAciServerOutput,
        MdAciTenantOutput,
        MdAciVrfOutput
    ):
    def __init__(self):
        MdAciAaeOutput.__init__(self)
        MdAciApOutput.__init__(self)
        MdAciBdOutput.__init__(self)
        MdAciCdpOutput.__init__(self)
        MdAciContractOutput.__init__(self)
        MdAciDomainOutput.__init__(self)
        MdAciEpOutput.__init__(self)
        MdAciEpgOutput.__init__(self)
        MdAciL2OutOutput.__init__(self)
        MdAciL3MplsOutput.__init__(self)
        MdAciL3OutOutput.__init__(self)
        MdAciLacpOutput.__init__(self)
        MdAciLldpOutput.__init__(self)
        MdAciNodeOutput.__init__(self)
        MdAciPhyOutput.__init__(self)
        MdAciPoolOutput.__init__(self)
        MdAciServerOutput.__init__(self)
        MdAciTenantOutput.__init__(self)
        MdAciVrfOutput.__init__(self)

    def get_aci_template_dir(self):
        main_dir = file_helper.get_main_dir()
        if main_dir is None:
            return None

        directory = os.path.join(
            os.path.join(
                os.path.join(
                    main_dir,
                    'templates'
                ),
                'md'
            ),
            'aci'
        )

        return directory

    def add_aci_connected_device_name(self, line, item, up=False, last=False):
        base = './'
        if up:
            base = '../'

        if item['nei_device_type'] is None or item['nei_device_type'] not in ['Nexus', 'ACI', 'FI', 'Server']:
            if item['nei_device_name'] is None:
                line = self.add_column(line, '---', last=last)
            else:
                line = self.add_column(line, item['nei_device_name'], last=last)

        if item['nei_device_type'] is not None and item['nei_device_type'] == 'Nexus':
            if self.xd_handler.is_nexus_device_name(item['nei_device_name']):
                line = self.add_column(
                    line,
                    '[%s](../nexus/%s%s-eth.md)' % (
                        item['nei_device_name'],
                        base,
                        item['nei_device_name']
                    ),
                    last=last
                )
            else:
                line = self.add_column(line, item['nei_device_name'], last=last)

        if item['nei_device_type'] is not None and item['nei_device_type'] == 'FI':
            if self.xd_handler.is_fi_name(item['nei_device_name']):
                line = self.add_column(
                    line,
                    '[%s](../fi/%s%s-eth.md)' % (
                        item['nei_device_name'],
                        base,
                        self.xd_handler.get_fi_hash(item['nei_device_name'])
                    ),
                    last=last
                )
            else:
                line = self.add_column(line, item['nei_device_name'], last=last)

        if item['nei_device_type'] is not None and item['nei_device_type'] == 'ACI':
            if self.xd_handler.is_aci_node_name(item['nei_device_name']):
                line = self.add_column(
                    line,
                    '[%s](%s%s-%s-phy.md)' % (
                        item['nei_device_name'],
                        base,
                        item['nei_apic_name'],
                        item['nei_device_name']
                    ),
                    last=last
                )
            else:
                line = self.add_column(line, item['nei_device_name'], last=last)

        if item['nei_device_type'] is not None and item['nei_device_type'] == 'Server':
            line = self.add_column(
                line,
                '[%s](%s../compute/%s-net.md)' % (
                    item['nei_device_name'],
                    base,
                    item['nei_device_id']
                ),
                last=last
            )

        return line

    def add_aci_connected_device_interface(self, line, item, up=False, last=False):
        base = './'
        if up:
            base = '../'

        if item['nei_device_type'] is None or item['nei_device_type'] not in ['Nexus', 'ACI', 'FI', 'Server']:
            if item['nei_interface_name'] is None:
                line = self.add_column(line, '---', last=last)
            else:
                line = self.add_column(line, item['nei_interface_name'], last=last)

        if item['nei_device_type'] is not None and item['nei_device_type'] == 'Nexus':
            if item['nei_interface_name'] is None:
                line = self.add_column(line, '---', last=last)
            else:
                if self.xd_handler.is_nexus_device_name(item['nei_device_name']):
                    line = self.add_column(
                        line,
                        '[%s](../nexus/%s/%s.md)' % (
                            item['nei_interface_name'],
                            nexus_helper.get_nexus_interface_type(item['nei_interface_name']),
                            item['nei_interface_hash']
                        ),
                        last=last
                    )
                else:
                    line = self.add_column(line, item['nei_interface_name'], last=last)

        if item['nei_device_type'] is not None and item['nei_device_type'] == 'FI':
            if item['nei_interface_name'] is None:
                line = self.add_column(line, '---', last=last)
            else:
                if self.xd_handler.is_fi_name(item['nei_device_name']):
                    line = self.add_column(
                        line,
                        '[%s](../fi/eth/%s.md)' % (
                            item['nei_interface_name'],
                            item['nei_interface_hash']
                        ),
                        last=last
                    )
                else:
                    line = self.add_column(line, item['nei_interface_name'], last=last)

        if item['nei_device_type'] is not None and item['nei_device_type'] == 'ACI':
            if item['nei_interface_name'] is None:
                line = self.add_column(line, '---', last=last)
            else:
                line = self.add_column(
                    line,
                    '[%s](%sphy/%s.md)' % (
                        item['nei_interface_name'],
                        base,
                        item['nei_interface_hash']
                    ),
                    last=last
                )

        if item['nei_device_type'] is not None and item['nei_device_type'] == 'Server':
            if item['nei_interface_name'] is None:
                line = self.add_column(line, '---', last=last)
            else:
                line = self.add_column(line, item['nei_interface_name'], last=last)

        return line

    def print_aci_policy_table_bar(self, controller, section):
        line = '\n[Back](../README.md)'

        if section == 'domain-aaa':
            line = '%s Domain:AAA' % (line)
        else:
            line = '%s [Domain:AAA](./%s-domain-aaa.md)' % (line, controller)

        if section == 'domain-l2':
            line = '%s Domain:L2' % (line)
        else:
            line = '%s [Domain:L2](./%s-domain-l2.md)' % (line, controller)

        if section == 'domain-l3':
            line = '%s Domain:L3' % (line)
        else:
            line = '%s [Domain:L3](./%s-domain-l3.md)' % (line, controller)

        if section == 'domain-phy':
            line = '%s Domain:Phy' % (line)
        else:
            line = '%s [Domain:Phy](./%s-domain-phy.md)' % (line, controller)

        if section == 'domain-vmm':
            line = '%s Domain:VMM' % (line)
        else:
            line = '%s [Domain:VMM](./%s-domain-vmm.md)' % (line, controller)

        if section == 'aae':
            line = '%s AAE' % (line)
        else:
            line = '%s [AAE](./%s-aae.md)' % (line, controller)

        if section == 'pool-vlan':
            line = '%s Pool:VLAN' % (line)
        else:
            line = '%s [Pool:VLAN](./%s-pool-vlan.md)' % (line, controller)

        self.my_output.print_stream(
            line,
            'output'
        )

    def print_aci_global_table_bar(self, controller, section):
        line = '\n[Back](../README.md)'

        if section == 'tenant':
            line = '%s Tenant' % (line)
        else:
            line = '%s [Tenant](./%s-tenant.md)' % (line, controller)

        if section == 'ap':
            line = '%s AP' % (line)
        else:
            line = '%s [AP](./%s-ap.md)' % (line, controller)

        if section == 'epg':
            line = '%s EPG' % (line)
        else:
            line = '%s [EPG](./%s-epg.md)' % (line, controller)

        if section == 'bd':
            line = '%s BD' % (line)
        else:
            line = '%s [BD](./%s-bd.md)' % (line, controller)

        if section == 'vrf':
            line = '%s VRF' % (line)
        else:
            line = '%s [VRF](./%s-vrf.md)' % (line, controller)

        if section == 'l2out':
            line = '%s L2Out' % (line)
        else:
            line = '%s [L2Out](./%s-l2out.md)' % (line, controller)

        if section == 'l3out':
            line = '%s L3Out' % (line)
        else:
            line = '%s [L3Out](./%s-l3out.md)' % (line, controller)

        if section == 'l3mpls':
            line = '%s SR-MPLS L3Out' % (line)
        else:
            line = '%s [SR-MPLS L3Out](./%s-l3mpls.md)' % (line, controller)

        if section == 'contract-standard':
            line = '%s Contract' % (line)
        else:
            line = '%s [Contract](./%s-contract-standard.md)' % (line, controller)

        if section == 'contract-taboo':
            line = '%s Taboo' % (line)
        else:
            line = '%s [Taboo](./%s-contract-taboo.md)' % (line, controller)

        if section == 'contract-filter':
            line = '%s Filter' % (line)
        else:
            line = '%s [Filter](./%s-contract-filter.md)' % (line, controller)

        self.my_output.print_stream(
            line,
            'output'
        )

    def print_aci_controller_bar(self, current_controller, section):
        line = ''
        for controller_name in self.aci_controller_names:
            if current_controller == controller_name:
                line = '%s%s ' % (line, controller_name)
            else:
                line = '%s[%s](./%s-%s.md) ' % (line, controller_name, controller_name, section.replace(':', '-'))

        self.my_output.print_stream(
            '\n%s\n' % (line.strip()),
            'output'
        )

    def print_aci_controller_table_bar(self, controller, section):
        line = '\n[Back](../README.md)'

        if section == 'lacp':
            line = '%s LACP' % (line)
        else:
            line = '%s [LACP](./%s-lacp.md)' % (line, controller)

        if section == 'lldp':
            line = '%s LLDP' % (line)
        else:
            line = '%s [LLDP](./%s-lldp.md)' % (line, controller)

        if section == 'cdp':
            line = '%s CDP' % (line)
        else:
            line = '%s [CDP](./%s-cdp.md)' % (line, controller)

        if section == 'bgp':
            line = '%s BGP' % (line)
        else:
            line = '%s [BGP](./%s-bgp.md)' % (line, controller)

        if section == 'ep':
            line = '%s EP' % (line)
        else:
            line = '%s [EP](./%s-ep.md)' % (line, controller)

        if section == 'server':
            line = '%s Server' % (line)
        else:
            line = '%s [Server](./%s-server.md)' % (line, controller)

        if section == 'vmware':
            line = '%s VMWare' % (line)
        else:
            line = '%s [VMWare](./%s-vmware.md)' % (line, controller)

        if section == 'ocp':
            line = '%s OCP' % (line)
        else:
            line = '%s [OCP](./%s-ocp.md)' % (line, controller)

        self.my_output.print_stream(
            line,
            'output'
        )

    def print_aci_tenant_bar(self, controller, current_tenant, section):
        line = ''
        for aci_tenant_name in self.aci_tenant_names[controller]:
            if aci_tenant_name == current_tenant:
                line = '%s%s ' % (line, aci_tenant_name)
            else:
                line = '%s[%s](./%s-%s-%s.md) ' % (line, aci_tenant_name, controller, aci_tenant_name, section)

        self.my_output.print_stream(
            '\n%s\n' % (line.strip()),
            'output'
        )

    def print_aci_tenant_table_bar(self, controller, current_tenant, section):
        line = '\n[Back](../README.md)'
        if section == 'ap':
            line = '%s AP' % (line)
        else:
            line = '%s [AP](./%s-%s-ap.md)' % (line, controller, current_tenant)

        if section == 'epg':
            line = '%s EPG' % (line)
        else:
            line = '%s [EPG](./%s-%s-epg.md)' % (line, controller, current_tenant)

        if section == 'bd':
            line = '%s BD' % (line)
        else:
            line = '%s [BD](./%s-%s-bd.md)' % (line, controller, current_tenant)

        if section == 'vrf':
            line = '%s VRF' % (line)
        else:
            line = '%s [VRF](./%s-%s-vrf.md)' % (line, controller, current_tenant)

        if section == 'l2out':
            line = '%s L2Out' % (line)
        else:
            line = '%s [L2Out](./%s-%s-l2out.md)' % (line, controller, current_tenant)

        if section == 'l3out':
            line = '%s L3Out' % (line)
        else:
            line = '%s [L3Out](./%s-%s-l3out.md)' % (line, controller, current_tenant)

        if section == 'l3mpls':
            line = '%s SR-MPLS L3Out' % (line)
        else:
            line = '%s [SR-MPLS L3Out](./%s-%s-l3mpls.md)' % (line, controller, current_tenant)

        if section == 'contract':
            line = '%s Contract' % (line)
        else:
            line = '%s [Contract](./%s-%s-contract-standard.md)' % (line, controller, current_tenant)

        if section == 'taboo':
            line = '%s Taboo' % (line)
        else:
            line = '%s [Taboo](./%s-%s-contract-taboo.md)' % (line, controller, current_tenant)

        if section == 'filter':
            line = '%s Filter' % (line)
        else:
            line = '%s [Filter](./%s-%s-contract-filter.md)' % (line, controller, current_tenant)

        self.my_output.print_stream(
            line,
            'output'
        )

    def print_aci_node_bar(self, controller, current_node, section):
        line = ''
        for aci_node_name in self.aci_node_names[controller]:
            if aci_node_name == current_node:
                line = '%s%s ' % (line, aci_node_name)
            else:
                line = '%s[%s](./%s-%s-%s.md) ' % (line, aci_node_name, controller, aci_node_name, section.replace(':', '-'))

        self.my_output.print_stream(
            '\n%s\n' % (line.strip()),
            'output'
        )

    def print_aci_node_table_bar(self, controller, current_node, section):
        line = '\n[Back](../README.md)'
        if section == 'phy':
            line = '%s Phy' % (line)
        else:
            line = '%s [Phy](./%s-%s-phy.md)' % (line, controller, current_node)

        if section == 'phy:l2':
            line = '%s Phy:L2' % (line)
        else:
            line = '%s [Phy:L2](./%s-%s-phy-l2.md)' % (line, controller, current_node)

        if section == 'phy:vlan':
            line = '%s Phy:VLAN' % (line)
        else:
            line = '%s [Phy:VLAN](./%s-%s-phy-vlan.md)' % (line, controller, current_node)

        if section == 'phy:optics':
            line = '%s Phy:Optics' % (line)
        else:
            line = '%s [Phy:Optics](./%s-%s-phy-optics.md)' % (line, controller, current_node)

        if section == 'phy:epg':
            line = '%s Phy:EPG' % (line)
        else:
            line = '%s [Phy:EPG](./%s-%s-phy-epg.md)' % (line, controller, current_node)

        if section == 'phy:policy':
            line = '%s Phy:Policy' % (line)
        else:
            line = '%s [Phy:Policy](./%s-%s-phy-policy.md)' % (line, controller, current_node)

        if section == 'phy:pc':
            line = '%s PC' % (line)
        else:
            line = '%s [PC](./%s-%s-pc.md)' % (line, controller, current_node)

        if section == 'lacp':
            line = '%s LACP' % (line)
        else:
            line = '%s [LACP](./%s-%s-lacp.md)' % (line, controller, current_node)

        if section == 'lldp':
            line = '%s LLDP' % (line)
        else:
            line = '%s [LLDP](./%s-%s-lldp.md)' % (line, controller, current_node)

        if section == 'cdp':
            line = '%s CDP' % (line)
        else:
            line = '%s [CDP](./%s-%s-cdp.md)' % (line, controller, current_node)

        if section == 'server':
            line = '%s Server' % (line)
        else:
            line = '%s [Server](./%s-%s-server.md)' % (line, controller, current_node)

        if section == 'vmware':
            line = '%s VMWare' % (line)
        else:
            line = '%s [VMWare](./%s-%s-vmware.md)' % (line, controller, current_node)

        if section == 'ocp':
            line = '%s OCP' % (line)
        else:
            line = '%s [OCP](./%s-%s-ocp.md)' % (line, controller, current_node)

        self.my_output.print_stream(
            line,
            'output'
        )

    def print_readme_aci_policy(self):
        self.my_output.print_stream(
            '\nAPIC | D:AAA | D:L2 | D:L3 | D:Phy | D:VMM | AAE | P:VLAN',
            'output'
        )

        self.my_output.print_stream(
            '--- | --- | --- | --- | --- | --- | --- | --- ',
            'output'
        )

        for controller_name in self.aci_controller_names:
            line = ''
            line = self.add_column(line, controller_name)
            line = self.add_column(
                line,
                '[%s](./apic/%s-domain-aaa.md)' % (
                    self.aci_domain_aaa_count[controller_name],
                    controller_name
                )
            )
            line = self.add_column(
                line,
                '[%s](./apic/%s-domain-l2.md)' % (
                    self.aci_domain_l2_count[controller_name],
                    controller_name
                )
            )
            line = self.add_column(
                line,
                '[%s](./apic/%s-domain-l3.md)' % (
                    self.aci_domain_l3_count[controller_name],
                    controller_name
                )
            )
            line = self.add_column(
                line,
                '[%s](./apic/%s-domain-phy.md)' % (
                    self.aci_domain_phy_count[controller_name],
                    controller_name
                )
            )
            line = self.add_column(
                line,
                '[%s](./apic/%s-domain-vmm.md)' % (
                    self.aci_domain_vmm_count[controller_name],
                    controller_name
                )
            )
            line = self.add_column(
                line,
                '[%s](./apic/%s-aae.md)' % (
                    self.aci_aae_count[controller_name],
                    controller_name
                )
            )
            line = self.add_column(
                line,
                '[%s](./apic/%s-pool-vlan.md)' % (
                    self.aci_pool_vlan_count[controller_name],
                    controller_name
                )
            )
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('\n\n', 'output')

    def print_readme_aci_tenant(self):
        self.my_output.print_stream(
            '\nAPIC | Tenant | AP | EPG | BD | VRF | L2Out | L3Out | SR-MPLS L3Out | Contract | Taboo | Filter ',
            'output'
        )

        self.my_output.print_stream(
            '--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---',
            'output'
        )

        for controller_name in self.aci_controller_names:
            line = ''
            line = self.add_column(line, controller_name)
            line = self.add_column(
                line,
                '[%s](./apic/%s-tenant.md)' % (
                    self.aci_tenant_count[controller_name],
                    controller_name
                )
            )
            line = self.add_column(
                line,
                '[%s](./apic/%s-ap.md)' % (
                    self.aci_ap_count[controller_name],
                    controller_name
                )
            )
            line = self.add_column(
                line,
                '[%s](./apic/%s-epg.md)' % (
                    self.aci_epg_count[controller_name],
                    controller_name
                )
            )
            line = self.add_column(
                line,
                '[%s](./apic/%s-bd.md)' % (
                    self.aci_bd_count[controller_name],
                    controller_name
                )
            )
            line = self.add_column(
                line,
                '[%s](./apic/%s-vrf.md)' % (
                    self.aci_vrf_count[controller_name],
                    controller_name
                )
            )
            line = self.add_column(
                line,
                '[%s](./apic/%s-l2out.md)' % (
                    self.aci_l2out_count[controller_name],
                    controller_name
                )
            )
            line = self.add_column(
                line,
                '[%s](./apic/%s-l3out.md)' % (
                    self.aci_l3out_count[controller_name],
                    controller_name
                )
            )
            line = self.add_column(
                line,
                '[%s](./apic/%s-l3mpls.md)' % (
                    self.aci_l3mpls_count[controller_name],
                    controller_name
                )
            )
            line = self.add_column(
                line,
                '[%s](./apic/%s-contract-standard.md)' % (
                    self.aci_contract_standard_count[controller_name],
                    controller_name
                )
            )
            line = self.add_column(
                line,
                '[%s](./apic/%s-contract-taboo.md)' % (
                    self.aci_contract_taboo_count[controller_name],
                    controller_name
                )
            )
            line = self.add_column(
                line,
                '[%s](./apic/%s-contract-filter.md)' % (
                    self.aci_contract_filter_count[controller_name],
                    controller_name
                )
            )
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('\n\n', 'output')

    def print_readme_aci_node(self):
        self.my_output.print_stream(
            'APIC | Node | Eth | PC | LACP | LLDP | CDP | BGP | EP | Server | VMWare | OCP',
            'output'
        )

        self.my_output.print_stream(
            '--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---',
            'output'
        )

        for controller_name in self.aci_controller_names:
            line = ''
            # APIC,
            line = self.add_column(
                line,
                controller_name
            )
            # Node
            line = self.add_column(line, '---')
            # Eth
            line = self.add_column(line, '---')
            # PC
            line = self.add_column(line, '---')
            # LACP
            line = self.add_column(
                line,
                '[%s](./apic/%s-lacp.md)' % (
                    self.aci_lacp_count[controller_name],
                    controller_name
                )
            )
            # LLDP
            line = self.add_column(
                line,
                '[%s](./apic/%s-lldp.md)' % (
                    self.aci_lldp_count[controller_name],
                    controller_name
                )
            )
            # CDP
            line = self.add_column(
                line,
                '[%s](./apic/%s-cdp.md)' % (
                    self.aci_cdp_count[controller_name],
                    controller_name
                )
            )
            # BGP
            line = self.add_column(
                line,
                '[%s](./apic/%s-cdp.md)' % (
                    self.aci_bgp_count[controller_name],
                    controller_name
                )
            )
            # EP
            line = self.add_column(
                line,
                '[%s](./apic/%s-ep.md)' % (
                    self.aci_ep_count[controller_name],
                    controller_name
                )
            )
            # Server
            line = self.add_column(
                line,
                '[%s](./apic/%s-server.md)' % (
                    self.aci_server_count[controller_name],
                    controller_name
                )
            )
            # VMWare
            line = self.add_column(
                line,
                '[%s](./apic/%s-vmware.md)' % (
                    self.aci_vmware_count[controller_name],
                    controller_name
                )
            )
            # OCP
            line = self.add_column(
                line,
                '[%s](./apic/%s-ocp.md)' % (
                    self.aci_ocp_count[controller_name],
                    controller_name
                )
            )
            self.my_output.print_stream(
                line,
                'output'
            )

            for node_name in self.aci_node_names[controller_name]:
                line = ''
                # APIC,
                line = self.add_column(
                    line,
                    controller_name
                )
                # Node
                line = self.add_column(
                    line,
                    '[%s](./apic/%s-%s-node.md)' % (
                        node_name,
                        controller_name,
                        node_name
                    )
                )
                # Eth
                line = self.add_column(
                    line,
                    '[%s/%s](./apic/%s-%s-phy.md)' % (
                        self.aci_node_phy_up_count[controller_name][node_name],
                        self.aci_node_phy_count[controller_name][node_name],
                        controller_name,
                        node_name
                    )
                )
                # PC
                line = self.add_column(
                    line,
                    '[PC](./apic/%s-%s-pc.md)' % (
                        controller_name,
                        node_name
                    )
                )
                # LACP
                line = self.add_column(
                    line,
                    '[%s](./apic/%s-%s-lacp.md)' % (
                        self.aci_node_lacp_count[controller_name][node_name],
                        controller_name,
                        node_name
                    )
                )
                # LLDP
                line = self.add_column(
                    line,
                    '[%s](./apic/%s-%s-lldp.md)' % (
                        self.aci_node_lldp_count[controller_name][node_name],
                        controller_name,
                        node_name
                    )
                )
                # CDP
                line = self.add_column(
                    line,
                    '[%s](./apic/%s-%s-cdp.md)' % (
                        self.aci_node_cdp_count[controller_name][node_name],
                        controller_name,
                        node_name
                    )
                )
                # BGP
                line = self.add_column(
                    line,
                    '[%s](./apic/%s-%s-bgp.md)' % (
                        self.aci_node_bgp_count[controller_name][node_name],
                        controller_name,
                        node_name
                    )
                )
                # EP
                line = self.add_column(line, '---')
                # Server
                line = self.add_column(
                    line,
                    '[%s](./apic/%s-%s-server.md)' % (
                        self.aci_node_server_count[controller_name][node_name],
                        controller_name,
                        node_name
                    )
                )
                # VMWare
                line = self.add_column(
                    line,
                    '[%s](./apic/%s-%s-vmware.md)' % (
                        self.aci_node_vmware_count[controller_name][node_name],
                        controller_name,
                        node_name
                    )
                )
                # OCP
                line = self.add_column(
                    line,
                    '[%s](./apic/%s-%s-ocp.md)' % (
                        self.aci_node_ocp_count[controller_name][node_name],
                        controller_name,
                        node_name
                    )
                )
                self.my_output.print_stream(
                    line,
                    'output'
                )

    def print_readme_aci(self):
        self.my_output.print_stream(
            '\n## ACI\n',
            'output'
        )

        self.print_readme_aci_policy()
        self.print_readme_aci_tenant()
        self.print_readme_aci_node()

    def print_aci(self, servers):
        self.my_output.default('ACI...')

        self.copy_file(
            os.path.join(self.get_aci_template_dir(), 'access_policy.png'),
            'access_policy.png',
            subdir='apic/phy'
        )

        aci_node_servers = self.xd_handler.get_aci_node_servers()

        nodes = self.xd_handler.get_aci_node()
        node_commands = self.xd_handler.get_aci_node_cmd()
        for controller in self.aci_controller_names:
            for node in nodes[controller]:
                self.print_aci_node(controller, node)
                phy = self.xd_handler.get_aci_phy(controller, node['id'])
                self.print_aci_node_phy(
                    controller,
                    node['name'],
                    phy,
                    aci_node_servers[controller][node['name']],
                    servers,
                    node_commands[controller][node['id']]
                )

        for controller in self.aci_controller_names:
            self.print_aci_server(
                aci_node_servers[controller],
                controller
            )

            self.print_aci_vmware(
                aci_node_servers[controller],
                controller
            )

            self.print_aci_ocp(
                aci_node_servers[controller],
                controller
            )

            for node_name in self.aci_node_names[controller]:
                self.print_aci_node_server(
                    aci_node_servers[controller][node_name],
                    controller,
                    node_name,
                    self.xd_handler.get_aci_node_id_by_name(node_name)
                )

                self.print_aci_node_vmware(
                    aci_node_servers[controller][node_name],
                    controller,
                    node_name,
                    self.xd_handler.get_aci_node_id_by_name(node_name)
                )

                self.print_aci_node_ocp(
                    aci_node_servers[controller][node_name],
                    controller,
                    node_name,
                    self.xd_handler.get_aci_node_id_by_name(node_name)
                )

        ep = self.xd_handler.get_aci_ep()
        for controller in self.aci_controller_names:
            self.print_aci_ep(ep[controller], controller)

        cdp = self.xd_handler.get_aci_cdp()
        for controller in self.aci_controller_names:
            self.print_aci_cdp(cdp[controller], controller)
            for node_name in self.aci_node_names[controller]:
                self.print_aci_node_cdp(cdp[controller], controller, node_name, servers)

        lldp = self.xd_handler.get_aci_lldp()
        for controller in self.aci_controller_names:
            self.print_aci_lldp(lldp[controller], controller)
            for node_name in self.aci_node_names[controller]:
                self.print_aci_node_lldp(lldp[controller], controller, node_name, servers)

        lacp = self.xd_handler.get_aci_lacp()
        for controller in self.aci_controller_names:
            self.print_aci_lacp(lacp[controller], controller, self.aci_node_mapping)
            for node_name in self.aci_node_names[controller]:
                self.print_aci_node_lacp(lacp[controller], controller, node_name, self.aci_node_mapping)

        tenant = self.xd_handler.get_aci_tenant()
        for controller in tenant:
            self.print_aci_tenant(tenant[controller], controller)

        ap = self.xd_handler.get_aci_ap()
        for controller in ap:
            self.print_aci_ap(ap[controller], controller)
            for tenant in self.aci_tenant_names[controller]:
                self.print_aci_tenant_ap(ap[controller], tenant, controller)

        bd = self.xd_handler.get_aci_bd()
        for controller in bd:
            self.print_aci_bd(bd[controller], controller)
            for tenant in self.aci_tenant_names[controller]:
                self.print_aci_tenant_bd(bd[controller], tenant, controller)

        epg = self.xd_handler.get_aci_epg()
        for controller in epg:
            self.print_aci_epg(epg[controller], controller)
            for tenant in self.aci_tenant_names[controller]:
                self.print_aci_tenant_epg(epg[controller], tenant, controller)

        vrf = self.xd_handler.get_aci_vrf()
        for controller in vrf:
            self.print_aci_vrf(vrf[controller], controller)
            for tenant in self.aci_tenant_names[controller]:
                self.print_aci_tenant_vrf(vrf[controller], tenant, controller)

        l2out = self.xd_handler.get_aci_l2out()
        for controller in l2out:
            self.print_aci_l2out(l2out[controller], controller)
            for tenant in self.aci_tenant_names[controller]:
                self.print_aci_tenant_l2out(l2out[controller], tenant, controller)

        l3out = self.xd_handler.get_aci_l3out()
        for controller in l3out:
            self.print_aci_l3out(l3out[controller], controller)
            self.print_aci_l3mpls(l3out[controller], controller)
            for tenant in self.aci_tenant_names[controller]:
                self.print_aci_tenant_l3out(l3out[controller], tenant, controller)
                self.print_aci_tenant_l3mpls(l3out[controller], tenant, controller)

        aae = self.xd_handler.get_aci_aae()
        for controller in aae:
            self.print_aci_aae(aae[controller], controller)

        domain = self.xd_handler.get_aci_domain_aaa()
        for controller in domain:
            self.print_aci_domain_aaa(domain[controller], controller)

        domain = self.xd_handler.get_aci_domain_l2()
        for controller in domain:
            self.print_aci_domain_l2(domain[controller], controller)

        domain = self.xd_handler.get_aci_domain_l3()
        for controller in domain:
            self.print_aci_domain_l3(domain[controller], controller)

        domain = self.xd_handler.get_aci_domain_phy()
        for controller in domain:
            self.print_aci_domain_phy(domain[controller], controller)

        domain = self.xd_handler.get_aci_domain_vmm()
        for controller in domain:
            self.print_aci_domain_vmm(domain[controller], controller)

        pool = self.xd_handler.get_aci_pool_vlan()
        for controller in pool:
            self.print_aci_pool_vlan(pool[controller], controller)

        contract = self.xd_handler.get_aci_contract_filter()
        for controller in contract:
            self.print_aci_contract_filter(contract[controller], controller)
            for tenant in self.aci_tenant_names[controller]:
                self.print_aci_tenant_contract_filter(contract[controller], tenant, controller)

        contract = self.xd_handler.get_aci_contract_standard()
        for controller in contract:
            self.print_aci_contract_standard(contract[controller], controller)
            for tenant in self.aci_tenant_names[controller]:
                self.print_aci_tenant_contract_standard(contract[controller], tenant, controller)

        contract = self.xd_handler.get_aci_contract_taboo()
        for controller in contract:
            self.print_aci_contract_taboo(contract[controller], controller)
            for tenant in self.aci_tenant_names[controller]:
                self.print_aci_tenant_contract_taboo(contract[controller], tenant, controller)
