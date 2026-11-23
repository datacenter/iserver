import json


class MdVcSwitchOutput():
    def __init__(self):
        pass

    def print_vc_host_switch(self, host, switch):
        self.print_page_header('vCenter Host - Standard Switch')

        self.my_output.print_stream('\n## Debug\n', 'output')
        self.my_output.print_stream('```', 'output')
        self.my_output.print_stream(json.dumps(switch, indent=4), 'output')
        self.my_output.print_stream('```', 'output')

        self.save_output(switch['hash'], subdir='vc/switch')

    def print_vc_host_switches(self, host, hosts):
        self.print_vc_host_page_header(
            'Standard Virtual Switch',
            host,
            hosts
        )

        order = [
            'vSwitch',
            'Info'
        ]
        self.print_table_header(order)

        for vswitch in host['pnet']['vswitch']:
            line = ''
            line = self.add_vc_host_link(line, 'switch', vswitch)
            line = self.add_column(
                line,
                '[Link](./%s.md)' % (vswitch['hash'])
            )

            self.vc_switch_count[host['vcenter']][host['name']] += 1
            if vswitch['up']:
                self.vc_switch_up_count[host['vcenter']][host['name']] += 1

            self.my_output.print_stream(line, 'output')

        self.my_output.print_stream('\n## Debug\n', 'output')
        self.my_output.print_stream('```', 'output')
        self.my_output.print_stream(json.dumps(host, indent=4), 'output')
        self.my_output.print_stream('```', 'output')

        self.save_output(host['hash'], subdir='vc/switch')

        for vswitch in host['pnet']['vswitch']:
            self.print_vc_host_switch(
                host,
                vswitch
            )
