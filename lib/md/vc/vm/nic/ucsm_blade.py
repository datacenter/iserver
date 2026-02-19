from lib import ip_helper


class MdVcVmNicUcsmBladeOutput():
    def __init__(self):
        pass

    def add_vc_vm_nic_ucsm_blade_vmware(self, vm, info):
        self.my_output.print_stream('## VMWare', 'output')
        self.my_output.print_stream('- vCenter: [%s](../%s-vm.md)' % (vm['vcenter'], vm['vcenter']), 'output')
        self.my_output.print_stream('- Cluster: [%s](./%s.md)' % (vm['clusterName'], vm['cluster_hash']), 'output')
        self.my_output.print_stream('- Host: [%s](./%s.md)' % (vm['host'], vm['host_hash']), 'output')

        self.my_output.print_stream(
            '- Virtual Switch: %s (%s)' % (
                info['vswitchName'],
                info['vswitchType']
            ),
            'output'
        )
        self.my_output.print_stream(
            '- VLAN: %s' % (
                ', '.join(info['vlans'])
            ),
            'output'
        )

        self.my_output.print_stream('', 'output')
        order = [
            'Upstream Device',
            'MAC',
            'Dn'
        ]
        self.print_table_header(order)

        for pnic in info['pnic']:
            line = ''
            line = self.add_column(line, pnic['device'])
            line = self.add_column(line, pnic['mac'])
            line = self.add_column(line, pnic['interfaceDn'])
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

    def add_vc_vm_nic_ucsm_blade_server(self, info):
        self.my_output.print_stream('## Server', 'output')
        self.my_output.print_stream('- Name: %s' % (info['name']), 'output')
        self.my_output.print_stream('- Moid: %s' % (info['moid']), 'output')
        self.my_output.print_stream('- Serial: %s' % (info['type']), 'output')
        self.my_output.print_stream('- Management: UCSM', 'output')

        self.my_output.print_stream('', 'output')
        order = [
            'Server Adapter',
            'MAC',
            'Interface',
            'Dn'
        ]
        self.print_table_header(order)

        for adapter in info['adapter']:
            line = ''
            line = self.add_column(line, adapter['AdapterModel'])
            line = self.add_column(line, adapter['MacAddress'])
            line = self.add_column(line, adapter['InterfaceName'])
            line = self.add_column(line, adapter['InterfaceDn'])
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

    def add_vc_vm_nic_ucsm_blade_server_vic(self, info):
        self.my_output.print_stream('### VIC', 'output')
        self.my_output.print_stream('- Model: %s' % (info['model']), 'output')
        self.my_output.print_stream('- Serial: %s' % (info['serial']), 'output')
        self.my_output.print_stream('- Presence: %s' % (info['presence']), 'output')
        self.my_output.print_stream('- Power: %s' % (info['power']), 'output')
        self.my_output.print_stream('- Reachability: %s' % (info['reachability']), 'output')

        self.my_output.print_stream('', 'output')
        self.my_output.print_stream(
            '![GenericVic](./generic-vic-connectivity.png)',
            'output'
        )

        self.my_output.print_stream('', 'output')
        order = [
            'vNIC',
            'DCE ID',
            'Link',
            'Type',
            'Side',
            'IOM',
            'FI'
        ]
        self.print_table_header(order)

        for dce in info['dce']:
            line = ''
            if dce['used_by_vnic']:
                line = self.add_column(line, ':white_check_mark:')
            else:
                line = self.add_column(line, ':x:')

            line = self.add_column(line, dce['id'])
            line = self.add_column(line, dce['link_state'])
            line = self.add_column(line, dce['if_type'])
            line = self.add_column(line, dce['switch_id'])
            line = self.add_column(line, dce['peer_dn'].split('/')[-1])
            line = self.add_column(line, dce['ep_dn'].split('/')[-1])
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

    def add_vc_vm_nic_ucsm_blade_server_vnic(self, info):
        self.my_output.print_stream('### vNIC', 'output')
        self.my_output.print_stream('- Name: %s' % (info['name']), 'output')
        self.my_output.print_stream('- Dn: %s' % (info['dn']), 'output')
        self.my_output.print_stream('- vNIC Dn: %s' % (info['vnic_dn']), 'output')
        self.my_output.print_stream('- Interface: %s (%s)' % (info['if_role'], info['if_type']), 'output')
        self.my_output.print_stream('- Link state: %s' % (info['link_state']), 'output')
        self.my_output.print_stream('- MAC: %s' % (info['mac']), 'output')
        self.my_output.print_stream('- PCI: %s' % (info['pci_addr']), 'output')

        self.my_output.print_stream('', 'output')
        order = [
            'vNIC',
            'VIF ID',
            'Link',
            'State',
            'Role',
            'Side'
        ]
        self.print_table_header(order)

        for vif in info['vif']:
            line = ''
            if vif['oper_state'] == 'active':
                line = self.add_column(line, ':white_check_mark:')
            else:
                line = self.add_column(line, ':x:')

            line = self.add_column(line, vif['id'])
            line = self.add_column(line, vif['link_state'])
            line = self.add_column(line, vif['oper_state'])
            line = self.add_column(line, vif['prot_role'])
            line = self.add_column(line, vif['switch_id'])
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

    def add_vc_vm_nic_ucsm_blade_server_iom(self, iom_backplane, iom_backplane_pc, iom_fi):
        self.my_output.print_stream('### IOM', 'output')
        self.my_output.print_stream('- Model: %s' % (iom_fi[0]['model']), 'output')
        self.my_output.print_stream('- Serial: %s' % (iom_fi[0]['serial']), 'output')
        self.my_output.print_stream('- Slot ID: %s' % (iom_fi[0]['slot_id']), 'output')
        self.my_output.print_stream('- Side: %s' % (iom_fi[0]['switch_id']), 'output')

        self.my_output.print_stream('', 'output')
        self.my_output.print_stream('Backplane Port', 'output')
        self.my_output.print_stream('- ID: %s/%s' % (iom_backplane['slot_id'], iom_backplane['port_id']), 'output')
        self.my_output.print_stream('- State: %s' % (iom_backplane['oper_state']), 'output')
        self.my_output.print_stream('- Speed: %s' % (iom_backplane['admin_speed']), 'output')
        self.my_output.print_stream('- Adaptor type: %s' % (iom_backplane['connected_adaptor_type']), 'output')
        self.my_output.print_stream('- MAC: %s' % (iom_backplane['mac']), 'output')
        self.my_output.print_stream('- Transport: %s' % (iom_backplane['transport']), 'output')
        self.my_output.print_stream('- Interface: %s (%s)' % (iom_backplane['if_role'], iom_backplane['if_type']), 'output')
        self.my_output.print_stream('- PC (towards FI): %s' % (iom_backplane_pc['port_id']), 'output')

        self.my_output.print_stream('', 'output')
        order = [
            'Fabric Port ID',
            'State',
            'XCVR',
            'FI',
            'Interface'
        ]
        self.print_table_header(order)

        for uplink in iom_fi:
            line = ''
            line = self.add_column(line, uplink['port_id'])
            line = self.add_column(line, uplink['oper_state'])
            line = self.add_column(line, uplink['xcvr_type'])
            line = self.add_column(line, uplink['switch_id'])
            line = self.add_column(
                line, '%s/%s' % (
                    uplink['peer_slot_id'],
                    uplink['peer_port_id']
                )
            )
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

    def add_vc_vm_nic_ucsm_blade_server_fi(self, fi, fi_iom, vlan):
        self.my_output.print_stream('### Fabric Interconnect', 'output')
        self.my_output.print_stream('- Model: %s' % (fi['model']), 'output')
        self.my_output.print_stream('- Serial: %s' % (fi['serial']), 'output')
        self.my_output.print_stream('- Side: %s' % (fi['id']), 'output')
        self.my_output.print_stream('- Operability: %s' % (fi['operability']), 'output')

        self.my_output.print_stream('', 'output')
        order = [
            'Interface',
            'State',
            'Speed',
            'XCVR',
            'IOM'
        ]
        self.print_table_header(order)

        for link in fi_iom:
            line = ''
            line = self.add_column(line, '%s/%s' % (link['slot_id'], link['port_id']))
            line = self.add_column(line, link['oper_state'])
            line = self.add_column(line, link['oper_speed'])
            line = self.add_column(line, link['xcvr_type'])
            line = self.add_column(
                line,
                '%s %s %s' % (
                    link['peer_dn'].split('/')[1],
                    link['peer_dn'].split('/')[2],
                    link['peer_dn'].split('/')[4]
                )
            )
            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')
        order = [
            'VLAN',
            'VLAN Group',
            'Port Channel',
            'Interface',
            'State',
            'Speed',
            'XCVR',
            'Fabric',
            'Switch',
            'Interface'
        ]
        self.print_table_header(order)

        for vlan_id in vlan:
            for ep in vlan[vlan_id]['ep']:
                line = ''
                line = self.add_column(line, vlan_id)
                line = self.add_column(line, vlan[vlan_id]['netGroup']['name'])
                line = self.add_column(
                    line,
                    '%s (%s)' % (
                        vlan[vlan_id]['pc']['name'],
                        vlan[vlan_id]['pc']['port_id']
                    )
                )
                line = self.add_column(
                    line,
                    '%s/%s' % (
                        ep['slot_id'],
                        ep['port_id']
                    )
                )
                line = self.add_column(line, ep['oper_state'])
                line = self.add_column(line, ep['eth']['oper_speed'])
                line = self.add_column(line, ep['eth']['xcvr_type'])
                line = self.add_column(line, ep['fabric_type'])
                line = self.add_column(line, ep['fabric_switch'])
                line = self.add_column(line, ep['fabric_interface'])
                self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('', 'output')

    def add_vc_vm_nic_ucsm_blade_details(self, vm, fabric):
        self.my_output.print_stream('## Details', 'output')
        self.add_vc_vm_nic_ucsm_blade_vmware(vm, fabric['vmware'])
        self.add_vc_vm_nic_ucsm_blade_server(fabric['server'])
        for adapter in fabric['server']['adapter']:
            self.my_output.print_stream('## Interface [%s]' % (adapter['InterfaceName']), 'output')
            self.add_vc_vm_nic_ucsm_blade_server_vic(adapter['vic'])
            self.add_vc_vm_nic_ucsm_blade_server_vnic(adapter['vnic'])
            self.add_vc_vm_nic_ucsm_blade_server_iom(
                adapter['iom_backplane'],
                adapter['iom_backplane_pc'],
                adapter['iom_fi']
            )
            self.add_vc_vm_nic_ucsm_blade_server_fi(
                adapter['fi'],
                adapter['fi_iom'],
                adapter['vlan']
            )

    def add_vc_vm_nic_ucsm_blade_summary(self, nic):
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

        for pnic in nic['fabric']['vmware']['pnic']:
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
                            line = self.add_column(line, 'VIF ID %s' % (vif['id']))
                    self.my_output.print_stream(line, 'output')

                    line = ''
                    line = self.add_column(line, 'Chassis')
                    line = self.add_column(line, 'IOM')
                    line = self.add_column(line, 'Slot: %s' % (adapter['dce']['slot_id']))
                    line = self.add_column(line, 'Side: %s' % (adapter['dce']['switch_id']))
                    self.my_output.print_stream(line, 'output')

                    line = ''
                    line = self.add_column(line, 'FI')
                    line = self.add_column(line, 'Server Port')

                    ports = []
                    fi_pc = None
                    for port in adapter['fi_iom']:
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

    def add_vc_vm_nic_ucsm_blade_legend(self):
        self.my_output.print_stream('## Reference', 'output')
        self.my_output.print_stream('- VMWare', 'output')
        self.my_output.print_stream('\t - VM with interface backed with network', 'output')
        self.my_output.print_stream('\t - Network connected to virtual switch', 'output')
        self.my_output.print_stream('\t - Virtual switch with upstream interface(s)', 'output')
        self.my_output.print_stream('- Blade Server (UCSM)', 'output')
        self.my_output.print_stream('\t - vNIC behind VMWare network device', 'output')
        self.my_output.print_stream('\t - vNIC configured on Cisco VIC adapter', 'output')
        self.my_output.print_stream('- UCS Chassis', 'output')
        self.my_output.print_stream('\t - IOM/FEX server ports internally with VIC', 'output')
        self.my_output.print_stream('\t - IOM/FEX upstream ports via fiber to FI', 'output')
        self.my_output.print_stream('- Fabric Interconnect', 'output')
        self.my_output.print_stream('\t - server ports connected to Chassis IOM/FEX', 'output')
        self.my_output.print_stream('\t - upstream port groups connected with network switches', 'output')
        self.my_output.print_stream('\t - per-VLAN group based mapping of upstream connectivity', 'output')

        self.my_output.print_stream('', 'output')
        self.my_output.print_stream(
            '![FabricAccess](./ucsm-blade.png)',
            'output'
        )
