class VrfOutput():
    def __init__(self):
        pass

    def print_vrf_properties(self, info):
        order = [
            'name',
            'tenant',
            'ipDataPlaneLearning',
            'knwMcastAct',
            'pcEnfDir',
            'pcEnfPref',
            'bdEnforcedEnable'
        ]

        headers = [
            'Name',
            'Tenant',
            'Data Plane Learning',
            'Multicast',
            'Policy Control Enforcement Direction',
            'Policy Control Enforcement Preference',
            'Bridge Domain Enforcement Status'
        ]

        if 'endpointsCount' in info:
            order.append('endpointsCount')
            headers.append('Endpoints Count')

        self.my_output.dictionary(
            info,
            title='VRF Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_vrf_v4_route(self, info):
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

    def print_vrfs_properties(self, info):
        if len(info) == 0:
            self.my_output.default('No vrf found')
            return

        order = [
            'nameTenant',
            'ipDataPlaneLearning',
            'knwMcastAct',
            'pcEnfPref',
            'pcEnfDir',
            'bdEnforcedEnable'
        ]

        headers = [
            'VRF',
            'DP Learning',
            'Mcast',
            'PCE Preference',
            'PCE Direction',
            'BD Enforced'
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

    def print_vrfs_references(self, info):
        if len(info) == 0:
            self.my_output.default('No vrf found')
            return

        order = [
            'nameTenant',
            'fvAEPg.nameApTenant',
            'fvBD.nameTenant',
            'fvSubnet.ip',
            'l3out.nameTenant'
        ]

        headers = [
            'VRF',
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

    def print_vrfs(self, info):
        if len(info) == 0:
            self.my_output.default('No vrf found')
            return

        order = [
            'nameTenant',
            'pcEnfPref',
            'pcEnfDir',
            'fvAEPg.nameApTenant',
            'fvBD.nameTenant',
            'fvSubnet.ip',
            'l3out.nameTenant'
        ]

        headers = [
            'VRF',
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
