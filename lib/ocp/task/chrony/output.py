class OcpTaskChronyOutput():
    def __init__(self):
        pass

    def print_ocp_chrony_config(self, info, title=False):
        if title:
            self.my_output.default(
                'Chrony Configuration',
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        equal = True
        if len(info) > 1:
            reference = '\n'.join(info[0]['config'])
            for item in info:
                if '\n'.join(item['config']) != reference:
                    equal = False

        if equal:
            self.my_output.default('Configuration the same on all nodes', before_newline=True, after_newline=True)
            for line in info[0]['config']:
                self.my_output.default(line)

        if not equal:
            for item in info:
                self.my_output.default('Node %s [%s]' % (item['name'], item['ip']), after_newline=True)
                for line in item['config']:
                    self.my_output.default(line)

    def print_ocp_chrony_state(self, info):
        order = [
            'name',
            'status',
            'reference',
            'stratum',
            'time',
            'root_delay'
        ]

        headers = [
            'Node',
            'Status',
            'Reference',
            'Stratum',
            'Time',
            'Delay'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_ocp_chrony_mc(self, info, title=False):
        if title:
            self.my_output.default(
                'Chrony Machine Configuration',
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            self.my_output.default('Machine config: %s' % (item['name']), before_newline=True)
            self.my_output.default('Node: %s' % (', '.join(item['node'])))
            for file_info in item['file']:
                self.my_output.default('Path: %s' % (file_info['path']))
                self.my_output.default(file_info['content'])

    def print_ocp_chrony_info(self, info):
        if 'config' in info:
            self.print_ocp_chrony_config(info['config'], title=True)

        if 'state' in info:
            self.print_ocp_chrony_state(info['state'])

        if 'mc' in info:
            self.print_ocp_chrony_mc(info['mc'], title=True)
