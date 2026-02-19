import traceback

from lib import ip_helper


class LinuxInterface():
    def __init__(self):
        self.interfaces = None

    def get_interfaces_commands(self):
        commands = []
        commands.append('ip link show')
        return commands

    def is_interface_name_phys(self, name):
        if name == 'lo':
            return False

        if 'bond' in name:
            return False

        return True

    def analyze_ip_link_show_output(self, output, phys_only=False):
        interfaces = []

        info = None
        for line in output.split('\n'):
            if ' mtu ' in line:
                if info is not None:
                    if info['netns'] is not None:
                        info['phys'] = False
                    else:
                        info['phys'] = self.is_interface_name_phys(info['name'])

                    if not phys_only or info['phys']:
                        interfaces.append(
                            info
                        )

                info = {}
                info['index'] = line.split(':')[0]
                info['name'] = line.split(':')[1].strip()
                info['flags'] = line.split('<')[1].split('>')[0]
                info['mtu'] = line.split(' mtu ')[1].split(' ')[0]
                info['state'] = line.split(' state ')[1].split(' ')[0]
                info['up'] = False
                if info['state'] == 'UP':
                    info['up'] = True
                info['mac'] = ''
                info['netns'] = None
                info['vf'] = []

            if ' vf ' in line:
                vf_info = {}
                vf_info['index'] = line.split(' vf ')[1].split(' ')[0]
                vf_info['mac'] = line.split(' link/ether ')[1].split(' ')[0]
                if len(line.split(' link-netns ')) > 1:
                    info['netns'] = line.split(' link-netns ')[1].split(' ')[0]

                vf_info['vlan'] = None
                if ' vlan ' in line:
                    vf_info['vlan'] = line.split(' vlan ')[1].split(' ')[0].rstrip(',')
                vf_info['spoof'] = line.split(' spoof checking ')[1].split(' ')[0].rstrip(',')
                vf_info['link'] = line.split(' link-state ')[1].split(' ')[0].rstrip(',')
                vf_info['trust'] = line.split(' trust ')[1].split(' ')[0].rstrip(',')
                info['vf'].append(
                    vf_info
                )

            if ' vf ' not in line and ' link/ether ' in line:
                info['mac'] = line.split(' link/ether ')[1].split(' ')[0]
                if len(line.split(' link-netns ')) > 1:
                    info['netns'] = line.split(' link-netns ')[1].split(' ')[0]

        if info is not None:
            if info['netns'] is not None:
                info['phys'] = False
            else:
                info['phys'] = self.is_interface_name_phys(info['name'])

            if not phys_only or info['phys']:
                interfaces.append(
                    info
                )

        return interfaces

    def get_interface(self, mac_address, cache=False):
        if not cache or self.interfaces is None:
            self.interfaces = self.get_interfaces()
            if self.interfaces is None:
                return None

        for interface in self.interfaces:
            if ip_helper.is_mac_equal(interface['mac'], mac_address):
                interface['vf_info'] = None
                return interface

            for virtual_function in interface['vf']:
                if ip_helper.is_mac_equal(virtual_function['mac'], mac_address):
                    interface['vf_info'] = virtual_function
                    return interface

        return None

    def get_interface_by_name(self, name, cache=True):
        if not cache or self.interfaces is None:
            self.interfaces = self.get_interfaces()
            if self.interfaces is None:
                return None

        for interface in self.interfaces:
            if interface['name'] == name:
                return interface

        return None

    def get_interfaces(self, progress_bar=False, phys_only=False, ethtool=False, lspci=False, verbose=False):
        try:
            commands = self.get_interfaces_commands()
            if verbose:
                self.my_output.default('- ip link show')
            outputs = self.run_commands(commands, progress_bar=progress_bar)
            if outputs is None:
                self.my_output.error('Commands output collection failed')
                return None

            interfaces = self.analyze_ip_link_show_output(
                outputs['ip link show'],
                phys_only=phys_only
            )

        except BaseException:
            self.my_output.default(traceback.format_exc())
            return None

        if ethtool or lspci:
            for interface in interfaces:
                interface['ethtool'] = None
                if interface['phys']:
                    if verbose:
                        self.my_output.default('- ethtool [%s]' % (interface['name']))
                    interface['ethtool'] = self.get_inteface_ethtool(interface['name'])
                    if interface['ethtool'] is not None:
                        if interface['ethtool']['driver'] == 'iavf':
                            interface['phys'] = False

        if lspci:
            for interface in interfaces:
                interface['lspci'] = None
                if interface['phys'] and interface['ethtool'] is not None:
                    if len(interface['ethtool']['bus-info']) > 0:
                        if verbose:
                            self.my_output.default('- lspci %s [%s]' % (interface['name'], interface['ethtool']['bus-info']))
                        interface['lspci'] = self.get_inteface_lspci(interface['ethtool']['bus-info'])

        return interfaces

    def get_interfaces_state_up_map(self):
        interfaces = self.get_interfaces()
        if interfaces is None:
            return None

        state = {}
        for interface in interfaces:
            state[interface['name']] = interface['up']

        return state

    def get_sriov_interfaces(self, numa_info=False, pci_info=False):
        all_interfaces = self.get_interfaces()

        sriov_interfaces = []
        for interface in all_interfaces:
            if len(interface['vf']) > 0:
                interface['vfCount'] = len(interface['vf'])
                if numa_info:
                    interface['numa'] = self.get_interface_numa(
                        interface['name']
                    )

                if pci_info:
                    interface['pci'] = self.get_interface_pci(
                        interface['name']
                    )

                sriov_interfaces.append(
                    interface
                )

        return sriov_interfaces

    def get_interface_numa(self, interface_name):
        command = 'cat /sys/class/net/%s/device/numa_node' % (interface_name)
        outputs = self.run_commands([command])
        if outputs is None:
            self.my_output.error('Interface numa check failed failed:%s' % (interface_name))
            return None

        numa = outputs[command].strip().replace('\n', '')
        return numa

    def get_interface_pci(self, interface_name):
        command = 'cat /sys/class/net/%s/device/uevent' % (interface_name)
        outputs = self.run_commands([command])
        if outputs is None:
            self.my_output.error('Interface pci check failed failed:%s' % (interface_name))
            return None

        pci_info = {}

        for line in outputs[command].split('\n'):
            if len(line.split('=')) == 2:
                (key, value) = line.split('=')
                if key == 'DRIVER':
                    pci_info['driver'] = value
                    continue

                if key == 'PCI_CLASS':
                    pci_info['class'] = value
                    continue

                if key == 'PCI_ID':
                    pci_info['id'] = value
                    continue

                if key == 'PCI_SUBSYS_ID':
                    pci_info['subid'] = value
                    continue

                if key == 'PCI_SLOT_NAME':
                    pci_info['slot'] = value
                    continue

        return pci_info

    def get_inteface_ethtool(self, interface_name):
        command = 'ethtool -i %s' % (interface_name)
        outputs = self.run_commands([command])
        if outputs is None:
            self.my_output.error('Interface ethtool check failed failed:%s' % (interface_name))
            return None

        values = {}

        for line in outputs[command].strip().split('\n'):
            key = line.split(':')[0].strip()
            value = ':'.join(line.split(':')[1:]).strip()
            values[key] = value

        return values

    def get_inteface_ethtool_priv_flags(self, interface_name):
        command = 'ethtool --show-priv-flags %s' % (interface_name)
        outputs = self.run_commands([command])
        if outputs is None:
            self.my_output.error('Interface ethtool priv flags check failed failed:%s' % (interface_name))
            return None

        values = {}

        for line in outputs[command].strip().split('\n'):
            key = line.split(':')[0].strip()
            value = ':'.join(line.split(':')[1:]).strip()
            values[key] = value

        return values

    def set_inteface_ethtool_priv_flags(self, interface_name, flag, value):
        command = 'sudo ethtool --set-priv-flags %s %s %s' % (interface_name, flag, value)
        outputs = self.run_commands([command])
        return True

    def get_inteface_lspci(self, interface_slot):
        command = 'lspci -s %s' % (interface_slot)
        outputs = self.run_commands([command])
        if outputs is None:
            self.my_output.error('Interface lspci check failed:%s' % (interface_slot))
            return None

        lspci = outputs[command].strip().replace('\n', '')
        return lspci
