class VpcKeepaliveOutput():
    def __init__(self):
        pass

    def print_vpc_keepalive_status(self, info, title=False):
        if title:
            self.my_output.default(
                'VPC Keepalive - Status [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nexus_name',
            'vpc-peer-keepalive-status',
            'vpc-peer-keepalive-up-time',
            'vpc-keepalive-send-interface',
            'vpc-keepalive-send-status',
            'vpc-keepalive-receive-interface',
            'vpc-keepalive-receive-status'
        ]

        headers = [
            'Device',
            'Status',
            'Up Time',
            'Interface TX',
            'Status TX',
            'Interface RX',
            'Status RX'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_vpc_keepalive_parameters(self, info, title=False):
        if title:
            self.my_output.default(
                'VPC Keepalive - Parameters [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nexus_name',
            'vpc-keepalive-dest',
            'vpc-keepalive-interval',
            'vpc-keepalive-timeout',
            'vpc-keepalive-hold-timeout',
            'vpc-keepalive-vrf',
            'vpc-keepalive-udp-port',
            'vpc-keepalive-tos'
        ]

        headers = [
            'Device',
            'Destination',
            'Interval [msec]',
            'Timeout [sec]',
            'Hold Timeout [sec]',
            'VRF',
            'UDP Port',
            'ToS'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_vpc_keepalive(self, info, title=False):
        self.print_vpc_keepalive_status(info, title=title)
        self.print_vpc_keepalive_parameters(info, title=title)
