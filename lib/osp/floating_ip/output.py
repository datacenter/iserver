class OspFloatingIpOutput():
    def __init__(self):
        pass

    def print_floating_ips(self, info, title=False):
        if title:
            self.my_output.default(
                'Floating IP [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'status',
            'floating_ip_address',
            'tenant_name',
            'floating_network_name',
            'fixed_ip_address',
            'port_details.mac_address',
            'port_details.network_name',
            'port_details.vm_name',
            'router_name'
        ]

        headers = [
            'Status',
            'Floating',
            'Tenant',
            'Floating Network',
            'Fixed',
            'MAC',
            'Network',
            'VM',
            'Router'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_floating_ips_id(self, info, title=False):
        if title:
            self.my_output.default(
                'Floating IP - Identifiers[#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'status',
            'floating_ip_address',
            'floating_network_id',
            'fixed_ip_address',
            'port_details.network_id',
            'port_details.device_id',
            'router_id',
            'tenant_id'
        ]

        headers = [
            'Status',
            'Floating',
            'Network',
            'Fixed',
            'Network',
            'VM',
            'Router',
            'Tenant'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )
