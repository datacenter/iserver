import copy


class OspRouterOutput():
    def __init__(self):
        pass

    def print_routers(self, info, title=False, select=False):
        if title:
            self.my_output.default(
                'Router [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

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
            'haTick',
            'snatTick',
            'network_name',
            'fixed_ips.subnet_name',
            'fixed_ips.cidr',
            'fixed_ips.gateway_ip',
            'fixed_ips.ip_address',
            'created_age'
        ]

        headers = headers + [
            'Name',
            'Tenant',
            'Admin',
            'Status',
            'HA',
            'SNAT',
            'Network',
            'Subnet',
            'CIDR',
            'Gateway',
            'IP',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['fixed_ips']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_routers_port(self, info, title=False):
        if title:
            self.my_output.default(
                'Router - Port [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            if item['tenant_name'] is None:
                item['extended_name'] = item['name']
            else:
                item['extended_name'] = '%s/%s' % (
                    item['tenant_name'],
                    item['name']
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

        order = [
            'extended_name',
            'port_info.mac_address',
            'port_info.ips',
            'port_info.type',
            'port_info.vm_tenant_name'
        ]

        headers = [
            'Name',
            'MAC',
            'IP',
            'Type',
            'VM'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['port_info']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_routers_id(self, info, title=False):
        if title:
            self.my_output.default(
                'Router - Identifier [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'id',
            'tenant_id',
            'network_id',
            'fixed_ips.subnet_id'
        ]

        headers = [
            'Name',
            'Id',
            'Tenant',
            'Network',
            'Subnet'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['fixed_ips']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def select_router(self, info):
        self.my_output.default(
            'Select Router [#%s]' % (len(info)),
            underline=True,
            before_newline=True
        )

        if len(info) == 0:
            self.my_output.default('No router found')
            return None

        new_info = copy.deepcopy(info)

        index = 1
        for item in new_info:
            item['__id'] = index
            index = index + 1

        self.print_routers(new_info, title=False, select=True)

        while True:
            answer = input("Select router using index value (0 to break): ")
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
