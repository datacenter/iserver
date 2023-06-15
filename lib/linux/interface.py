import traceback

from lib import ip_helper


class LinuxInterface():
    def __init__(self):
        self.interfaces = None

    def get_interfaces_commands(self):
        commands = []
        commands.append('ip link show')
        return commands

    def analyze_ip_link_show_output(self, output):
        interfaces = []

        info = None
        for line in output.split('\n'):
            if ' mtu ' in line:
                if info is not None:
                    interfaces.append(
                        info
                    )

                # 4: br-8bc193248176: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default
                info = {}
                info['index'] = line.split(':')[0]
                info['name'] = line.split(':')[1].strip()
                info['flags'] = line.split('<')[1].split('>')[0]
                info['mtu'] = line.split(' mtu ')[1].split(' ')[0]
                info['state'] = line.split(' state ')[1].split(' ')[0]
                info['mac'] = ''
                info['vf'] = []

            if ' vf ' in line:
                vf_info = {}
                vf_info['index'] = line.split(' vf ')[1].split(' ')[0]
                vf_info['mac'] = line.split(' link/ether ')[1].split(' ')[0]
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

        if info is not None:
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

    def get_interfaces(self, progress_bar=False):
        try:
            commands = self.get_interfaces_commands()
            outputs = self.run_commands(commands, progress_bar=progress_bar)
            if outputs is None:
                self.my_output.error('Commands output collection failed')
                return None

            interfaces = self.analyze_ip_link_show_output(
                outputs['ip link show']
            )

        except BaseException:
            self.my_output.default(traceback.format_exc())
            return None

        return interfaces

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

        # DRIVER=vmxnet3
        # PCI_CLASS=20000
        # PCI_ID=15AD:07B0
        # PCI_SUBSYS_ID=15AD:07B0
        # PCI_SLOT_NAME=0000:03:00.0
        # MODALIAS=pci:v000015ADd000007B0sv000015ADsd000007B0bc02sc00i00
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
