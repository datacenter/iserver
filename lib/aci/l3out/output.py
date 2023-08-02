class L3OutOutput():
    def __init__(self):
        pass

    def print_l3outs_bgp(self, info, title=False):
        if title:
            self.my_output.default(
                'L3Out - BGP [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'faults',
            'nameTenant',
            'mplsEnabledTick',
            'bgpExtP.enabledTick',
            'l3extRsEctx.tenant_name',
            'nodes.nodeDn',
            'nodes.rtrId'
        ]

        headers = [
            'Faults',
            'L3Out',
            'MPLS',
            'BGP',
            'VRF Name',
            'Border Leaf',
            'Router ID'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['nodes']
            ),
            order=order,
            headers=headers,
            underline=True,
            allow_order_subkeys=True,
            row_separator=True,
            merge=True,
            remove_empty_columns=True,
            table=True
        )

    def print_l3outs_eigrp(self, info, title=False):
        if title:
            self.my_output.default(
                'L3Out - EIGRP [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'faults',
            'nameTenant',
            'eigrpExtP.enabledTick',
            'l3extRsEctx.nameTenant',
            'nodes.nodeDn',
            'nodes.rtrId'
        ]

        headers = [
            'Faults',
            'L3Out',
            'EIGRP',
            'VRF',
            'Border Leaf',
            'Router ID'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['nodes']
            ),
            order=order,
            headers=headers,
            underline=True,
            allow_order_subkeys=True,
            row_separator=True,
            merge=True,
            remove_empty_columns=True,
            table=True
        )

    def print_l3outs_ospf(self, info, title=False):
        if title:
            self.my_output.default(
                'L3Out - OSPF [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'faults',
            'nameTenant',
            'targetDscp',
            'ospfExtP.enabledTick',
            'ospfExtP.areaId',
            'ospfExtP.areaType',
            'ospfExtP.areaCost',
            'ospfExtP.redistributeTick',
            'ospfExtP.summaryTick',
            'ospfExtP.suppressTick',
            'nodes.nodeDn',
            'nodes.rtrId'
        ]

        headers = [
            'Faults',
            'L3Out',
            'Target DSCP',
            'OSPF',
            'Area ID',
            'Area Type',
            'Area Cost',
            'Redistribute LSA into NSSA',
            'Originate Summary LSA',
            'Suppress translated LSA',
            'Border Leaf',
            'Router ID'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['nodes']
            ),
            order=order,
            headers=headers,
            underline=True,
            allow_order_subkeys=True,
            row_separator=True,
            merge=True,
            remove_empty_columns=True,
            table=True
        )

    def print_l3outs_mpls(self, info, title=False):
        if title:
            self.my_output.default(
                'L3Out - MPLS [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'faults',
            'nameTenant',
            'mplsEnabledTick',
            'bgpExtP.enabledTick',
            'l3extRsEctx.nameTenant',
            'nodes.nodeDn',
            'nodes.rtrId'
        ]

        headers = [
            'Faults',
            'L3Out',
            'Tenant',
            'PIM',
            'BGP',
            'VRF',
            'Border Leaf',
            'Router ID'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['nodes']
            ),
            order=order,
            headers=headers,
            underline=True,
            allow_order_subkeys=True,
            row_separator=True,
            merge=True,
            remove_empty_columns=True,
            table=True
        )

    def print_l3outs_pim(self, info, title=False):
        if title:
            self.my_output.default(
                'L3Out - PIM [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'faults',
            'nameTenant',
            'pimExtP.enabledTick',
            'l3extRsEctx.nameTenant',
            'nodes.nodeDn',
            'nodes.rtrId'
        ]

        headers = [
            'Faults',
            'L3Out',
            'Tenant',
            'PIM',
            'VRF',
            'Border Leaf',
            'Router ID'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['nodes']
            ),
            order=order,
            headers=headers,
            underline=True,
            allow_order_subkeys=True,
            row_separator=True,
            merge=True,
            remove_empty_columns=True,
            table=True
        )

    def print_l3outs_epg(self, info, title=False):
        if title:
            self.my_output.default(
                'L3Out - EPG [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'faults',
            'nameTenant',
            'l3extRsEctx.nameTenant',
            'l3extRsL3DomAtt.name',
            'l3extInstP.name'
        ]

        headers = [
            'Faults',
            'L3Out Name',
            'VRF',
            'L3 Domain',
            'External EPG'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['l3extInstP']
            ),
            order=order,
            headers=headers,
            underline=True,
            allow_order_subkeys=True,
            row_separator=True,
            merge=True,
            remove_empty_columns=True,
            table=True
        )

    def print_l3outs_node(self, info, title=False):
        if title:
            self.my_output.default(
                'L3Out - Node [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'faults',
            'nameTenant',
            'mplsEnabledTick',
            'pimExtP.enabledTick',
            'bgpExtP.enabledTick',
            'ospfExtP.enabledTick',
            'eigrpExtP.enabledTick',
            'nodes.nodeDn',
            'nodes.rtrId',
            'nodes.rtrIdLoopBack'
        ]

        headers = [
            'Faults',
            'L3Out',
            'MPLS',
            'PIM',
            'BGP',
            'OSPF',
            'EIGRP',
            'Border Leaf',
            'Router ID',
            'Loopback'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['nodes']
            ),
            order=order,
            headers=headers,
            underline=True,
            allow_order_subkeys=True,
            row_separator=True,
            merge=True,
            remove_empty_columns=True,
            table=True
        )

    def print_l3outs(self, info, title=False):
        if title:
            self.my_output.default(
                'L3Out [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'faults',
            'nameTenant',
            'mplsEnabledTick',
            'pimExtP.enabledTick',
            'bgpExtP.enabledTick',
            'ospfExtP.enabledTick',
            'eigrpExtP.enabledTick',
            'l3extRsEctx.nameTenant',
            'l3extRsL3DomAtt.name'
        ]

        headers = [
            'Faults',
            'L3Out',
            'MPLS',
            'PIM',
            'BGP',
            'OSPF',
            'EIGRP',
            'VRF',
            'L3 Domain'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['nodes', 'l3extInstP']
            ),
            order=order,
            headers=headers,
            underline=True,
            allow_order_subkeys=True,
            row_separator=True,
            merge=True,
            remove_empty_columns=True,
            table=True
        )

        # if verbose:
        #     for l3out in l3outs:
        #         for node_profile in l3out['nodeProfiles']:
        #             self.print_l3out_node_profile(node_profile)

    def print_l3out_node_profile(self, info, title=False):
        if title:
            self.my_output.default(
                'L3Out - Node Profile [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'dn',
            'descr',
            'targetDscp'
        ]

        headers = [
            'Dn',
            'Description',
            'Target DSCP'
        ]

        self.my_output.dictionary(
            info,
            title='Logical Node Profile: %s' % (info['name']),
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_l3outs_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'L3Out - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'L3Out - Event Logs last %s [#%s]' % (when, len(info)),
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
            'L3Out',
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

    def print_l3outs_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'L3Out - Faults [#%s]' % (len(info)),
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
            'L3Out',
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

    def print_l3outs_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'L3Out - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'L3Out - Fault Records last %s [#%s]' % (when, len(info)),
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
            'L3Out',
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

    def print_l3outs_audit_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'L3Out - Audit Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'L3Out - Audit Logs last %s [#%s]' % (when, len(info)),
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
            'L3Out',
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
