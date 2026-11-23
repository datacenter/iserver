class DomainVmmOutput():
    def __init__(self):
        pass

    def print_domains_vmm(self, info, title=False):
        if title:
            self.my_output.default(
                'VMM Domain [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        for item in info:
            item['fvnsEncapBlk'] = []
            if item['vlan_info'] is not None:
                item['fvnsEncapBlk'] = item['vlan_info']['fvnsEncapBlk']

        for item in info:
            if len(item['aaaDomain']) == 0:
                item['aaaDomain'].append('--')

        order = [
            'faults',
            'name',
            'aaep_names',
            'vlan',
            'vlan_info.allocMode',
            'fvnsEncapBlk.blockInfo',
            'epgCount',
            'aaaDomain'
        ]

        headers = [
            'Faults',
            'Domain',
            'AAEP',
            'VLAN Pool',
            'Mode',
            'Encapsulation Block',
            'EPG',
            'Sec Domain'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['aaep_names', 'fvnsEncapBlk', 'aaaDomain']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_domains_vmm_prop(self, info, title=False):
        if title:
            self.my_output.default(
                'VMM Domain - Properties [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'name',
            'encapMode',
            'accessModeT',
            'configInfraPg',
            'enableTag',
            'enableVmFolder',
            'epInventoryType',
            'epRetTime',
            'numOfUplinks'
        ]

        headers = [
            'Domain Name',
            'Encap',
            'Access Mode',
            'Cfg Infra PGs',
            'Tag Collection',
            'VM Folder Data',
            'Ep Inventory',
            'Ep Retention Time',
            'Uplinks'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_domains_vmm_vcenter(self, info, title=False):
        if title:
            self.my_output.default(
                'VMM Domain - vCenter [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'faults',
            'name',
            'controller.faults',
            'controller.name',
            'controller.hostOrIp',
            'controller.usr',
            'controller.operStTick',
            'controller.model',
            'controller.serialShort',
            'controller.rev',
            'controller.rootContName',
            'controller.hvCount',
            'controller.vmCount'
        ]

        headers = [
            'Faults',
            'Domain Name',
            'Controller Faults',
            'Controller Name',
            'IP',
            'Username',
            'Online',
            'Model',
            'Serial',
            'Rev',
            'Datacenter',
            'HV',
            'VM'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['controller']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_domains_vmm_epg(self, info, title=False):
        epg = []
        for item in info:
            for epg_info in item['vmmEpPD']:
                epg_info['domainName'] = item['name']
                epg.append(
                    epg_info
                )

        epg = sorted(
            epg,
            key=lambda i: (
                i['domainName'],
                i['tenantAppEpg']
            )
        )

        if title:
            self.my_output.default(
                'VMM Domain - Associated EPG [#%s]' % (len(epg)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'domainName',
            'tenantAppEpg',
            'encapCtx',
            'allocMode',
            'vlanId',
            'instrImedcy',
            'resImedcy',
            'switchingMode'
        ]

        headers = [
            'Domain Name',
            'EPG',
            'VLAN Pool',
            'Alloc Mode',
            'VLAN',
            'Deployment',
            'Resolution',
            'Switching'
        ]

        self.my_output.my_table(
            epg,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_domains_vmm_node(self, info, title=False):
        if title:
            self.my_output.default(
                'VMM Domain - Nodes [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'faults',
            'name',
            'aaep_names',
            'vlan',
            'node.name',
            'node.interfaces'
        ]

        headers = [
            'Faults',
            'Domain',
            'AAEP',
            'VLAN Pool',
            'Node',
            'Interfaces'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['aaep_names', 'node']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_domains_vmm_interface(self, info, title=False):
        if title:
            self.my_output.default(
                'VMM Domain - Interfaces [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'faults',
            'name',
            'aaep_names',
            'vlan',
            'interface.node_name',
            'interface.intf_name'
        ]

        headers = [
            'Faults',
            'Domain',
            'AAEP',
            'VLAN Pool',
            'Node',
            'Interface'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['aaep_names', 'interface']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_domains_vmm_vlan(self, info, title=False):
        if title:
            self.my_output.default(
                'VMM Domain - Interfaces VLAN [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        for item in info:
            item['fvnsEncapBlk'] = []
            if item['vlan_info'] is not None:
                item['fvnsEncapBlk'] = item['vlan_info']['fvnsEncapBlk']

        order = [
            'faults',
            'name',
            'aaep_names',
            'vlan',
            'fvnsEncapBlk.blockInfo',
            'interface.node_name',
            'interface.intf_name',
            'interface.operSt',
            'interface.operMode',
            'interface.vlans'
        ]

        headers = [
            'Faults',
            'Domain',
            'AAEP',
            'VLAN Pool',
            'Encapsulation Block',
            'Node',
            'Interface',
            'State',
            'Mode',
            'VLANs'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['aaep_names', 'interface', 'fvnsEncapBlk']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_domains_vmm_reln(self, info, title=False):
        if title:
            self.my_output.default(
                'VMM Domain - Policy Relationships [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            if title:
                self.my_output.default('None')
            return

        order = [
            'faults',
            'name',
            'reln.type',
            'reln.name'
        ]

        headers = [
            'Faults',
            'Domain',
            'Policy Type',
            'Policy Name'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['reln']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_domains_vmm_event_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'VMM Domain - Event Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'VMM Domain - Event Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'domainName',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'Domain',
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

    def print_domains_vmm_fault_inst(self, info, title=False):
        if title:
            self.my_output.default(
                'VMM Domain - Faults [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'domainName',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Domain',
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

    def print_domains_vmm_fault_record(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'VMM Domain - Fault Records [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'VMM Domain - Fault Records last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'domainName',
            'severityT',
            'code',
            'cause',
            'created',
            'lc',
            'descrT'
        ]

        headers = [
            'Domain',
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

    def print_domains_vmm_audit_logs(self, info, when=None, title=False):
        if title:
            if when is None:
                self.my_output.default(
                    'VMM Domain - Audit Logs [#%s]' % (len(info)),
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    'VMM Domain - Audit Logs last %s [#%s]' % (when, len(info)),
                    underline=True,
                    before_newline=True
                )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'domainName',
            'severityT',
            'code',
            'cause',
            'created',
            'descrT',
            'changeSetT'
        ]

        headers = [
            'Domain',
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
