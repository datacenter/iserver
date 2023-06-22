class BridgeDomainOutput():
    def __init__(self):
        pass

    def print_bridge_domain_properties(self, info):
        order = [
            'tenant',
            'name',
            'dn',
            'descr',
            'health.score',
            'type',
            'fvSubnetCount',
            'fvRsCtx.nameTenant',
            'l3OutCount',
            'endpointCount',
            'epgCount'
        ]

        headers = [
            'Tenant',
            'Name',
            'Dn',
            'Description',
            'Health Score',
            'Type',
            'Subnet Count',
            'VRF',
            'L3Out',
            'Endpoint',
            'EPG'
        ]

        self.my_output.dictionary(
            info,
            title='Bridge Domain Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_bridge_domain_l2_properties(self, info):
        order = [
            'unkMacUcastActT',
            'bcastP',
            'multiDstPktActT',
            'epClearTick',
            'intersiteL2StretchTick'
        ]

        headers = [
            'L2 Unknown Unicast',
            'Multicast Address (GIPo)',
            'Multi Destination Flooding',
            'Clear Remote MAC Entries',
            'Scaled L2 Only Mode'
        ]

        self.my_output.dictionary(
            info,
            title='L2 Forwarding Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_bridge_domain_mcast_properties(self, info):
        order = [
            'fvRsIgmpsn.nameTenant',
            'fvRsMldsn.nameTenant',
            'mcastAllowTick',
            'unkMcastActT',
            'ipv6McastAllowTick',
            'v6unkMcastActT'
        ]

        headers = [
            'IGMP Snooping Policy',
            'MLD Snooping Policy',
            'IPv4 Multicast',
            'IPv4 L3 Unknown Multicast Flooding',
            'IPv6 Multicast',
            'IPv6 L3 Unknown Multicast'
        ]

        self.my_output.dictionary(
            info,
            title='Multicast Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_bridge_domain_l3_properties(self, info):
        order = [
            'unicastRouteTick',
            'mac',
            'vmacT',
            'ipLearningTick',
            'hostBasedRoutingTick',
            'limitIpLearnToSubnetsTick',
            'arpFloodTick',
            'epMoveDetectModeT'
        ]

        headers = [
            'Unicast Routing',
            'BD MAC Address',
            'Virtual MAC Address',
            'IP Learning',
            'Advertise Host Routes',
            'Limit Local IP Learning to BD/EPG Subnets',
            'ARP Flooding',
            'EP Move Detection Mode'
        ]

        self.my_output.dictionary(
            info,
            title='L3 Forwarding Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_bridge_domain_subnets(self, info):
        order = [
            'network',
            'gateway',
            'preferredTick',
            'virtualTick',
            'scope',
            'ipDPLearningTick',
            'usage',
            'available'
        ]

        headers = [
            'Network',
            'Gateway',
            'Preferred',
            'Virtual',
            'Scope',
            'IP Data Plane Learning',
            'IP Usage',
            'IP Available'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            remove_empty_columns=False,
            underline=True,
            table=True
        )

    def print_bridge_domain_epgs(self, info):
        self.my_output.default(
            'Endpoint Groups',
            underline=True,
            before_newline=True
        )

        order = [
            'adminUpTick',
            'nameApTenant',
            'endpointCount',
            'contractCount'
        ]

        headers = [
            'Up',
            'EPG',
            'Endpoints',
            'Contract'
        ]

        self.my_output.my_table(
            info['fvAEPg'],
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_bridge_domain_endpoints(self, info):
        self.my_output.default(
            'Bridge Domain Endpoints',
            underline=True
        )

        self.print_endpoints(
            info['fvCEp']
        )

        vmm_endpoints = []
        for endpoint_info in info['fvCEp']:
            if 'fvRsToVm' in endpoint_info and endpoint_info['fvRsToVm'] is not None:
                vmm_endpoints.append(
                    endpoint_info
                )

        if len(vmm_endpoints) > 0:
            self.my_output.default(
                'Bridge Domain Endpoints with VMM information',
                underline=True,
                before_newline=True
            )
            self.print_endpoints_vmm(
                vmm_endpoints
            )

    def print_bridge_domain(self, info):
        self.print_bridge_domain_properties(
            info
        )

        self.print_bridge_domain_l2_properties(
            info
        )

        self.print_bridge_domain_mcast_properties(
            info
        )

        self.print_policy_snoop_igmp(
            info['fvRsIgmpsn']['policy']
        )

        self.print_policy_snoop_mld(
            info['fvRsMldsn']['policy']
        )

        self.print_bridge_domain_l3_properties(
            info
        )

        if len(info['fvSubnet']) > 0:
            self.print_bridge_domain_subnets(
                info['fvSubnet']
            )

        if len(info['fvAEPg']) > 0:
            self.print_bridge_domain_epgs(
                info
            )

        self.print_vrf_properties(
            info['fvCtx']
        )

        if len(info['fvCEp']) > 0:
            self.print_bridge_domain_endpoints(
                info
            )

    def print_bridge_domains_l2(self, info, title=False):
        if len(info) == 0:
            return

        if title:
            self.my_output.default(
                'Bridge Domain L2 Forwarding Properties',
                underline=True,
                before_newline=True
            )

        order = [
            'nameTenant',
            'unkMacUcastActT',
            'bcastP',
            'arpFloodTick',
            'multiDstPktActT',
            'epClearTick'
        ]

        headers = [
            'Bridge Domain',
            'L2 Unknown Ucast',
            'Mcast (GIPo)',
            'ARP Flooding',
            'Multi Dest Flooding',
            'Clear Remote MAC'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            underline=True,
            table=True
        )

    def print_bridge_domains_l3(self, info, title=False):
        if len(info) == 0:
            return

        if title:
            self.my_output.default(
                'Bridge Domain L3 Properties',
                underline=True,
                before_newline=True
            )

        order = [
            'nameTenant',
            'unicastRouteTick',
            'mac',
            'vmacT',
            'ipLearningTick',
            'limitIpLearnToSubnetsTick',
            'hostBasedRoutingTick',
            'epMoveDetectModeT'
        ]

        headers = [
            'Bridge Domain',
            'Ucast Routing',
            'BD MAC',
            'Virtual MAC',
            'IP Learning',
            'Limit Local IP Learning',
            'Adv Host Routes',
            'EP Move Detection Mode'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            remove_empty_columns=False,
            underline=True,
            table=True
        )

    def print_bridge_domains_mcast(self, info, title=False):
        if len(info) == 0:
            return

        if title:
            self.my_output.default(
                'Bridge Domain Multicast Properties',
                underline=True,
                before_newline=True
            )

        order = [
            'nameTenant',
            'mcastAllowTick',
            'unkMcastActT',
            'fvRsIgmpsn.nameTenant',
            'ipv6McastAllowTick',
            'v6unkMcastActT',
            'fvRsMldsn.nameTenant'
        ]

        headers = [
            'Bridge Domain',
            'PIM',
            'Unknown IPv4 Flooding',
            'IGMP Snooping Policy',
            'PIMv6',
            'Unknown IPv6 Flooding',
            'MLD Snooping Policy'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            underline=True,
            table=True
        )

    def print_bridge_domains_vrf(self, info, title=False):
        if len(info) == 0:
            return

        if title:
            self.my_output.default(
                'Bridge Domain VRF Properties',
                underline=True,
                before_newline=True
            )

        order = [
            'nameTenant',
            'fvCtx.nameTenant',
            'fvCtx.ipDataPlaneLearningTick',
            'fvCtx.pcEnfDir',
            'fvCtx.pcEnfPref',
            'fvCtx.bdEnforcedEnableTick'
        ]

        headers = [
            'Bridge Domain',
            'VRF',
            'Learning',
            'PCE Direction',
            'PCE Preference',
            'BD Enforcement'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            underline=True,
            table=True
        )

    def print_bridge_domains(self, info, title=False):
        if len(info) == 0:
            return

        if title:
            self.my_output.default(
                'Bridge Domain Summary [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        order = [
            'nameTenant',
            'pcTag',
            'seg',
            'fvSubnet.ip',
            'fvSubnet.usage',
            'fvAEPg.nameTenant',
            'fvRsCtx.nameTenant',
            'fvRsBDToOut.nameTenant'
        ]

        headers = [
            'Bridge Domain',
            'Class ID',
            'VNID',
            'Subnet',
            'Usage',
            'EPG',
            'VRF',
            'L3Out'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['fvSubnet', 'fvRsBDToOut', 'fvAEPg']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            remove_empty_columns=False,
            underline=True,
            table=True
        )
