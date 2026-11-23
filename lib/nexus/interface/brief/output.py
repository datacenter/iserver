class InterfaceBriefOutput():
    def __init__(self):
        pass

    def print_interfaces_mgmt_brief(self, info, title=False):
        interfaces = []

        for item in info:
            if item['type'] == 'mgmt':
                interfaces.append(
                    item
                )

        if len(interfaces) == 0:
            return

        if title:
            self.my_output.default(
                'Management Interface [#%s]' % (len(interfaces)),
                underline=True,
                before_newline=True
            )

        order = [
            'nexus_name',
            'interface',
            'state',
            'ip_addr',
            'speed',
            'mtu'
        ]

        headers = [
            'Device',
            'Management Interface',
            'State',
            'IP Address',
            'Speed',
            'MTU'
        ]

        self.my_output.my_table(
            interfaces,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_interfaces_eth_brief(self, info, title=False):
        interfaces = []

        for item in info:
            if item['type'] == 'eth':
                interfaces.append(
                    item
                )

        if len(interfaces) == 0:
            return

        if title:
            self.my_output.default(
                'Ethernet Interface [#%s]' % (len(interfaces)),
                underline=True,
                before_newline=True
            )

        order = [
            'nexus_name',
            'interface',
            'vlan',
            'portmode',
            'state',
            'state_rsn_desc',
            'speed',
            'ratemode',
            'portchan'
        ]

        headers = [
            'Device',
            'Eth Interface',
            'VLAN',
            'Mode',
            'State',
            'Reason',
            'Speed',
            'Rate',
            'Port Channel'
        ]

        self.my_output.my_table(
            interfaces,
            order=order,
            cast_none=True,
            headers=headers,
            underline=True,
            table=True
        )

    def print_interfaces_pc_brief(self, info, title=False):
        interfaces = []

        for item in info:
            if item['type'] == 'pc':
                interfaces.append(
                    item
                )

        if len(interfaces) == 0:
            return

        if title:
            self.my_output.default(
                'Port Channel Interface [#%s]' % (len(interfaces)),
                underline=True,
                before_newline=True
            )

        order = [
            'nexus_name',
            'interface',
            'vlan',
            'portmode',
            'state',
            'state_rsn_desc',
            'speed',
            'ratemode',
            'proto'
        ]

        headers = [
            'Device',
            'PC Interface',
            'VLAN',
            'Mode',
            'State',
            'Reason',
            'Speed',
            'Rate',
            'Protocol'
        ]

        self.my_output.my_table(
            interfaces,
            order=order,
            cast_none=True,
            headers=headers,
            underline=True,
            table=True
        )

    def print_interfaces_vlan_brief(self, info, title=False):
        interfaces = []

        for item in info:
            if item['type'] == 'vlan':
                interfaces.append(
                    item
                )

        if len(interfaces) == 0:
            return

        if title:
            self.my_output.default(
                'VLAN Interface [#%s]' % (len(interfaces)),
                underline=True,
                before_newline=True
            )

        order = [
            'nexus_name',
            'interface',
            'svi_admin_state',
            'svi_rsn_desc'
        ]

        headers = [
            'Device',
            'VLAN Interface',
            'State',
            'Reason'
        ]

        self.my_output.my_table(
            interfaces,
            order=order,
            cast_none=True,
            headers=headers,
            underline=True,
            table=True
        )

    def print_interfaces_brief(self, info, title=False):
        self.print_interfaces_mgmt_brief(info, title=title)
        self.print_interfaces_eth_brief(info, title=title)
        self.print_interfaces_pc_brief(info, title=title)
        self.print_interfaces_vlan_brief(info, title=title)
