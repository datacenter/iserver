class LinuxBondOutput():
    def __init__(self):
        pass

    def print_linux_bond(self, info, title=False):
        if title:
            self.my_output.default(
                'Bond',
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'server',
            'name',
            'mii_status',
            'mii_polling_ms',
            'transmit_hash_policy',
            'up_delay_ms',
            'down_delay_ms',
            'lacp_active',
            'lacp_rate',
            'member.name'
        ]

        headers = [
            'Linux',
            'Bond',
            'Status',
            'Polling [ms]',
            'Hash',
            'Up delay [ms]',
            'Down delay [ms]',
            'LACP Active',
            'LACP Rate',
            'Member'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['member']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )

    def print_linux_bond_member(self, info, title=False):
        if title:
            self.my_output.default(
                'Bond - Member',
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'server',
            'name',
            'mii_status',
            'member.name',
            'member.mii_status',
            'member.speed',
            'member.duplex',
            'member.mac'
        ]

        headers = [
            'Linux',
            'Bond',
            'Status',
            'Member',
            'Status',
            'Speed',
            'Duplex',
            'MAC'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['member']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )

    def print_linux_bond_aci(self, info, title=False):
        if title:
            self.my_output.default(
                'Bond - ACI',
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'server',
            'interface',
            'pod_node_name',
            'id',
            'key',
            'adjacency.sysId',
            'adjacency.sysPrio',
            'adjacency.key',
            'adjacency.port',
            'adjacency.portPrio'
        ]

        headers = [
            'Linux',
            'Interface',
            'ACI Node',
            'Member',
            'Oper Key',
            'Nbr System MAC',
            'Nbr System Prio',
            'Nbr Oper Key',
            'Nbr Port',
            'Nbr Port Prio'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True,
            merge=True
        )

    def print_linux_bond_nexus(self, info, title=False):
        if title:
            self.my_output.default(
                'Bond - Nexus',
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'server',
            'interface',
            'nexus_name',
            'interface',
            'port.port',
            'port.partner_mac'
        ]

        headers = [
            'Linux',
            'Interface',
            'Nexus',
            'Interface',
            'Port',
            'Partner'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['port']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True,
            merge=True
        )
