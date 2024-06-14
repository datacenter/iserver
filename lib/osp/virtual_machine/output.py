import copy


class OspVirtualMachineOutput():
    def __init__(self):
        pass

    def print_virtual_machines(self, info, title=False):
        if title:
            self.my_output.default(
                'Virtual Machine [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = copy.deepcopy(info)
        for item in new_info:
            item['task_stateT'] = item['task_state']
            if item['task_state'] is None:
                item['task_stateT'] = '--'

        order = [
            'tenant_name',
            'name',
            'hypervisor',
            'status',
            'power_state',
            'task_stateT',
            'bootSourceT',
            'flavor_info.name',
            'flavor_info.resource',
            'age'
        ]

        headers = [
            'Tenant',
            'VM',
            'Hypervisor',
            'Status',
            'Power',
            'Task',
            'Boot Source',
            'Flavor',
            'Resource',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['interface']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_virtual_machines_console(self, info, title=False):
        if title:
            self.my_output.default(
                'Virtual Machine Console [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'tenant_name',
            'name',
            'console'
        ]

        headers = [
            'Tenant',
            'VM',
            'Console'
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

    def print_virtual_machines_logs(self, info):
        for item in info:
            self.my_output.default(
                'Virtual Machine Logs: %s/%s ' % (
                    item['tenant_name'],
                    item['name']
                ),
                underline=True,
                before_newline=True,
                after_newline=True
            )

            self.my_output.default(item['logs'])

    def print_virtual_machines_id(self, info, title=False):
        if title:
            self.my_output.default(
                'Virtual Machine - Identifier [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'tenant_name',
            'name',
            'id',
            'image.id',
            'flavor.id'
        ]

        headers = [
            'Tenant',
            'VM',
            'Id',
            'Image',
            'Flavor'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['interface']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_virtual_machines_net(self, info, title=False):
        if title:
            self.my_output.default(
                'Virtual Machine - Networking [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'tenant_name',
            'name',
            'interface.network',
            'interface.mac',
            'interface.ip_type',
            'interface.subnet'
        ]

        headers = [
            'Tenant',
            'VM',
            'Network',
            'MAC',
            'IP',
            'Subnet'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['interface']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_virtual_machines_sec(self, info, title=False):
        if title:
            self.my_output.default(
                'Virtual Machine - Security [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'tenant_name',
            'name',
            'interface.network',
            'interface.mac',
            'interface.ip_type',
            'interface.subnet',
            'interface.port_info.port_security_enabledTick',
            'interface.port_info.security_group_names_value'
        ]

        headers = [
            'Tenant',
            'VM',
            'Network',
            'MAC',
            'IP',
            'Subnet',
            'Port Security',
            'Security Group'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['interface']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def select_virtual_machine(self, info):
        self.my_output.default(
            'Select Virtual Machine [#%s]' % (len(info)),
            underline=True,
            before_newline=True
        )

        if len(info) == 0:
            self.my_output.default('No virtual machine found')
            return None

        new_info = copy.deepcopy(info)

        index = 1
        for item in new_info:
            item['__id'] = index
            index = index + 1
            if item['bootSource'] is None:
                item['bootSource'] = '--'

        order = [
            '__id',
            'tenant_name',
            'name',
            'status',
            'bootFrom',
            'bootSource',
            'flavor_info.name',
            'flavor_info.resource',
            'interface.network',
            'interface.mac',
            'interface.ip_type',
            'interface.subnet'
        ]

        headers = [
            'Index',
            'Tenant',
            'VM',
            'Status',
            'Boot From',
            'Boot Source',
            'Flavor',
            'Resource',
            'Network',
            'MAC',
            'IP',
            'Subnet'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['interface']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

        while True:
            answer = input("Select virtual machine using index value (0 to break): ")
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
