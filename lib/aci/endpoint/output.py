class EndpointOutput():
    def __init__(self):
        pass

    def print_endpoints(self, endpoints, bridge_domain_name=True, stream='default'):
        if len(endpoints) == 0:
            return

        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'flags',
            'mac',
            'fvIp.addr',
            'epgNameApTenant',
            'encapT',
            'bdNameTenant',
            'vrfNameTenant'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'SF',
            'MAC Address',
            'IP Address',
            'EPG',
            'Encap',
            'BD',
            'VRF'
        ]

        if not bridge_domain_name:
            order.remove('bdNameTenant')
            headers.remove('BD')

        self.my_output.my_table(
            self.my_output.expand_lists(
                endpoints,
                order,
                ['fvIp']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            remove_empty_columns=True,
            table=True,
            stream=stream
        )

    def print_endpoints_fabric(self, endpoints, stream='default'):
        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'flags',
            'mac',
            'fvIp.addr',
            'epgName',
            'encapT',
            'fabric.ep'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'SF',
            'MAC Address',
            'IP Address',
            'EPG',
            'Encapsulation',
            'Fabric'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                endpoints,
                order,
                ['fvIp', 'fabric']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            remove_empty_columns=True,
            table=True,
            stream=stream
        )

    def print_endpoints_vmm(self, endpoints):
        order = []
        if self.is_apic:
            order = ['apic']

        order = order + [
            'flags',
            'mac',
            'fvIp.addr',
            'vm.vmm',
            'hv.name',
            'vm.name',
            'vm.state',
            'vnic.name',
            'vnic.operSt'
        ]

        headers = []
        if self.is_apic:
            headers = ['Apic']

        headers = headers + [
            'SF',
            'MAC Address',
            'IP Address',
            'VMM',
            'Hypervisor',
            'VM Name',
            'VM State',
            'vNIC Name',
            'vNIC State'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                endpoints,
                order,
                ['fvIp']
            ),
            merge=True,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            row_separator=True,
            underline=True,
            table=True
        )
