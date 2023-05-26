class InterfaceVirtualPortChannelOutput():
    def __init__(self):
        pass

    def print_interfaces_virtual_port_channel_state(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'id',
            'operRole',
            'operSt',
            'peerSt',
            'peerStQual',
            'compatSt',
            'compatQualStr',
            'localMemberSummary',
            'peerMemberSummary'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'VPC Domain Id',
            'Oper Role',
            'Oper State',
            'Peer State',
            'Reason',
            'Constistency',
            'Reason',
            'Local Members',
            'Remote Members'
        ]

        self.my_output.my_table(
            interfaces,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_interfaces_virtual_port_channel_address(self, interfaces):
        if len(interfaces) == 0:
            self.my_output.default(
                'No interface'
            )
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'pod_node_name',
            'id',
            'operRole',
            'operSt',
            'peerSt',
            'virtualIp',
            'vpcMAC',
            'localMAC',
            'localPrio',
            'peerIp',
            'peerMAC',
            'peerPrio'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'Node',
            'VPC Domain Id',
            'Oper Role',
            'Oper State',
            'Peer State',
            'VPC IP',
            'VPC MAC',
            'Local MAC',
            'Local Prio',
            'Peer IP',
            'Peer MAC',
            'Peer Prio'
        ]

        self.my_output.my_table(
            interfaces,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_interface_virtual_port_channel_info(self, interface):
        order = [
            'apic',
            'pod_node_name',
            'id',
            'operRole',
            'operSt',
            'localMAC',
            'localPrio',
            'peerSt',
            'peerStQual',
            'peerIp',
            'peerMAC',
            'peerPrio',
            'peerVersion',
            'compatSt',
            'compatQualStr',
            'vpcPrio',
            'vpcMAC',
            'virtualIp',
            'localMemberSummary',
            'peerMemberSummary'
        ]

        headers = [
            'Apic',
            'Node',
            'VPC Domain Id',
            'Oper Role',
            'Oper State',
            'Local MAC',
            'Local Priority',
            'Peer State',
            'Reason',
            'Peer IP',
            'Peer MAC',
            'Peer Priority',
            'Peer Version',
            'Configuration Constistency',
            'Reason',
            'VPC Priority',
            'VPC MAC',
            'Virtual IP',
            'Local Members',
            'Peer Members'
        ]

        self.my_output.dictionary(
            interface,
            title='Interface Virtual Port Channel',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_interface_virtual_port_channel_members(self, members):
        order = [
            'id',
            'name',
            'pcMode',
            'localOperSt',
            'remoteOperSt'
        ]

        headers = [
            'ID',
            'Name',
            'PC Mode',
            'Local State',
            'Remote State'
        ]

        self.my_output.my_table(
            members,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_interface_virtual_port_channel(self, interface):
        self.print_interface_virtual_port_channel_info(interface)
        self.print_interface_virtual_port_channel_members(interface['members'])
