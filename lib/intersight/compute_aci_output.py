class ComputeAciOutput():
    def __init__(self):
        pass

    def print_aci(self, server, title=False):
        self.print_aci_summary(server, title=title)
        self.print_aci_endpoint(server, title=title)
        self.print_aci_lacp(server, title=title)
        self.print_aci_lldp(server, title=title)

    def print_aci_summary(self, server, title=False):
        if title:
            self.my_output.default(
                'Interface - ACI Summary [#%s]' % (len(server['MacAddressInfo'])),
                underline=True,
                before_newline=True
            )

        if len(server['MacAddressInfo']) == 0:
            self.my_output.default('None')
            return

        for item in server['MacAddressInfo']:
            item['__Output'] = {}
            in_aci = False
            if item['endpoint'] is not None:
                in_aci = True
                item['epTick'] = '\u2713'
                item['__Output']['epTick'] = 'Green'
            else:
                item['epTick'] = '\u2717'
                item['__Output']['epTick'] = 'Red'

            if len(item['lacp']) > 0:
                in_aci = True
                item['lacpTick'] = '\u2713'
                item['__Output']['lacpTick'] = 'Green'
            else:
                item['lacpTick'] = '\u2717'
                item['__Output']['lacpTick'] = 'Red'

            if item['adjacency'] is not None:
                in_aci = True
                item['lldpTick'] = '\u2713'
                item['__Output']['lldpTick'] = 'Green'
            else:
                item['lldpTick'] = '\u2717'
                item['__Output']['lldpTick'] = 'Red'

            if in_aci:
                item['aciTick'] = '\u2713'
                item['__Output']['aciTick'] = 'Green'
            else:
                item['aciTick'] = '\u2717'
                item['__Output']['aciTick'] = 'Red'

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
            'aciTick',
            'epTick',
            'lacpTick',
            'lldpTick',
        ]

        headers = [
            'MAC Address',
            'Interface',
            'Adapter',
            'Pci Slot',
            'ACI',
            'Endpoint',
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

    def print_aci_endpoint(self, server, skip_empty=True, title=False):
        macs = sorted(
            server['MacAddressInfo'],
            key=lambda i: (
                i['AdapterModel'],
                i['InterfaceName'],
            )
        )

        info = []

        for mac in macs:
            if mac['endpoint'] is None:
                if skip_empty:
                    continue
                mac['endpoint'] = {}
                mac['endpoint']['ip'] = '--'
                mac['endpoint']['epgNameApTenant'] = '--'
                mac['endpoint']['encapT'] = '--'
                mac['endpoint']['bdNameTenant'] = '--'
                mac['endpoint']['vrfNameTenant'] = '--'
                mac['fabric'] = [dict(ep='--')]
            else:
                mac['fabric'] = mac['endpoint']['fabric']

            info.append(mac)

        if len(info) == 0:
            return

        if title:
            self.my_output.default(
                'Endpoint [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        order = [
            'MacAddress',
            'InterfaceName',
            'AdapterModel',
            'AdapterPciSlot',
            'endpoint.ip',
            'endpoint.epgNameApTenant',
            'endpoint.encapT',
            'endpoint.bdNameTenant',
            'endpoint.vrfNameTenant',
            'fabric.ep'
        ]

        headers = [
            'MAC Address',
            'Interface',
            'Adapter',
            'Pci Slot',
            'IP Address',
            'EPG',
            'Encap',
            'BD',
            'VRF',
            'Fabric'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['fabric']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True,
            merge=True
        )

    def print_aci_lacp(self, server, skip_empty=True, title=False):
        macs = sorted(
            server['MacAddressInfo'],
            key=lambda i: (
                i['AdapterModel'],
                i['InterfaceName'],
            )
        )

        info = []

        for mac in macs:
            if mac['lacp'] is None or len(mac['lacp']) == 0:
                if skip_empty:
                    continue

                empty_lacp = {}
                empty_lacp['pod_node_name'] = '--'
                empty_lacp['id'] = '--'
                empty_lacp['key'] = '--'
                empty_lacp['adjacency'] = {}
                empty_lacp['adjacency']['sysId'] = '--'
                empty_lacp['adjacency']['sysPrio'] = '--'
                empty_lacp['adjacency']['key'] = '--'
                empty_lacp['adjacency']['port'] = '--'
                empty_lacp['adjacency']['portPrio'] = '--'
                mac['lacp'].append(
                    empty_lacp
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
            'lacp.pod_node_name',
            'lacp.id',
            'lacp.key',
            'lacp.adjacency.sysId',
            'lacp.adjacency.sysPrio',
            'lacp.adjacency.key',
            'lacp.adjacency.port',
            'lacp.adjacency.portPrio'
        ]

        headers = [
            'MAC Address',
            'Interface',
            'Adapter',
            'Pci Slot',
            'ACI Node',
            'Member',
            'Oper Key',
            'Nbr System MAC',
            'Nbr System Prio',
            'Nbr Oper Key',
            'Nbr Port',
            'Nbr Port Prio'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['lacp']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            table=True,
            merge=True
        )

    def print_aci_lldp(self, server, skip_empty=True, title=False):
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
                mac['adjacency']['pod_node_name'] = '--'
                mac['adjacency']['interface_id'] = '--'
                mac['adjacency']['health'] = '--'
                mac['adjacency']['faults'] = '--'

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
            'adjacency.pod_node_name',
            'adjacency.interface_id',
            'adjacency.health',
            'adjacency.faults',
        ]

        headers = [
            'MAC Address',
            'Interface',
            'Adapter',
            'Pci Slot',
            'ACI Node',
            'Interface',
            'Nei Health',
            'Nei Faults'
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
