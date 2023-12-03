import copy


class OspSecurityGroupOutput():
    def __init__(self):
        pass

    def print_security_groups(self, info, title=False):
        if title:
            self.my_output.default(
                'Security Group [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = copy.deepcopy(info)
        for item in new_info:
            if item['tenant_name'] is None or len(item['tenant_name']) == 0:
                item['tenant_name'] = '--'

        order = [
            'tenant_name',
            'name',
            'rule_count',
            'create_age',
            'update_age'
        ]

        headers = [
            'Tenant',
            'Name',
            'Rule Count',
            'Create',
            'Update'
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

    def print_security_groups_rule(self, info, title=False):
        if title:
            self.my_output.default(
                'Security Group - Rule [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = copy.deepcopy(info)
        for item in new_info:
            if item['tenant_name'] is None or len(item['tenant_name']) == 0:
                item['tenant_name'] = '--'

            for rule in item['rule']:
                if rule['protocol'] is None:
                    rule['protocol'] = '--'

                if rule['port_range'] is None:
                    rule['port_range'] = '--'

                if rule['remote_ip_prefix'] is None:
                    rule['remote_ip_prefix'] = '--'

                if rule['remote_group_name'] is None:
                    rule['remote_group_name'] = '--'

        order = [
            'tenant_name',
            'name',
            'rule.ethertype',
            'rule.direction',
            'rule.protocol',
            'rule.port_range',
            'rule.remote_ip_prefix',
            'rule.remote_group_name',
            'rule.create_age',
            'rule.update_age'
        ]

        headers = [
            'Tenant',
            'Name',
            'EtherType',
            'Direction',
            'Protocol',
            'Port Range',
            'Remote Prefix',
            'Remote Group',
            'Create',
            'Update'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['rule']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_security_groups_port(self, info, title=False):
        if title:
            self.my_output.default(
                'Security Group - Port and Rule [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = copy.deepcopy(info)
        for item in new_info:
            if item['tenant_name'] is None or len(item['tenant_name']) == 0:
                item['tenant_name'] = '--'

            for rule in item['rule']:
                if rule['protocol'] is None:
                    rule['protocol'] = '--'

                if rule['port_range'] is None:
                    rule['port_range'] = '--'

                if rule['remote_ip_prefix'] is None:
                    rule['remote_ip_prefix'] = '--'

                if rule['remote_group_name'] is None:
                    rule['remote_group_name'] = '--'

            for port in item['port']:
                if port['vm_tenant_name'] is None:
                    port['vm_tenant_name'] = '--'

        order = [
            'tenant_name',
            'name',
            'port.mac_address',
            'port.vm_tenant_name',
            'rule.ethertype',
            'rule.direction',
            'rule.protocol',
            'rule.port_range',
            'rule.remote_ip_prefix',
            'rule.remote_group_name'
        ]

        headers = [
            'Tenant',
            'Name',
            'MAC',
            'VM',
            'EtherType',
            'Direction',
            'Protocol',
            'Port Range',
            'Remote Prefix',
            'Remote Group'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['port', 'rule']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_security_groups_id(self, info, title=False):
        if title:
            self.my_output.default(
                'Security Group - Identifier [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'tenant_id',
            'rule.id'
        ]

        headers = [
            'Name',
            'Tenant',
            'Rule'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['rule']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
