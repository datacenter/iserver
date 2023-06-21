class BridgeDomainOutput():
    def __init__(self):
        pass

    def print_bridge_domain_properties(self, info):
        order = [
            'name',
            'tenant',
            'dn',
            'descr',
            'health.score',
            'type',
            'fvSubnetCount',
            'fvRsCtx.nameTenant',
            'l3OutCount',
            'endpointsCount',
            'epgsCount'
        ]

        headers = [
            'Name',
            'Tenant',
            'Dn',
            'Description',
            'Health Score',
            'Type',
            'Subnet Count',
            'VRF',
            'Associated L3 Outs',
            'Endpoints Count',
            'Endpoint Groups Count'
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
            'unkMacUcastAct',
            'multiDstPktAct',
            'epClear'
        ]

        headers = [
            'L2 Unknown Unicast',
            'Multi Destination Flooding',
            'Clear Remote MAC Entries'
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
            'fvRsIgmpsn.name',
            'fvRsMldsn.name',
            'mcastAllow',
            'unkMcastAct',
            'ipv6McastAllow',
            'v6unkMcastAct'
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
            'unicastRoute',
            'mac',
            'vmac',
            'ipLearning',
            'hostBasedRouting',
            'limitIpLearnToSubnets',
            'arpFlood',
            'epMoveDetectMode'
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
            'preferred',
            'virtual',
            'scope',
            'ipDPLearning',
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
            'name',
            'tenant',
            'application_profile',
            'endpointsCount',
            'vzBrCP.tenant_name'
        ]

        headers = [
            'Up',
            'EPG Name',
            'Tenant',
            'App Profile',
            'Endpoints',
            'Contract'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info['fvAEPg'],
                order,
                ['vzBrCP']
            ),
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
                'Bridge Domain L2 Properties',
                underline=True,
                before_newline=True
            )

        order = [
            'nameTenant',
            'unkMacUcastAct',
            'arpFlood',
            'multiDstPktAct',
            'epClear',
            'intersiteL2Stretch'
        ]

        headers = [
            'Bridge Domain',
            'L2 Unknown Ucast',
            'ARP Flooding',
            'Multi Dest Flooding',
            'Clear Remote MAC',
            'Scaled L2 Only'
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
            'unicastRoute',
            'mac',
            'vmac',
            'ipLearning',
            'limitIpLearnToSubnets',
            'hostBasedRouting',
            'epMoveDetectMode'
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
            'unkMcastAct',
            'fvRsIgmpsn.nameTenant',
            'ipv6McastAllowTick',
            'v6unkMcastAct',
            'fvRsMldsn.nameTenant'
        ]

        headers = [
            'Bridge Domain',
            'PIM',
            'Unknown IPv4 Flooding',
            'IGMP Snooping',
            'PIMv6',
            'Unknown IPv6 Flooding',
            'MLD Snooping'
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
            'fvCtx.ipDataPlaneLearning',
            'fvCtx.pcEnfDir',
            'fvCtx.pcEnfPref',
            'fvCtx.bdEnforcedEnable'
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
                'Bridge Domain Summary',
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
