class EndpointOutput():
    def __init__(self):
        pass

    def print_endpoints_apic(self, endpoints):
        if not self.is_apic:
            return False

        if len(endpoints) == 0:
            return False

        if 'apic' not in endpoints[0]:
            return False

        return True

    def print_endpoints(self, endpoints, bridge_domain_name=True, stream='default', title=False):
        if title:
            self.my_output.default(
                'Endpoint [#%s]' % (len(endpoints)),
                underline=True,
                before_newline=True
            )

        if len(endpoints) == 0:
            self.my_output.default('None')
            return

        is_apic = self.print_endpoints_apic(endpoints)
        order = []
        if is_apic:
            order = ['apic']

        order = order + [
            'flags',
            'mac',
            'fvIp.addr',
            'epgNameApTenant',
            'encapT',
            'bdNameTenant',
            'vrfNameTenant',
            'fabric.ep'
        ]

        headers = []
        if is_apic:
            headers = ['Apic']

        headers = headers + [
            'SF',
            'MAC Address',
            'IP Address',
            'EPG',
            'Encap',
            'BD',
            'VRF',
            'Fabric'
        ]

        if not bridge_domain_name:
            order.remove('bdNameTenant')
            headers.remove('BD')

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

        is_apic = self.print_endpoints_apic(endpoints)
        if is_apic:
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
        if is_apic:
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
