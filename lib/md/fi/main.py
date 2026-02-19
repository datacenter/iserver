from lib.md.fi.eth import MdFiEthOutput
from lib.md.fi.pc import MdFiPcOutput


class MdFiOutput(MdFiEthOutput, MdFiPcOutput):
    def __init__(self):
        MdFiEthOutput.__init__(self)
        MdFiPcOutput.__init__(self)

    def add_fi_connected_device_name(self, line, item, up=False, last=False):
        base = './'
        if up:
            base = '../'

        if item['Peer'] is not None:
            line = self.add_column(
                line,
                '[%s](%s../compute/%s-net.md)' % (
                    item['Peer']['ServerName'],
                    base,
                    item['Peer']['ServerMoid']
                ),
                last=last
            )
            return line

        if item['ACI'] is not None:
            line = self.add_column(
                line,
                '%s:[%s](../apic/%s-%s-phy.md)' % (
                    item['ACI']['apic'],
                    item['ACI']['node_name'],
                    item['ACI']['apic'],
                    item['ACI']['node_name']
                ),
                last=last
            )
            return line

        if item['Nexus'] is not None:
            line = self.add_column(
                line,
                '[%s](../nexus/%s-phy.md)' % (
                    item['Nexus']['device_name'],
                    item['Nexus']['device_name']
                ),
                last=last
            )
            return line

        line = self.add_column(line, '---')

        return line

    def add_fi_connected_device_interface(self, line, item, up=False, last=False):
        base = './'
        if up:
            base = '../'

        if item['Peer'] is not None:
            line = self.add_column(
                line,
                item['Peer']['ServerPort'],
                last=last
            )
            return line

        if item['ACI'] is not None:
            line = self.add_column(
                line,
                '[%s](../apic/phy/%s.md)' % (
                    item['ACI']['interface_id'],
                    item['ACI']['hash']
                ),
                last=last
            )
            return line

        if item['Nexus'] is not None:
            line = self.add_column(
                line,
                '[%s](../nexus/eth/%s.md)' % (
                    item['Nexus']['interface_id'],
                    item['Nexus']['hash']
                ),
                last=last
            )
            return line

        line = self.add_column(line, '---')
        return line

    def print_fi_devices_bar(self, current_device, section):
        line = ''
        for fi_name in self.fi_names_hash:
            if fi_name == current_device:
                line = '%s%s ' % (line, fi_name)
            else:
                line = '%s[%s](./%s-%s.md) ' % (line, fi_name, self.fi_names_hash[fi_name], section)

        self.my_output.print_stream(
            '\n%s\n' % (line.strip()),
            'output'
        )

    def print_fi_table_bar(self, current_device, section):
        line = '\n[Back](../README.md)'
        if section == 'eth':
            line = '%s Eth' % (line)
        else:
            line = '%s [Eth](./%s-eth.md)' % (line, self.fi_names_hash[current_device])

        if section == 'pc':
            line = '%s PC' % (line)
        else:
            line = '%s [PC](./%s-pc.md)' % (line, self.fi_names_hash[current_device])

        if section == 'server':
            line = '%s Server' % (line)
        else:
            line = '%s [Server](./%s-server.md)' % (line, self.fi_names_hash[current_device])

        if section == 'vmware':
            line = '%s VMWare' % (line)
        else:
            line = '%s [VMWare](./%s-vmware.md)' % (line, self.fi_names_hash[current_device])

        if section == 'ocp':
            line = '%s OCP' % (line)
        else:
            line = '%s [OCP](./%s-ocp.md)' % (line, self.fi_names_hash[current_device])

        self.my_output.print_stream(
            line,
            'output'
        )

    def print_fi(self, servers):
        self.my_output.default('FI ethernet')

        for fi_name in self.fi_names_hash:
            self.print_fi_interface_eth(
                fi_name,
                self.xd_handler.get_fi_by_name(fi_name),
                self.xd_handler.get_fi_interface_eth(fi_name),
                servers
            )

            self.print_fi_interface_pc(
                fi_name,
                self.xd_handler.get_fi_by_name(fi_name),
                self.xd_handler.get_fi_interface_pc(fi_name)
            )

