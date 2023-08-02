class ProtocolIsisOutput():
    def __init__(self):
        pass

    def print_proto_isis_domains(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ISIS - Domain [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

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

    def print_proto_isis_instances(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ISIS - Instance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        if len(info) == 0:
            return

        order = [
            'instance.pod_node_name',
            'instance.health',
            'instance.faults',
            'instance.adminSt',
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
            'Health',
            'Faults',
            'Admin State',
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
            table=True,
            merge=True
        )

    def print_proto_isis_interfaces(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ISIS - Interface [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
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

    def print_proto_isis_lsps(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ISIS - LSP [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
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

    def print_proto_isis_neighbors(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ISIS - Neighbor [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
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

    def print_proto_isis_routes(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ISIS - Route [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
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

    def print_proto_isis_trees(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ISIS - Tree [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
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

    def print_proto_isis_tunnels(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ISIS - Tunnel [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'domain',
            'id',
            'dest_node',
            'role',
            'type'
        ]

        headers = [
            'Node',
            'Domain',
            'Id',
            'Destination',
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

    def print_proto_isis_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'Protocol ISIS - Faults [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Node',
            'Sev',
            'Code',
            'Cause',
            'Created Time',
            'Lifecycle',
            'Description'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_isis_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Protocol ISIS - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Protocol ISIS - Fault Records last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Node',
            'Sev',
            'Code',
            'Cause',
            'Created Time',
            'Lifecycle',
            'Description'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            underline=True,
            table=True
        )

    def print_proto_isis_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'Protocol ISIS - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'Protocol ISIS - Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod_node_name',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT',
            'affectedT'
        ]

        headers = [
            'Node',
            'Sev',
            'Code',
            'Cause',
            'Created Time',
            'Description',
            'Change Set',
            'Affected'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT', 'changeSetT', 'affectedT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            row_separator=True,
            underline=True,
            table=True
        )
