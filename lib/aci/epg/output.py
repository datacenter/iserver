class EpgOutput():
    def __init__(self):
        pass

    def print_epg_properties(self, info):
        order = [
            'adminUpTick',
            'configSt',
            'name',
            'application_profile',
            'tenant',
            'fvBD.nameTenant',
            'nameAlias',
            'descr',
            'annotation',
            'pcTagT',
            'exceptionTag',
            'prio',
            'pcEnfPref',
            'prefGrMemb',
            'floodOnEncap',
            'isMatch'
        ]

        headers = [
            'Up',
            'Configuration State',
            'EPG Name',
            'Application Profile',
            'Tenant',
            'Bridge Domain',
            'Alias',
            'Description',
            'Annotations',
            'Class ID',
            'Contract Exception Tag',
            'QoS Class',
            'Intra EPG Isolation',
            'Preferred Group Member',
            'Flood in Encapsulation',
            'ESG Matched'
        ]

        self.my_output.dictionary(
            info,
            title='Application EPG Properties',
            underline=True,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers
        )

    def print_epg_contracts(self, info):
        if len(info['contractConsumed']) > 0:
            self.my_output.default(
                'Contract Consumed',
                underline=True
            )
            for contract in info['contractConsumed']:
                self.my_output.default(
                    '- %s' % (contract['nameTenant'])
                )

        if len(info['contractConsumedInfo']) > 0:
            self.print_contracts(
                info['contractConsumedInfo'],
                show_contract_filters=True
            )

        if len(info['contractProvided']) > 0:
            self.my_output.default(
                'Contract Provided',
                underline=True
            )
            for contract in info['contractProvided']:
                self.my_output.default(
                    '- %s' % (contract['nameTenant'])
                )

        if len(info['contractProvidedInfo']) > 0:
            self.print_contracts(
                info['contractProvidedInfo'],
                show_contract_filters=True
            )

    def print_epg_bridge_domain(self, info):
        self.print_bridge_domain_properties(
            info['fvBD']
        )

        self.print_bridge_domain_subnets(
            info['fvBD']['fvSubnet']
        )

    def print_epg_vrf(self, info):
        self.print_vrf_properties(
            info['fvBD']['fvCtxInfo']
        )

    def print_epg_l3out(self, info):
        if len(info['fvBD']['fvRsBDToOut']) > 0:
            self.my_output.default(
                'Associated L3 Out',
                underline=True,
                before_newline=True
            )

            self.print_l3outs(
                info['fvBD']['l3extOutInfo']
            )

    def print_epg_fabric(self, info):
        if len(info['fabricNode']) > 0:
            self.my_output.default(
                'Deployed Nodes',
                underline=True,
                before_newline=True
            )
            self.print_nodes(
                info['fabricNode']
            )

    def print_epg_endpoints(self, info):
        if info['endpointsCount'] > 0:
            self.my_output.default(
                'EPG Endpoints',
                underline=True,
                before_newline=True
            )
            self.print_endpoints(
                info['fvCEp'],
                bridge_domain_name=False
            )

    def print_epg(self, info):
        self.print_epg_properties(
            info
        )

        self.print_epg_contracts(
            info
        )

        self.print_epg_bridge_domain(
            info
        )

        self.print_epg_vrf(
            info
        )

        self.print_epg_l3out(
            info
        )

        self.print_epg_fabric(
            info
        )

        self.print_epg_endpoints(
            info
        )

    def print_epgs_properties(self, info):
        if len(info) == 0:
            self.my_output.default('No application epg found')
            return

        order = [
            'adminUpTick',
            'nameApTenant',
            'prefGrMemb',
            'floodOnEncap',
            'pcTagT',
            'prio',
            'pcEnfPref',
            'matchT'
        ]

        headers = [
            'Up',
            'EPG',
            'Preferred Member',
            'Flood',
            'Class ID',
            'QoS Class',
            'Isolation',
            'Label Match'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            remove_empty_columns=True,
            table=True
        )

    def print_epgs_bridge_domain(self, info):
        if len(info) == 0:
            self.my_output.default('No application epg found')
            return

        for item in info:
            item['fvSubnet'] = None
            item['fvRsBDToOut'] = None
            if item['fvBD'] is not None:
                item['fvSubnet'] = item['fvBD']['fvSubnet']
                item['fvRsBDToOut'] = item['fvBD']['fvRsBDToOut']

        order = [
            'adminUpTick',
            'nameApTenant',
            'fvBD.nameTenant',
            'fvSubnet.ip',
            'fvSubnet.usage',
            'fvRsBDToOut.nameTenant'
        ]

        headers = [
            'Up',
            'EPG',
            'Bridge Domain',
            'BD Subnets',
            'Usage',
            'L3Out'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['fvSubnet', 'fvRsBDToOut']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_epgs_contract(self, info):
        if len(info) == 0:
            self.my_output.default('No application epg found')
            return

        order = [
            'adminUpTick',
            'nameApTenant',
            'contractConsumed.nameTenant',
            'contractProvided.nameTenant'
        ]

        headers = [
            'Up',
            'EPG',
            'Contract Consumed',
            'Contract Provided'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['contractConsumed', 'contractProvided']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_epgs_node(self, info):
        if len(info) == 0:
            self.my_output.default('No application epg found')
            return

        order = [
            'adminUpTick',
            'nameApTenant',
            'fabricNode.name',
            'fabricNode.address',
            'fabricNode.adSt',
            'fabricNode.fabricSt',
            'fabricNode.model',
            'fabricNode.serial',
            'fabricNode.version'

        ]

        headers = [
            'Up',
            'EPG',
            'Node Name',
            'IP Address',
            'Admin',
            'Fabric',
            'Model',
            'Serial',
            'Version'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['fabricNode']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_epgs(self, epgs):
        if len(epgs) == 0:
            self.my_output.default('No application epg found')
            return

        for epg in epgs:
            epg['fvSubnet'] = epg['fvBD']['fvSubnet']

        order = [
            'adminUpTick',
            'nameApTenant',
            'fvBD.nameTenant',
            'fvSubnet.ip',
            'endpointsCount',
            'contractTick'
        ]

        headers = [
            'Up',
            'EPG',
            'Bridge Domain',
            'BD Subnets',
            'Endpoints',
            'Contract'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                epgs,
                order,
                ['fvSubnet']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
