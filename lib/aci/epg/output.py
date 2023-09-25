class EpgOutput():
    def __init__(self):
        pass

    def print_epg_properties(self, info):
        order = [
            'health',
            'faults',
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
            'Health',
            'Faults',
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
                underline=True,
                before_newline=True
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

        if len(info['contractTaboo']) > 0:
            self.my_output.default(
                'Contract Taboo',
                underline=True,
                before_newline=True
            )
            for contract in info['contractTaboo']:
                self.my_output.default(
                    '- %s' % (contract['nameTenant'])
                )

        if len(info['contractTabooInfo']) > 0:
            self.print_taboos(
                info['contractTabooInfo'],
                show_taboo_filters=True
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
        if info['endpointCount'] > 0:
            self.my_output.default(
                'EPG Endpoints',
                underline=True,
                before_newline=True
            )
            self.print_endpoints(
                info['fvCEp'],
                bridge_domain_name=False,
                title=True
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

    def print_epgs_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'EPG - Properties [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'health',
            'faults',
            'nameApTenant',
            'prefGrMemb',
            'floodOnEncap',
            'pcTagT',
            'prio',
            'pcEnfPref',
            'matchT'
        ]

        headers = [
            'Health',
            'Faults',
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
            remove_empty_columns=False,
            table=True
        )

    def print_epgs_bridge_domain(self, info, title=False):
        if title:
            self.my_output.default(
                'EPG - Bridge Domain [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
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
            'fvBD.fvRsCtx.nameTenant',
            'fvRsBDToOut.nameTenant'
        ]

        headers = [
            'Up',
            'EPG',
            'Bridge Domain',
            'BD Subnets',
            'Usage',
            'VRF',
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

    def print_epgs_contract(self, info, title=False):
        if title:
            self.my_output.default(
                'EPG - Contracts [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'adminUpTick',
            'nameApTenant',
            'pcTagT',
            'contractConsumed.nameTenant',
            'contractProvided.nameTenant',
            'contractTaboo.nameTenant'
        ]

        headers = [
            'Up',
            'EPG',
            'Class ID',
            'Contract Consumed',
            'Contract Provided',
            'Contract Taboo'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['contractConsumed', 'contractProvided', 'contractTaboo']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_epgs_contract_pivot(self, info, title=False):
        if title:
            self.my_output.default(
                'EPG - Contracts (pivot view) [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        contract_names = []
        contracts = []
        taboo_names = []
        taboos = []
        for epg_info in info:
            for contract_info in epg_info['contractConsumed']:
                if contract_info['nameTenant'] not in contract_names:
                    contract_names.append(
                        contract_info['nameTenant']
                    )
                    contract_info['type'] = 'Contract'
                    contract_info['epg'] = []
                    contracts.append(
                        contract_info
                    )

            for contract_info in epg_info['contractProvided']:
                if contract_info['nameTenant'] not in contract_names:
                    contract_names.append(
                        contract_info['nameTenant']
                    )
                    contract_info['type'] = 'Contract'
                    contract_info['epg'] = []
                    contracts.append(
                        contract_info
                    )

            for contract_info in epg_info['contractTaboo']:
                if contract_info['nameTenant'] not in taboo_names:
                    taboo_names.append(
                        contract_info['nameTenant']
                    )
                    contract_info['type'] = 'Taboo'
                    contract_info['epg'] = []
                    taboos.append(
                        contract_info
                    )

        for contract_info in contracts:
            for epg_info in info:
                for epg_contract_info in epg_info['contractConsumed']:
                    if epg_contract_info['nameTenant'] == contract_info['nameTenant']:
                        contract_info['epg'].append(
                            '%s (Consumed)' % (epg_info['nameApTenant'])
                        )

                for epg_contract_info in epg_info['contractProvided']:
                    if epg_contract_info['nameTenant'] == contract_info['nameTenant']:
                        contract_info['epg'].append(
                            '%s (Provided)' % (epg_info['nameApTenant'])
                        )

        for taboo_info in taboos:
            for epg_info in info:
                for epg_contract_info in epg_info['contractTaboo']:
                    if epg_contract_info['nameTenant'] == taboo_info['nameTenant']:
                        taboo_info['epg'].append(
                            epg_info['nameApTenant']
                        )

        all_contracts = contracts + taboos
        all_contracts = sorted(
            all_contracts,
            key=lambda i: i['nameTenant']
        )

        order = [
            'nameTenant',
            'type',
            'epg'
        ]

        headers = [
            'Contract',
            'Type',
            'EPG'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                all_contracts,
                order,
                ['epg']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_epgs_node(self, info, title=False):
        if title:
            self.my_output.default(
                'EPG - Deployed Nodes [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
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

    def print_epgs_node_pivot(self, info, title=False):
        if title:
            self.my_output.default(
                'EPG - Deployed Nodes (pivot view) [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        names = []
        nodes = []
        for epg_info in info:
            for node_info in epg_info['fabricNode']:
                if node_info['pod_node_name'] not in names:
                    names.append(
                        node_info['pod_node_name']
                    )
                    node_info['epg'] = []
                    nodes.append(
                        node_info
                    )

        for node_info in nodes:
            for epg_info in info:
                for epg_node_info in epg_info['fabricNode']:
                    if epg_node_info['pod_node_name'] == node_info['pod_node_name']:
                        node_info['epg'].append(
                            epg_info['nameApTenant']
                        )

        order = [
            'name',
            'address',
            'adSt',
            'fabricSt',
            'model',
            'serial',
            'version',
            'epg',

        ]

        headers = [
            'Node Name',
            'IP Address',
            'Admin',
            'Fabric',
            'Model',
            'Serial',
            'Version',
            'EPG'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                nodes,
                order,
                ['epg']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_epgs_static_port(self, info, title=False):
        if title:
            self.my_output.default(
                'EPG - Static Port [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return
        order = [
            'nameApTenant',
            'staticPort.pathNodeT',
            'staticPort.pathType',
            'staticPort.pathEp',
            'staticPort.encap',
            'staticPort.modeT',
            'staticPort.instrImedcy',
            'staticPort.state'
        ]

        headers = [
            'EPG',
            'Path',
            'Type',
            'Ep',
            'Encapsulation',
            'Mode',
            'Deployment Immediacy',
            'State'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['staticPort']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_epgs_domain(self, info, title=False):
        if title:
            self.my_output.default(
                'EPG - Domain [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nameApTenant',
            'domain.name',
            'domain.typeT',
            'domain.instrImedcy',
            'domain.resImedcy',
            'domain.switchingMode',
            'domain.encapMode',
            'domain.epgCos'
        ]

        headers = [
            'EPG',
            'Domain Name',
            'Domain Type',
            'Deployment',
            'Resolution',
            'Switching Mode',
            'Encap Mode',
            'CoS'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['vlan', 'domain', 'domainVlanPool']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_epgs_domain_pivot(self, info, title=False):
        if title:
            self.my_output.default(
                'EPG - Domain (pivot view) [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        names = []
        domains = []
        for epg_info in info:
            for domain_info in epg_info['domain']:
                if domain_info['name'] not in names:
                    names.append(
                        domain_info['name']
                    )
                    domain_info['epg'] = []
                    domains.append(
                        domain_info
                    )

        for domain_info in domains:
            for epg_info in info:
                for epg_domain_info in epg_info['domain']:
                    if epg_domain_info['name'] == domain_info['name']:
                        domain_info['epg'].append(
                            epg_info['nameApTenant']
                        )

        order = [
            'name',
            'typeT',
            'instrImedcy',
            'resImedcy',
            'switchingMode',
            'encapMode',
            'epgCos',
            'epg',

        ]

        headers = [
            'Domain Name',
            'Domain Type',
            'Deployment',
            'Resolution',
            'Switching Mode',
            'Encap Mode',
            'CoS',
            'EPG'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                domains,
                order,
                ['epg']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_epgs_member(self, info, title=False):
        if title:
            self.my_output.default(
                'EPG - Member [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nameApTenant',
            'member.memberType',
            'member.nodeName',
            'member.pathType',
            'member.pathName',
            'member.encap'
        ]

        headers = [
            'EPG',
            'Member Type',
            'Node',
            'Type',
            'ID',
            'VLAN'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['member']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_epgs_endpoint(self, info, title=False):
        if title:
            self.my_output.default(
                'EPG - Endpoints [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'flags',
            'mac',
            'fvIp.addr',
            'epgNameApTenant',
            'encapT',
            'bdNameTenant',
            'vrfNameTenant'
        ]

        headers = [
            'SF',
            'MAC Address',
            'IP Address',
            'EPG',
            'Encap',
            'BD',
            'VRF'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['fvIp']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            remove_empty_columns=False,
            table=True
        )

    def print_epgs(self, info, title=False):
        if title:
            self.my_output.default(
                'EPG [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for epg in info:
            epg['fvSubnet'] = epg['fvBD']['fvSubnet']

        order = [
            'health',
            'faults',
            'adminUpTick',
            'nameApTenant',
            'pcTag',
            'fvBD.nameTenant',
            'fvSubnet.ip',
            'endpointCount',
            'fabricNode.pod_node_name',
            'domain.name',
            'contractCount',
            'staticPortCount',
            'ifconnSummary.fv.stpathatt',
            'ifconnSummary.fv.dyatt'
        ]

        headers = [
            'Health',
            'Faults',
            'Up',
            'EPG',
            'Class ID',
            'BD',
            'BD Subnet',
            'Endpoint',
            'Node',
            'Domain',
            'Contract',
            'StPort',
            'StMember',
            'DynMember'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['fvSubnet', 'vlan', 'fabricNode', 'domain']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_epgs_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'EPG - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'EPG - Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nameApTenant',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'EPG',
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

    def print_epgs_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'EPG - Faults [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nameApTenant',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'EPG',
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

    def print_epgs_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'EPG - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'EPG - Fault Records last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nameApTenant',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'EPG',
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

    def print_epgs_audit_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'EPG - Audit Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'EPG - Audit Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'nameApTenant',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'EPG',
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
