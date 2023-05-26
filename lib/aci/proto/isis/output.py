class ProtocolIsisOutput():
    def __init__(self):
        pass

    def print_proto_isis(self, info):
        self.print_proto_isis_instance(
            info['instance']
        )

        for domain_info in info['domain']:
            self.print_proto_isis_domain(
                domain_info
            )

            if 'interface' in domain_info:
                self.my_output.default(
                    'Interfaces',
                    underline=True,
                    before_newline=True
                )
                self.print_proto_isis_interfaces(
                    domain_info['interface']
                )

            if 'lsp' in domain_info:
                self.my_output.default(
                    'LSP Records',
                    underline=True,
                    before_newline=True
                )
                self.print_proto_isis_lsps(
                    domain_info['lsp']
                )

            if 'neighbor' in domain_info:
                self.my_output.default(
                    'Neighbors',
                    underline=True,
                    before_newline=True
                )
                self.print_proto_isis_neighbors(
                    domain_info['neighbor']
                )

            if 'route' in domain_info:
                self.my_output.default(
                    'IS-IS Routes',
                    underline=True,
                    before_newline=True
                )
                self.print_proto_isis_routes(
                    domain_info['route']
                )

            if 'tree' in domain_info:
                self.my_output.default(
                    'IS-IS Fabric Multicast Trees',
                    underline=True,
                    before_newline=True
                )
                self.print_proto_isis_trees(
                    domain_info['tree']
                )

            if 'tunnel' in domain_info:
                self.my_output.default(
                    'Discovered Tunnel Endpoints',
                    underline=True,
                    before_newline=True
                )
                self.print_proto_isis_tunnels(
                    domain_info['tunnel']
                )

    def print_proto_isis_domains(self, info):
        order = [
            'name',
            'operSt',
            'sysId',
            'areaId',
            'nSel',
            'mode',
            'maxEcmp',
            'metricStyle',
            'mtu'
        ]

        headers = [
            'Domain',
            'Oper State',
            'System ID',
            'Area',
            'Protocol',
            'Mode',
            'Max ECMP',
            'Metric Style',
            'MTU'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_isis_domain(self, info):
        order = [
            'name',
            'operSt',
            'sysId',
            'areaId',
            'nSel',
            'mode',
            'maxEcmp',
            'metricStyle',
            'mtu'
        ]

        headers = [
            'Name',
            'Oper State',
            'System ID',
            'Area',
            'Protocol',
            'Mode',
            'Max ECMP',
            'Metric Style',
            'MTU'
        ]

        self.my_output.dictionary(
            info,
            title='Domain',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_proto_isis_instances(self, info):
        if len(info) == 0:
            return

        order = [
            'instance.pod_node_name',
            'instance.adminSt',
            'instance.operSt',
            'domain.name',
            'domain.operSt',
            'domain.sysId',
            'domain.areaId',
            'domain.nSel',
            'domain.mode',
            'domain.maxEcmp',
            'domain.metricStyle',
            'domain.mtu'
        ]

        headers = [
            'Node',
            'Admin State',
            'Oper State',
            'Domain Name',
            'Oper State',
            'System ID',
            'Area',
            'Protocol',
            'Mode',
            'Max ECMP',
            'Metric Style',
            'MTU'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['domain']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_isis_instance(self, info):
        order = [
            'pod_node_name',
            'adminSt',
            'operSt',
            'domainCount'
        ]

        headers = [
            'Node',
            'Admin State',
            'Oper State',
            'Domains'
        ]

        self.my_output.dictionary(
            info,
            title='IS-IS Instance',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_proto_isis_interfaces(self, info):
        if len(info) == 0:
            return

        order = [
            'pod_node_name',
            'domain',
            'id',
            'adminSt',
            'cktT',
            'ctrl',
            'iibState'
        ]

        headers = [
            'Node',
            'Domain',
            'Id',
            'Admin State',
            'Circuit Type',
            'Control',
            'Protocol State'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_isis_lsps(self, info):
        if len(info) == 0:
            return

        order = [
            'pod_node_name',
            'domain',
            'sysId',
            'lanId',
            'frag',
            'type',
            'timerExpiryTS',
            'seqNum'
        ]

        headers = [
            'Node',
            'Domain',
            'Sys Id',
            'Lan Id',
            'Frag',
            'Type',
            'Lifetime',
            'Seqnum'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_isis_neighbors(self, info):
        if len(info) == 0:
            return

        order = [
            'pod_node_name',
            'domain',
            'interface',
            'sysId',
            'type',
            'cktType',
            'isisPeerIpAddr.addr',
            'operSt'
        ]

        headers = [
            'Node',
            'Domain',
            'Interface',
            'System Id',
            'Level',
            'Circuit Type',
            'Peer IP',
            'State'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_isis_routes(self, info):
        if len(info) == 0:
            return

        order = [
            'pod_node_name',
            'domain',
            'pfx',
            'metric',
            'pref',
            'isisNexthop.interface',
            'isisNexthop.address'
        ]

        headers = [
            'Node',
            'Domain',
            'Prefix',
            'Metric',
            'Preference',
            'NH Interface',
            'NH Address'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['isisNexthop']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_isis_trees(self, info):
        if len(info) == 0:
            return

        order = [
            'pod_node_name',
            'domain',
            'id',
            'root',
            'rootPort',
            'diameter',
            'origin',
            'diaAlert',
            'operSt'
        ]

        headers = [
            'Node',
            'Domain',
            'Id',
            'Root Address',
            'Root Port',
            'Diameter',
            'Origin',
            'Diameter Alert',
            'Oper State'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_isis_tunnels(self, info):
        if len(info) == 0:
            return

        order = [
            'pod_node_name',
            'domain',
            'id',
            'role',
            'type'
        ]

        headers = [
            'Node',
            'Domain',
            'Id',
            'Role',
            'Type'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )
