class VrfOutput():
    def __init__(self):
        pass

    def print_vrf_properties(self, info):
        order = [
            'health',
            'faults',
            'name',
            'tenant',
            'ipDataPlaneLearningTick',
            'knwMcastActTick',
            'pcEnfDir',
            'pcEnfPref',
            'bdEnforcedEnableTick',
            'pcTag',
            'seg'
        ]

        headers = [
            'Health',
            'Faults',
            'Name',
            'Tenant',
            'Data Plane Learning',
            'Multicast',
            'Policy Control Enforcement Direction',
            'Policy Control Enforcement Preference',
            'Bridge Domain Enforcement Status',
            'Class ID',
            'VNID'
        ]

        if 'endpointCount' in info:
            order.append('endpointCount')
            headers.append('Endpoints')

        self.my_output.dictionary(
            info,
            title='VRF Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_vrf_v4_route(self, info, title=False):
        if title:
            self.my_output.default(
                'VRF %s - IPv4 Routes [#%s]' % (info['nameTenant'], len(info['v4route'])),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'pod',
            'node',
            'prefix',
            'addr',
            'vrf',
            'routeType',
            'types',
            'pref',
            'owner'
        ]

        headers = [
            'Pod',
            'Node',
            'Prefix',
            'Next Hop',
            'Next Hop VRF',
            'Type',
            'Details',
            'Preference',
            'Source'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info['v4route'],
                order,
                ['types']
            ),
            order=order,
            headers=headers,
            underline=True,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )

    def print_vrf(self, info):
        self.print_vrf_properties(
            info
        )

        if 'fvAEPg' in info and len(info['fvAEPg']) > 0:
            self.my_output.default(
                'Associated EPGs',
                underline=True
            )
            self.print_epgs(
                info['fvAEPg']
            )

        if 'fvBD' in info and len(info['fvBD']) > 0:
            self.my_output.default(
                'Associated Bridge Domains',
                underline=True,
                before_newline=True
            )
            self.print_bridge_domains(
                info['fvBD']
            )

        if 'l3out' in info and len(info['l3out']) > 0:
            self.my_output.default(
                'Associated L3 Outs',
                underline=True,
                before_newline=True
            )
            self.print_l3outs(
                info['l3out']
            )

        if 'v4route' in info and len(info['v4route']) > 0:
            self.my_output.default(
                'Route Table (IPv4)',
                underline=True,
                before_newline=True
            )
            self.print_vrf_v4_route(
                info
            )

    def print_vrfs(self, info, title=False):
        if title:
            self.my_output.default(
                'VRF [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'health',
            'faults',
            'nameTenant',
            'pcTag',
            'seg',
            'pcEnfPref',
            'pcEnfDir',
            'fvAEPg.nameApTenant',
            'fvBD.nameTenant',
            'fvSubnet.ip',
            'l3out.nameTenant'
        ]

        headers = [
            'Health',
            'Faults',
            'VRF',
            'Class ID',
            'VNID',
            'PCE Preference',
            'PCE Direction',
            'Associated EPG',
            'Associated BD',
            'BD Subnets',
            'Associated L3Out'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['fvBD', 'fvSubnet', 'l3out', 'fvAEPg']
            ),
            order=order,
            headers=headers,
            underline=True,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )

    def print_vrfs_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'VRF - Properties [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nameTenant',
            'ipDataPlaneLearningTick',
            'knwMcastAct',
            'pcEnfPref',
            'pcEnfDir',
            'bdEnforcedEnableTick',
            'pcTag',
            'seg'
        ]

        headers = [
            'VRF',
            'DP Learning',
            'Mcast',
            'PCE Preference',
            'PCE Direction',
            'BD Enforced',
            'Class ID',
            'VNID'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            underline=True,
            allow_order_subkeys=True,
            row_separator=True,
            table=True
        )

    def print_vrfs_node(self, info, title=False):
        if title:
            self.my_output.default(
                'VRF - Nodes [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'health',
            'faults',
            'nameTenant',
            'node.name',
            'node.interfaces'
        ]

        headers = [
            'Health',
            'Faults',
            'VRF',
            'Node',
            'Interfaces'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['node']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_vrfs_interface(self, info, title=False):
        if title:
            self.my_output.default(
                'VRF - Interfaces [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'health',
            'faults',
            'nameTenant',
            'interface.node_name',
            'interface.intf_name'
        ]

        headers = [
            'Health',
            'Faults',
            'VRF',
            'Node',
            'Interface'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['interface']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_vrfs_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'VRF - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'VRF - Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nameTenant',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'VRF',
            'Sev',
            'Code',
            'Cause',
            'Created Time',
            'Description',
            'Change Set'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT', 'changeSetT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            row_separator=True,
            underline=True,
            table=True
        )

    def print_vrfs_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'VRF - Faults [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nameTenant',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'VRF',
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

    def print_vrfs_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'VRF - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'VRF - Fault Records last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nameTenant',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'VRF',
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

    def print_vrfs_audit_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'VRF - Audit Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'VRF - Audit Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nameTenant',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'VRF',
            'Sev',
            'Code',
            'Cause',
            'Created Time',
            'Description',
            'Change Set'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['descrT', 'changeSetT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=True,
            row_separator=True,
            underline=True,
            table=True
        )
