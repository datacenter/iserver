class VpcRoleOutput():
    def __init__(self):
        pass

    def print_vpc_role(self, info, title=False):
        if title:
            self.my_output.default(
                'VPC Role [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nexus_name',
            'vpc-current-role',
            'dual-active-detected',
            'vpc-system-mac',
            'vpc-system-prio',
            'vpc-local-system-mac',
            'vpc-local-system-prio',
            'vpc-local-role-prio',
            'vpc-peer-system-mac',
            'vpc-peer-system-prio',
            'vpc-peer-role-prio'
        ]

        headers = [
            'Device',
            'Role',
            'DAD',
            'System',
            'Prio',
            'Local System',
            'Prio',
            'Role Prio',
            'Peer',
            'Prio',
            'Role Prio'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )
