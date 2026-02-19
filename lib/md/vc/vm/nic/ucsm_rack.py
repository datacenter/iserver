from lib import ip_helper


class MdVcVmNicUcsmRackOutput():
    def __init__(self):
        pass

    def add_vc_vm_nic_ucsm_rack_summary(self, nic):
        self.my_output.print_stream('## Summary', 'output')
        order = [
            'Domain',
            'Step',
            'Identity',
            'Detail'
        ]
        self.print_table_header(order)

        line = ''
        line = self.add_column(line, 'VMWare')
        line = self.add_column(line, 'NIC')
        line = self.add_column(line, nic['label'])
        line = self.add_column(line, 'Type: %s, MAC: %s' % (nic['type'], nic['macAddress']))
        self.my_output.print_stream(line, 'output')

        line = ''
        line = self.add_column(line, 'VMWare')
        line = self.add_column(line, 'Network')
        line = self.add_column(line, nic['networkName'])
        line = self.add_column(line, 'VLAN: %s' % (', '.join(nic['fabric']['vmware']['vlans'])))
        self.my_output.print_stream(line, 'output')

        line = ''
        line = self.add_column(line, 'VMWare')
        line = self.add_column(line, 'vSwitch')
        line = self.add_column(line, nic['fabric']['vmware']['vswitchName'])
        line = self.add_column(line, nic['fabric']['vmware']['vswitchType'])
        self.my_output.print_stream(line, 'output')

        pnic_names = []
        for pnic in nic['fabric']['vmware']['pnic']:
            pnic_names.append(
                pnic['device']
            )

        line = ''
        line = self.add_column(line, 'VMWare')
        line = self.add_column(line, 'Device')
        line = self.add_column(line, ', '.join(pnic_names))
        line = self.add_column(line, '')
        self.my_output.print_stream(line, 'output')

        for pnic in nic['fabric']['vmware']['pnic']:
            self.my_output.print_stream('### vSwitch Upstream Device: %s' % (pnic['device']), 'output')

            order = [
                'Domain',
                'Step',
                'Identity',
                'Detail'
            ]
            self.print_table_header(order)

            for adapter in nic['fabric']['server']['adapter']:
                if ip_helper.is_mac_equal(pnic['mac'], adapter['MacAddress']):
                    line = ''
                    line = self.add_column(line, 'Server')
                    line = self.add_column(line, 'Interface')
                    line = self.add_column(line, adapter['InterfaceName'])
                    line = self.add_column(line, '%s - %s' % (nic['fabric']['server']['name'], adapter['AdapterModel']))
                    self.my_output.print_stream(line, 'output')

                    line = ''
                    line = self.add_column(line, 'Server')
                    line = self.add_column(line, 'vNIC')
                    line = self.add_column(line, adapter['vnic']['name'])
                    for vif in adapter['vnic']['vif']:
                        if vif['oper_state'] == 'active':
                            line = self.add_column(
                                line,
                                'VIF ID %s (Side: %s)' % (
                                    vif['id'],
                                    vif['switch_id']
                                )
                            )

                    self.my_output.print_stream(line, 'output')

                    line = ''
                    line = self.add_column(line, 'FI')
                    line = self.add_column(line, 'Server Port')

                    ports = []
                    fi_pc = None
                    for port in adapter['fi_vic']:
                        ports.append(
                            '%s/%s' % (
                                port['slot_id'],
                                port['port_id']
                            )
                        )
                        fi_pc = port['ep_dn'].split('/')[3]

                    ports = sorted(ports)
                    line = self.add_column(line, ', '.join(ports))
                    line = self.add_column(line, fi_pc)
                    self.my_output.print_stream(line, 'output')

                    for vlan_id in adapter['vlan']:
                        line = ''
                        line = self.add_column(line, 'FI')
                        line = self.add_column(line, 'Port Channel')
                        line = self.add_column(line, '%s (%s)' % (adapter['vlan'][vlan_id]['pc']['name'], adapter['vlan'][vlan_id]['pc']['port_id']))

                        ports = []
                        for port in adapter['vlan'][vlan_id]['ep']:
                            ports.append(
                                '%s/%s' % (
                                    port['slot_id'],
                                    port['port_id']
                                )
                            )

                        ports = sorted(ports)
                        line = self.add_column(line, ', '.join(ports))
                        self.my_output.print_stream(line, 'output')

                        for ep in adapter['vlan'][vlan_id]['ep']:
                            line = ''
                            line = self.add_column(line, ep['fabric_type'])
                            line = self.add_column(line, ep['fabric_switch'])
                            line = self.add_column(line, ep['fabric_interface'])
                            line = self.add_column(
                                line,
                                'FI %s/%s' % (
                                    ep['slot_id'],
                                    ep['port_id']
                                )
                            )
                            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')
