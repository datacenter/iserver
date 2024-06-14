import copy


class OspNetworkOutput():
    def __init__(self):
        pass

    def print_networks(self, info, title=False, select=False):
        if title:
            self.my_output.default(
                'Network [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = copy.deepcopy(info)
        for item in new_info:
            if item['tenant_name'] is None:
                item['tenant_name'] = '--'

            item['router'] = '--'
            if item['router_name'] is not None:
                item['router'] = '%s/%s' % (
                    item['router_tenant_name'],
                    item['router_name']
                )

            if len(item['subnet_info']) == 0:
                empty_subnet = {}
                empty_subnet['name'] = '--'
                empty_subnet['cidr'] = '--'
                item['subnet_info'].append(empty_subnet)

        order = []
        headers = []
        if select:
            order.append('__id')
            headers.append('Index')

        order = order + [
            'name',
            'tenant_name',
            'adminTick',
            'status',
            'sharedTick',
            'externalTick',
            'securityTick',
            'mtu',
            'subnet_info.name',
            'subnet_info.cidr',
            'router',
            'created_age'
        ]

        headers = headers + [
            'Name',
            'Tenant',
            'Admin',
            'Status',
            'Shared',
            'Ext',
            'Sec',
            'MTU',
            'Subnet',
            'CIDR',
            'Router',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['subnet_info']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_networks_port(self, info, title=False):
        if title:
            self.my_output.default(
                'Network - Port [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = copy.deepcopy(info)
        for item in new_info:
            if item['tenant_name'] is None:
                item['extended_name'] = item['name']
            else:
                item['extended_name'] = '%s/%s' % (
                    item['tenant_name'],
                    item['name']
                )

            if len(item['subnet_info']) == 0:
                item['subnet_info'].append(
                    dict(
                        name='--',
                        cidr='--'
                    )
                )

            if len(item['port_info']) == 0:
                item['port_info'].append(
                    dict(
                        mac_address='--',
                        ips='--',
                        type='--',
                        vm_tenant_name='--'
                    )
                )

            for port in item['port_info']:
                if port['vm_tenant_name'] is None:
                    port['vm_tenant_name'] = '--'

                if 'binding_host_id' not in port or port['binding_host_id'] is None:
                    port['binding_host_id'] = '--'

        order = [
            'extended_name',
            'subnet_info.cidr',
            'port_info.mac_address',
            'port_info.ips',
            'port_info.type',
            'port_info.vm_tenant_name',
            'port_info.binding_host_id'
        ]

        headers = [
            'Name',
            'CIDR',
            'MAC',
            'IP',
            'Type',
            'VM',
            'HV'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['subnet_info', 'port_info']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_networks_phy(self, info, title=False):
        if title:
            self.my_output.default(
                'Network - Phy [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = copy.deepcopy(info)
        for item in new_info:
            if item['tenant_name'] is None:
                item['extended_name'] = item['name']
            else:
                item['extended_name'] = '%s/%s' % (
                    item['tenant_name'],
                    item['name']
                )

            if item['provider_segmentation_id'] is None:
                item['provider_segmentation_id'] = '--'

        order = [
            'extended_name',
            'adminTick',
            'status',
            'provider_network_type',
            'provider_physical_network',
            'provider_segmentation_id'
        ]

        headers = [
            'Name',
            'Admin',
            'Status',
            'Network Type',
            'Physical Network',
            'Segmentation ID'
        ]

        self.my_output.my_table(
            new_info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_networks_id(self, info, title=False):
        if title:
            self.my_output.default(
                'Network - Identifier [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'id',
            'name',
            'tenant_id',
            'subnets'
        ]

        headers = [
            'Id',
            'Name',
            'Tenant',
            'Subnet'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['subnets']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def select_network(self, info):
        self.my_output.default(
            'Select Network [#%s]' % (len(info)),
            underline=True,
            before_newline=True
        )

        if len(info) == 0:
            self.my_output.default('No network found')
            return None

        new_info = copy.deepcopy(info)

        index = 1
        for item in new_info:
            item['__id'] = index
            index = index + 1

        self.print_networks(new_info, title=False, select=True)

        while True:
            answer = input("Select network using index value (0 to break): ")
            if answer is None:
                continue

            try:
                selected_id = int(answer)
            except BaseException:
                selected_id = 0

            if selected_id == 0:
                return None

            for item in new_info:
                if item['__id'] == int(answer):
                    return item
