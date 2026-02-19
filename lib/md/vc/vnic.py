class MdVcVnicOutput():
    def __init__(self):
        pass

    def print_vc_host_vnic(self, host, vnic):
        self.print_page_header('vCenter Host - VMkernel adapter')

        self.my_output.print_stream('## Host', 'output')
        self.my_output.print_stream('- vCenter: %s' % (host['vcenter']), 'output')
        self.my_output.print_stream('- Cluster: %s' % (host['clusterName']), 'output')
        self.my_output.print_stream('- Host: %s' % (host['name']), 'output')

        self.my_output.print_stream('## Properties', 'output')
        self.my_output.print_stream('- Name: %s' % (vnic['device']), 'output')
        self.my_output.print_stream('- Network: %s' % (vnic['portgroup']), 'output')
        self.my_output.print_stream('- VLAN ID: %s' % (vnic['vlan']), 'output')
        if vnic['services'] is None or len(vnic['services']) == 0:
            self.my_output.print_stream('- Enabled services: ---', 'output')
        else:
            self.my_output.print_stream('- Enabled services: %s' % (','.join(vnic['services'])), 'output')

        self.my_output.print_stream('## NIC settings', 'output')
        self.my_output.print_stream('- MAC: %s' % (vnic['mac']), 'output')
        self.my_output.print_stream('- MTU: %s' % (vnic['mtu']), 'output')

        self.my_output.print_stream('## IPv4 settings', 'output')
        self.my_output.print_stream('- IP: %s' % (vnic['cidr']), 'output')
        self.my_output.print_stream('- Gateway: %s' % (vnic['gateway']), 'output')

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(vnic, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(vnic['hash'], subdir='vc/vnic')

    def print_vc_host_vnics(self, host, hosts):
        self.print_vc_host_page_header(
            'VMKernel adapter',
            host,
            hosts
        )

        order = [
            'Device',
            'Network',
            'Switch',
            'IP Address',
            'Enabled Services'
        ]
        self.print_table_header(order)

        for vnic in host['pnet']['vnic']:
            line = ''
            line = self.add_vc_host_link(line, 'vnic', vnic, up=True)
            line = self.add_column(line, vnic['portgroup'])
            line = self.add_column(line, vnic['vswitch'])
            line = self.add_column(
                line,
                '%s/%s' % (
                    vnic['ip'],
                    vnic['prefix']
                )
            )
            if vnic['services'] is None or len(vnic['services']) == 0:
                line = self.add_column(line, '---')
            else:
                line = self.add_column(line, ','.join(vnic['services']))

            self.vc_vnic_count[host['vcenter']][host['name']] += 1
            if vnic['up']:
                self.vc_vnic_up_count[host['vcenter']][host['name']] += 1

            self.my_output.print_stream(line, 'output')

        # self.my_output.print_stream('\n## Debug\n', 'output')
        # self.my_output.print_stream('```', 'output')
        # self.my_output.print_stream(json.dumps(host, indent=4), 'output')
        # self.my_output.print_stream('```', 'output')

        self.save_output(host['hash'], subdir='vc/vnic')

        for vnic in host['pnet']['vnic']:
            self.print_vc_host_vnic(
                host,
                vnic
            )
