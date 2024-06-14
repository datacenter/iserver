class ComputeNxOutput():
    def __init__(self, log_id=None):
        pass

    def print_nx(self, server, title=False):
        self.print_nx_summary(server, title=title)
        self.print_nx_mac(server, title=title)
        self.print_nx_lacp(server, title=title)
        self.print_nx_lldp(server, title=title)

    def print_nx_summary(self, server, title=False):
        if title:
            self.my_output.default(
                'Interface - Nexus Summary [#%s]' % (len(server['MacAddressInfo'])),
                underline=True,
                before_newline=True
            )

        if len(server['MacAddressInfo']) == 0:
            self.my_output.default('None')
            return

        for item in server['MacAddressInfo']:
            item['__Output'] = {}
            in_nx = False
            if item['mac'] is not None:
                in_nx = True
                item['macTick'] = '\u2713'
                item['__Output']['macTick'] = 'Green'
            else:
                item['macTick'] = '\u2717'
                item['__Output']['macTick'] = 'Red'

            if item['interface'] is not None:
                in_nx = True
                item['lacpTick'] = '\u2713'
                item['__Output']['lacpTick'] = 'Green'
            else:
                item['lacpTick'] = '\u2717'
                item['__Output']['lacpTick'] = 'Red'

            if item['adjacency'] is not None:
                in_nx = True
                item['lldpTick'] = '\u2713'
                item['__Output']['lldpTick'] = 'Green'
            else:
                item['lldpTick'] = '\u2717'
                item['__Output']['lldpTick'] = 'Red'

            if in_nx:
                item['nxTick'] = '\u2713'
                item['__Output']['nxTick'] = 'Green'
            else:
                item['nxTick'] = '\u2717'
                item['__Output']['nxTick'] = 'Red'

        server['MacAddressInfo'] = sorted(
            server['MacAddressInfo'],
            key=lambda i: (
                i['AdapterModel'],
                i['InterfaceName'],
            )
        )

        order = [
            'MacAddress',
            'InterfaceName',
            'AdapterModel',
            'AdapterPciSlot',
            'nxTick',
            'macTick',
            'lacpTick',
            'lldpTick',
        ]

        headers = [
            'MAC Address',
            'Interface',
            'Adapter',
            'Pci Slot',
            'Nexus',
            'MAC',
            'LACP',
            'LLDP'
        ]

        self.my_output.my_table(
            server['MacAddressInfo'],
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True,
            merge=True
        )

    def print_nx_mac(self, server, skip_empty=True, title=False):
        macs = sorted(
            server['MacAddressInfo'],
            key=lambda i: (
                i['AdapterModel'],
                i['InterfaceName'],
            )
        )

        info = []

        for item in macs:
            if item['mac'] is None:
                if skip_empty:
                    continue
                item['mac'] = {}
                item['mac']['nexus_name'] = '--'
                item['mac']['vlan'] = '--'
                item['mac']['mac_addr'] = '--'
                item['mac']['type'] = '--'
                item['mac']['age'] = '--'
                item['mac']['is_secure'] = '--'
                item['mac']['is_ntfy'] = '--'
                item['mac']['port'] = '--'

            info.append(
                item
            )

        if len(info) == 0:
            return

        if title:
            self.my_output.default(
                'MAC Address Table [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        order = [
            'MacAddress',
            'InterfaceName',
            'AdapterModel',
            'AdapterPciSlot',
            'mac.nexus_name',
            'mac.vlan',
            'mac.mac_addr',
            'mac.type',
            'mac.age',
            'mac.is_secure',
            'mac.is_ntfy',
            'mac.port'
        ]

        headers = [
            'MAC Address',
            'Interface',
            'Adapter',
            'Pci Slot',
            'Device',
            'VLAN',
            'MAC',
            'Type',
            'Age',
            'Sec',
            'Ntfy',
            'Port'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True,
            merge=True
        )

    def print_nx_lacp(self, server, skip_empty=True, title=False):
        macs = sorted(
            server['MacAddressInfo'],
            key=lambda i: (
                i['AdapterModel'],
                i['InterfaceName'],
            )
        )

        info = []
        for mac in macs:
            if mac['interface'] is None or len(mac['interface']) == 0:
                if skip_empty:
                    continue

                mac['interface'] = {}
                mac['interface']['nexus_name'] = '--'
                mac['interface']['interface'] = '--'
                mac['port'] = []
                port_info = {}
                port_info['port'] = '--'
                port_info['partner_mac'] = '--'
                port_info['partner_port_num'] = '--'
                port_info['partner_port_state'] = '--'
                mac['port'].append(port_info)
            else:
                if 'port' not in mac:
                    mac['port'] = []

                for interface_info in mac['interface']:
                    for port_info in interface_info['port']:
                        mac['port'].append(
                            port_info
                        )

            info.append(
                mac
            )

        if len(info) == 0:
            return

        if title:
            self.my_output.default(
                'LACP [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        order = [
            'MacAddress',
            'InterfaceName',
            'AdapterModel',
            'AdapterPciSlot',
            'interface.nexus_name',
            'interface.interface',
            'port.port',
            'port.partner_mac',
            'port.partner_port_num',
            'port.partner_port_state'
        ]

        headers = [
            'MAC Address',
            'Interface',
            'Adapter',
            'Pci Slot',
            'Device',
            'Interface',
            'Port',
            'Partner MAC',
            'Partner Port',
            'Partner State'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['port']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True,
            merge=True
        )

    def print_nx_lldp(self, server, skip_empty=True, title=False):
        macs = sorted(
            server['MacAddressInfo'],
            key=lambda i: (
                i['AdapterModel'],
                i['InterfaceName'],
            )
        )

        info = []
        for mac in macs:
            if mac['adjacency'] is None:
                if skip_empty:
                    continue
                mac['adjacency'] = {}
                mac['adjacency']['nexus_name'] = '--'
                mac['adjacency']['l_port_id'] = '--'
                mac['adjacency']['chassis_id'] = '--'
                mac['adjacency']['port_id'] = '--'

            info.append(
                mac
            )

        if len(info) == 0:
            return

        if title:
            self.my_output.default(
                'LLDP [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        order = [
            'MacAddress',
            'InterfaceName',
            'AdapterModel',
            'AdapterPciSlot',
            'adjacency.nexus_name',
            'adjacency.l_port_id',
            'adjacency.chassis_id',
            'adjacency.port_id',
        ]

        headers = [
            'MAC Address',
            'Interface',
            'Adapter',
            'Pci Slot',
            'Device',
            'Interface',
            'Nbr Device ID',
            'Nbr Port ID'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True,
            merge=True
        )
