class VrfOutput():
    def __init__(self):
        pass

    def print_vrf_properties(self, info):
        order = [
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
        if len(info) == 0:
            return

        if title:
            self.my_output.default(
                'VRF IPv4 Routes',
                underline=True,
                before_newline=True
            )

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
                info,
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
                info['v4route']
            )

    def print_vrfs_properties(self, info, title=False):
        if len(info) == 0:
            return

        if title:
            self.my_output.default(
                'VRF Properties',
                underline=True,
                before_newline=True
            )

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

    def print_vrfs(self, info, title=False):
        if len(info) == 0:
            return

        if title:
            self.my_output.default(
                'VRF Summary [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        order = [
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
