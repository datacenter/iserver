class VpcStateOutput():
    def __init__(self):
        pass

    def print_vpc_state_summary(self, info):
        order = [
            'vpc-domain-id',
            'vpc-peer-status',
            'vpc-peer-keepalive-status',
            'vpc-peer-consistency-status',
            'vpc-per-vlan-peer-consistency',
            'vpc-type-2-consistency-status',
            'vpc-role',
            'num-of-vpcs',
            'peer-gateway',
            'dual-active-excluded-vlans',
            'vpc-graceful-consistency-check-status',
            'vpc-auto-recovery-status',
            'vpc-delay-restore-status',
            'vpc-delay-restore-svi-status',
            'vpc-delay-restore-orphan-port-status',
            'operational-l3-peer',
            'virtual-peerlink'
        ]

        headers = [
            'vPC domain id',
            'Peer status',
            'vPC keep-alive status',
            'Configuration consistency status',
            'Per-vlan consistency status',
            'Type-2 consistency status',
            'vPC role',
            'Number of vPCs configured',
            'Peer Gateway',
            'Dual-active excluded VLANs',
            'Graceful Consistency Check',
            'Auto-recovery status',
            'Delay-restore status',
            'Delay-restore SVI status',
            'Delay-restore Orphan-port status',
            'Operational Layer3 Peer-router',
            'Virtual-peerlink mode'
        ]

        self.my_output.dictionary(
            info,
            title='VPC Domain State Summary',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_vpc_state_peer(self, info, title=False):
        if title:
            self.my_output.default(
                'vPC Peer-link status [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'id',
            'ifindex',
            'state',
            'vlan'
        ]

        headers = [
            'ID',
            'Port',
            'State',
            'VLAN'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['vlan']
            ),
            order=order,
            headers=headers,
            underline=True,
            table=True,
            allow_order_subkeys=True,
            row_separator=True
        )

    def print_vpc_state_vpc(self, info, title=False):
        if title:
            self.my_output.default(
                'vPC Status [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'id',
            'ifindex',
            'state',
            'consistency',
            'vlan'
        ]

        headers = [
            'ID',
            'Port',
            'Status',
            'Consistency',
            'Active VLAN'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['vlan']
            ),
            order=order,
            headers=headers,
            underline=True,
            table=True,
            allow_order_subkeys=True,
            row_separator=True
        )

    def print_vpc_state(self, info, title=False):
        for item in info:
            self.print_vpc_state_summary(item)
            self.print_vpc_state_peer(item['peer'], title=title)
            self.print_vpc_state_vpc(item['vpc'], title=title)
