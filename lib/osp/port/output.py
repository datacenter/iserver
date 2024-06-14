import copy
import json


class OspPortOutput():
    def __init__(self):
        pass

    def print_ports(self, info, title=False, select=False):
        if title:
            self.my_output.default(
                'Port [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = copy.deepcopy(info)
        for item in new_info:
            if item['name'] is None or len(item['name']) == 0:
                item['name'] = '--'

            if item['type'] is None:
                item['type'] = '--'

            if item['tenant_name'] is None:
                item['tenant_name'] = '--'

            if item['network_name'] is None:
                item['network_name'] = '--'

            for fip in item['fixed_ips']:
                if fip['subnet_name'] is None:
                    fip['subnet_name'] = '--'

                if 'floating_ip' not in fip or fip['floating_ip'] is None:
                    fip['floating_ip'] = '--'

        order = []
        headers = []
        if select:
            order.append('__id')
            headers.append('Index')

        order = order + [
            'mac_address',
            'adminTick',
            'statusT',
            'type',
            'name',
            'fixed_ips.ip_address',
            'fixed_ips.floating_ip',
            'fixed_ips.subnet_name',
            'network_name',
            'tenant_name',
            'age'
        ]

        headers = headers + [
            'MAC',
            'Admin',
            'Status',
            'Type',
            'Name',
            'IP',
            'Floating IP',
            'Subnet',
            'Network',
            'Tenant',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['fixed_ips']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_ports_security(self, info, title=False):
        if title:
            self.my_output.default(
                'Port - Security [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = copy.deepcopy(info)
        for item in new_info:
            if item['type'] is None:
                item['type'] = '--'

            if item['vm_tenant_name'] is None:
                item['vm_tenant_name'] = '--'

            if len(item['allowed_address_pairs']) == 0:
                item['aap'] = []
            else:
                item['aap'] = json.dumps(
                    item['allowed_address_pairs'],
                    indent=2
                ).split('\n')

            if len(item['security_group_names']) == 0:
                item['security_group_names'].append('--')

        order = [
            'mac_address',
            'adminTick',
            'statusT',
            'type',
            'fixed_ips.ip_address',
            'vm_tenant_name',
            'aap',
            'port_security_enabledTick',
            'security_group_names'
        ]

        headers = [
            'MAC',
            'Admin',
            'Status',
            'Type',
            'IP',
            'VM',
            'Allowed Access Pairs',
            'Port Security',
            'Security Group'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['fixed_ips', 'aap', 'security_group_names']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_ports_hv(self, info, title=False):
        if title:
            self.my_output.default(
                'Port - Hypervisor [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = copy.deepcopy(info)
        for item in new_info:
            if item['type'] is None:
                item['type'] = '--'

            if item['vm_tenant_name'] is None:
                item['vm_tenant_name'] = '--'

            if item['binding_host_id'] is None or len(item['binding_host_id']) == 0:
                item['binding_host_id'] = '--'

            if len(item['binding_profile']) == 0:
                item['binding_profileT'] = ['--']
            else:
                item['binding_profileT'] = json.dumps(
                    item['binding_profile'],
                    indent=2
                ).split('\n')

            if len(item['binding_vif_details']) == 0:
                item['binding_vif_detailsT'] = ['--']
            else:
                item['binding_vif_detailsT'] = json.dumps(
                    item['binding_vif_details'],
                    indent=2
                ).split('\n')

        order = [
            'mac_address',
            'adminTick',
            'statusT',
            'type',
            'fixed_ips.ip_address',
            'vm_tenant_name',
            'binding_vnic_type',
            'binding_profileT',
            'binding_host_id',
            'binding_vif_type',
            'binding_vif_detailsT'
        ]

        headers = [
            'MAC',
            'Admin',
            'Status',
            'Type',
            'IP',
            'VM',
            'VNIC',
            'Profile',
            'Host',
            'Type',
            'Details'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['fixed_ips', 'binding_profileT', 'binding_vif_detailsT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_ports_id(self, info, title=False):
        if title:
            self.my_output.default(
                'Port - Identifier [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = copy.deepcopy(info)
        for item in new_info:
            item['itnd'] = []
            item['itnd'].append(
                'MAC: %s' % (item['mac_address'])
            )
            item['itnd'].append(
                'ID: %s' % (item['id'])
            )
            item['itnd'].append(
                'Tenant: %s' % (item['tenant_id'])
            )
            item['itnd'].append(
                'Network: %s' % (item['network_id'])
            )
            item['itnd'].append(
                'Device: %s' % (item['device_id'])
            )
        order = [
            'itnd',
            'fixed_ips.subnet_id',
            'security_groups'
        ]

        headers = [
            'Base',
            'Subnet',
            'Security Group'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['fixed_ips', 'itnd', 'security_groups']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def select_port(self, info):
        self.my_output.default(
            'Select Port [#%s]' % (len(info)),
            underline=True,
            before_newline=True
        )

        if len(info) == 0:
            self.my_output.default('No port found')
            return None

        new_info = copy.deepcopy(info)

        index = 1
        for item in new_info:
            item['__id'] = index
            index = index + 1

        self.print_ports(new_info, title=False, select=True)

        while True:
            answer = input("Select port using index value (0 to break): ")
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
