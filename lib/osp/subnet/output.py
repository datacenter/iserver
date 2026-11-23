import copy
import json


class OspSubnetOutput():
    def __init__(self):
        pass

    def print_subnets(self, info, title=False, select=False):
        if title:
            self.my_output.default(
                'Subnet [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = copy.deepcopy(info)
        for item in new_info:
            item['extended_name'] = []
            item['extended_name'].append(
                item['name']
            )
            if item['tenant_name'] is None:
                item['extended_name'].append(
                    'Tenant: --'
                )
            else:
                item['extended_name'].append(
                    'Tenant: %s' % (item['tenant_name'])
                )

            item['extended_name'].append(
                'Network: %s' % (item['network_name'])
            )

            if len(item['dns_nameservers']) == 0:
                item['dns_nameservers'] = ['--']

            if item['gateway_ip'] is None:
                item['gateway_ip'] = '--'

            if len(item['allocation_pools']) == 0:
                item['pool'] = ['--']
            else:
                item['pool'] = json.dumps(
                    item['allocation_pools'],
                    indent=2
                ).split('\n')

        order = []
        headers = []
        if select:
            order.append('__id')
            headers.append('Index')

        order = order + [
            'extended_name',
            'cidr',
            'gateway_ip',
            'dhcpTick',
            'pool',
            'dns_nameservers',
            'created_age'
        ]

        headers = headers + [
            'Subnet',
            'CIDR',
            'Gateway',
            'DHCP',
            'Pool',
            'DNS',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['extended_name', 'pool', 'dns_nameservers']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_subnets_port(self, info, title=False):
        if title:
            self.my_output.default(
                'Subnet - Port [#%s]' % (len(info)),
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
            'cidr',
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
                ['port_info']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_subnets_id(self, info, title=False):
        if title:
            self.my_output.default(
                'Subnet - Identifier [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'id',
            'name',
            'tenant_id'
        ]

        headers = [
            'Id',
            'Name',
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

    def select_subnet(self, info):
        self.my_output.default(
            'Select subnet [#%s]' % (len(info)),
            underline=True,
            before_newline=True
        )

        if len(info) == 0:
            self.my_output.default('No subnet found')
            return None

        new_info = copy.deepcopy(info)

        index = 1
        for item in new_info:
            item['__id'] = index
            index = index + 1

        self.print_subnets(new_info, title=False, select=True)

        while True:
            answer = input("Select subnet using index value (0 to break): ")
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
