from lib import ip_helper
from lib.nexus import helper as nexus_helper
from lib.md.nexus.cdp import MdNexusCdpOutput
from lib.md.nexus.configuration import MdNexusConfigurationOutput
from lib.md.nexus.feature import MdNexusFeatureOutput
from lib.md.nexus.hardware import MdNexusHardwareOutput
from lib.md.nexus.interface.main import MdNexusInterfaceOutput
from lib.md.nexus.lldp import MdNexusLldpOutput
from lib.md.nexus.mac import MdNexusMacOutput
from lib.md.nexus.management import MdNexusManagementOutput
from lib.md.nexus.ocp import MdNexusOcpOutput
from lib.md.nexus.server import MdNexusServerOutput
from lib.md.nexus.topology import MdNexusTopologyOutput
from lib.md.nexus.vc import MdNexusVcOutput
from lib.md.nexus.vpc import MdNexusVpcOutput


class MdNexusOutput(
        MdNexusCdpOutput,
        MdNexusConfigurationOutput,
        MdNexusFeatureOutput,
        MdNexusHardwareOutput,
        MdNexusInterfaceOutput,
        MdNexusLldpOutput,
        MdNexusMacOutput,
        MdNexusManagementOutput,
        MdNexusOcpOutput,
        MdNexusServerOutput,
        MdNexusTopologyOutput,
        MdNexusVcOutput,
        MdNexusVpcOutput
    ):
    def __init__(self):
        MdNexusCdpOutput.__init__(self)
        MdNexusConfigurationOutput.__init__(self)
        MdNexusFeatureOutput.__init__(self)
        MdNexusHardwareOutput.__init__(self)
        MdNexusInterfaceOutput.__init__(self)
        MdNexusLldpOutput.__init__(self)
        MdNexusMacOutput.__init__(self)
        MdNexusManagementOutput.__init__(self)
        MdNexusOcpOutput.__init__(self)
        MdNexusServerOutput.__init__(self)
        MdNexusTopologyOutput.__init__(self)
        MdNexusVcOutput.__init__(self)
        MdNexusVpcOutput.__init__(self)

    def add_nexus_interface(self, line, nexus_name, value, up=False, down=False):
        base = './'
        if up:
            base = '../'
        if down:
            base = './nexus/'

        port_type = nexus_helper.get_nexus_interface_type(value)
        port_hash = nexus_helper.get_nexus_interface_hash(nexus_name, value)
        if port_hash is None:
            line = self.add_column(line, value)
        else:
            line = self.add_column(
                line,
                '[%s](%s%s/%s.md)' % (
                    value,
                    base,
                    port_type,
                    port_hash
                )
            )

        return line

    def add_nexus_port_mode(self, line, item):
        if item['portmode'] == 'trunk':
            line = self.add_column(line, item['portmode'])
        if item['portmode'] == 'routed':
            line = self.add_column(line, item['portmode'])
        if item['portmode'] == 'access':
            line = self.add_column(line, '%s (%s)' % (item['portmode'], item['vlan']))

        return line

    def add_nexus_connected_device_name(self, line, item, up=False, last=False):
        base = './'
        if up:
            base = '../'

        if 'nei_device_type' not in item:
            item['nei_device_type'] = None

        if 'nei_device_name' not in item:
            item['nei_device_name'] = None

        if item['nei_device_type'] is None or item['nei_device_type'] not in ['Nexus', 'ACI', 'FI', 'Server']:
            if item['nei_device_name'] is None:
                line = self.add_column(line, '---', last=last)
            else:
                line = self.add_column(line, item['nei_device_name'], last=last)

        if item['nei_device_type'] is not None and item['nei_device_type'] == 'Nexus':
            if self.xd_handler.is_nexus_device_name(item['nei_device_name']):
                line = self.add_column(
                    line,
                    '[%s](%s%s-eth.md)' % (
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
            line = self.add_column(
                line,
                item['nei_device_name'],
                last=last
            )

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

    def add_nexus_connected_device_interface(self, line, item, up=False, last=False):
        base = './'
        if up:
            base = '../'

        if 'nei_device_type' not in item:
            item['nei_device_type'] = None

        if 'nei_interface_name' not in item:
            item['nei_interface_name'] = None

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
                        '[%s](%s%s/%s.md)' % (
                            item['nei_interface_name'],
                            base,
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
                line = self.add_column(line, item['nei_interface_name'], last=last)

        if item['nei_device_type'] is not None and item['nei_device_type'] == 'Server':
            if item['nei_interface_name'] is None:
                line = self.add_column(line, '---', last=last)
            else:
                line = self.add_column(line, item['nei_interface_name'], last=last)

        return line

    def print_nexus_devices_bar(self, current_device, section):
        line = ''
        for nexus_device_name in self.nexus_device_names:
            if nexus_device_name == current_device:
                line = '%s%s ' % (line, nexus_device_name)
            else:
                line = '%s[%s](./%s-%s.md) ' % (line, nexus_device_name, nexus_device_name, section)

        self.my_output.print_stream(
            '\n%s\n' % (line.strip()),
            'output'
        )

    def print_nexus_table_bar(self, current_device, section):
        line = '\n[Back](../README.md)'
        if section == 'configuration':
            line = '%s Conf' % (line)
        else:
            line = '%s [Conf](./%s-configuration.md)' % (line, current_device)

        if section == 'eth':
            line = '%s Eth' % (line)
        else:
            line = '%s [Eth](./%s-eth.md)' % (line, current_device)

        if section == 'pc':
            line = '%s PC' % (line)
        else:
            line = '%s [PC](./%s-pc.md)' % (line, current_device)

        if section == 'vlan':
            line = '%s VLAN' % (line)
        else:
            line = '%s [VLAN](./%s-vlan.md)' % (line, current_device)

        if section == 'lldp':
            line = '%s LLDP' % (line)
        else:
            line = '%s [LLDP](./%s-lldp.md)' % (line, current_device)

        if section == 'cdp':
            line = '%s CDP' % (line)
        else:
            line = '%s [CDP](./%s-cdp.md)' % (line, current_device)

        if section == 'mac':
            line = '%s MAC' % (line)
        else:
            line = '%s [MAC](./%s-mac.md)' % (line, current_device)

        if section == 'server':
            line = '%s Server' % (line)
        else:
            line = '%s [Server](./%s-server.md)' % (line, current_device)

        if section == 'vmware':
            line = '%s VMWare' % (line)
        else:
            line = '%s [VMWare](./%s-vmware.md)' % (line, current_device)

        if section == 'ocp':
            line = '%s OCP' % (line)
        else:
            line = '%s [OCP](./%s-ocp.md)' % (line, current_device)

        self.my_output.print_stream(
            line,
            'output'
        )

    def print_nexus_overview_bar(self, section):
        line = '\n[Back](../README.md)'
        if section == 'hw':
            line = '%s HW/SW' % (line)
        else:
            line = '%s [HW/SW](./devices.md)' % (line)

        if section == 'features':
            line = '%s Features' % (line)
        else:
            line = '%s [Features](./features.md)' % (line)

        if section == 'mgmt':
            line = '%s Mgmt' % (line)
        else:
            line = '%s [Mgmt](./management.md)' % (line)

        if section == 'lldp':
            line = '%s LLDP' % (line)
        else:
            line = '%s [LLDP](./lldp.md)' % (line)

        if section == 'cdp':
            line = '%s CDP' % (line)
        else:
            line = '%s [CDP](./cdp.md)' % (line)

        if section == 'topology':
            line = '%s Topology' % (line)
        else:
            line = '%s [Topology](./topology.md)' % (line)

        if section == 'vpc':
            line = '%s VPC' % (line)
        else:
            line = '%s [VPC](./vpc.md)' % (line)

        if section == 'up':
            line = '%s Eth-Up' % (line)
        else:
            line = '%s [Eth-Up](./eth-up.md)' % (line)

        self.my_output.print_stream(
            line,
            'output'
        )

    def print_nexus_devices(self):
        nexus_devices = self.xd_handler.get_nexus_devices()
        self.print_page_header('Nexus Devices')
        self.print_nexus_overview_bar('hw')

        order = [
            'Device',
            'FQDN/IP',
            'HW',
            'SW'
        ]
        self.print_table_header(order)

        for name in self.nexus_device_names:
            device_fqdn = '--'
            for nexus_device in nexus_devices:
                if nexus_device['name'] == name:
                    device_fqdn = nexus_device['ip']

            hw = self.xd_handler.nexus_hw[name]
            if hw is None:
                hw = '---'
            else:
                if hw in self.nexus_hw:
                    hw = '[%s](./hw/%s/README.md)' % (hw, hw)

            sw = self.xd_handler.nexus_sw[name]
            if sw is None:
                sw = '---'

            self.my_output.print_stream(
                '%s | %s | %s | %s' % (
                    name,
                    device_fqdn,
                    hw,
                    sw
                ),
                'output'
            )

        self.save_output('devices', subdir='nexus')

    def print_nexus(self, servers):
        self.my_output.default('Nexus servers')
        nexus_intfs = self.xd_handler.get_nexus_server()
        nexus_servers = {}
        all_nexus_servers = []
        for key in nexus_intfs:
            nexus_servers[key] = []
            for intf in nexus_intfs[key]:
                nexus_servers[key].append(
                    nexus_intfs[key][intf]
                )
                all_nexus_servers.append(
                    nexus_intfs[key][intf]
                )

            self.print_nexus_servers(nexus_servers[key], key)
            self.print_nexus_servers_vcenter(nexus_servers[key], key)
            self.print_nexus_servers_ocp(nexus_servers[key], key)

        self.print_nexus_fabric_servers(all_nexus_servers)
        for key in self.xd_handler.vc_instance:
            self.print_nexus_fabric_servers_vcenter(
                all_nexus_servers,
                self.xd_handler.get_server_moids('vc-%s' % (key)),
                key
            )

        self.my_output.default('Nexus configuration')
        config = self.xd_handler.get_nexus_configuration()
        for name in self.nexus_device_names:
            self.print_nexus_configuration(config[name], name)

        self.my_output.default('Nexus vlan')
        vlan = self.xd_handler.get_nexus_vlan()

        self.my_output.default('Nexus vpc')
        vpc_keepalive = self.xd_handler.get_nexus_vpc_keepalive()
        vpc_role = self.xd_handler.get_nexus_vpc_role()
        vpc_state = self.xd_handler.get_nexus_vpc_state()

        self.my_output.default('Nexus cdp')
        cdp = self.xd_handler.get_nexus_cdp()
        self.print_nexus_cdp_all(cdp)
        for name in self.nexus_device_names:
            self.print_nexus_cdp(cdp[name], name, servers)

        self.my_output.default('Nexus lldp')
        lldp = self.xd_handler.get_nexus_lldp()
        self.print_nexus_lldp_all(lldp)
        for name in self.nexus_device_names:
            self.print_nexus_lldp(lldp[name], name, servers)

        self.my_output.default('Nexus mac')
        mac = self.xd_handler.get_nexus_mac_table()
        for name in self.nexus_device_names:
            self.print_nexus_mac_table(mac[name], name)

        self.my_output.default('Nexus interface')
        for nexus_name in self.nexus_device_names:
            self.print_nexus_interface_eth(
                nexus_name,
                self.xd_handler.get_nexus_interface_eth(nexus_name)
            )
            self.print_nexus_interface_pc(
                nexus_name,
                self.xd_handler.get_nexus_interface_pc(nexus_name),
                self.xd_handler.get_nexus_vpc_domain(nexus_name),
                self.xd_handler.get_nexus_interfaces_pc()
            )

            self.print_nexus_interface_vlan(
                nexus_name,
                self.xd_handler.get_nexus_interface_vlan(nexus_name),
                self.xd_handler.get_nexus_interface_eth(nexus_name),
                self.xd_handler.get_nexus_interface_pc(nexus_name),
                vlan[nexus_name]
            )

        self.print_nexus_interface_eth_up(
            self.xd_handler.get_nexus_interface()
        )

        self.my_output.default('Nexus feature')
        feature = self.xd_handler.get_nexus_feature()

        self.my_output.default('Nexus vrf')
        vrf = self.xd_handler.get_nexus_vrf()

        self.my_output.default('Nexus devices')
        self.print_nexus_hardware()
        self.print_nexus_features()
        self.print_nexus_devices()

        self.my_output.default('Nexus management')
        self.print_nexus_management(
            self.xd_handler.get_nexus_interface_mgmt()
        )

        self.my_output.default('Nexus topology')
        self.print_nexus_topology(
            self.xd_handler.get_nexus_interface()
        )

        self.my_output.default('Nexus vpc')
        self.print_nexus_vpc(
            self.xd_handler.get_nexus_vpc_domains()
        )

        return True
