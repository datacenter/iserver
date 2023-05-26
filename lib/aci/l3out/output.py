class L3OutOutput():
    def __init__(self):
        pass

    def print_l3outs_bgp(self, l3outs):
        if len(l3outs) == 0:
            self.my_output.default('No L3Out found')
            return

        order = [
            'nameTenant',
            'mplsEnabledTick',
            'bgpExtP.enabledTick',
            'l3extRsEctx.tenant_name',
            'nodes.nodeDn',
            'nodes.rtrId'
        ]

        headers = [
            'L3Out',
            'MPLS',
            'BGP',
            'VRF Name',
            'Border Leaf',
            'Router ID'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                l3outs,
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

    def print_l3outs_eigrp(self, l3outs):
        if len(l3outs) == 0:
            self.my_output.default('No L3Out found')
            return

        order = [
            'nameTenant',
            'eigrpExtP.enabledTick',
            'l3extRsEctx.nameTenant',
            'nodes.nodeDn',
            'nodes.rtrId'
        ]

        headers = [
            'L3Out',
            'EIGRP',
            'VRF',
            'Border Leaf',
            'Router ID'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                l3outs,
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

    def print_l3outs_ospf(self, l3outs):
        if len(l3outs) == 0:
            self.my_output.default('No L3Out found')
            return

        order = [
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
                l3outs,
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

    def print_l3outs_mpls(self, l3outs):
        if len(l3outs) == 0:
            self.my_output.default('No L3Out found')
            return

        order = [
            'nameTenant',
            'mplsEnabledTick',
            'bgpExtP.enabledTick',
            'l3extRsEctx.nameTenant',
            'nodes.nodeDn',
            'nodes.rtrId'
        ]

        headers = [
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
                l3outs,
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

    def print_l3outs_pim(self, l3outs):
        if len(l3outs) == 0:
            self.my_output.default('No L3Out found')
            return

        order = [
            'nameTenant',
            'pimExtP.enabledTick',
            'l3extRsEctx.nameTenant',
            'nodes.nodeDn',
            'nodes.rtrId'
        ]

        headers = [
            'L3Out',
            'Tenant',
            'PIM',
            'VRF',
            'Border Leaf',
            'Router ID'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                l3outs,
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

    def print_l3outs_epg(self, l3outs):
        if len(l3outs) == 0:
            self.my_output.default('No L3Out found')
            return

        order = [
            'nameTenant',
            'l3extRsEctx.nameTenant',
            'l3extRsL3DomAtt.name',
            'l3extInstP.name'
        ]

        headers = [
            'L3Out Name',
            'VRF',
            'L3 Domain',
            'External EPG'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                l3outs,
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

    def print_l3outs_node(self, l3outs):
        if len(l3outs) == 0:
            self.my_output.default('No L3Out found')
            return

        order = [
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
                l3outs,
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

    def print_l3outs(self, l3outs):
        if len(l3outs) == 0:
            self.my_output.default('No L3Out found')
            return

        order = [
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
                l3outs,
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

    def print_l3out_node_profile(self, info):
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
