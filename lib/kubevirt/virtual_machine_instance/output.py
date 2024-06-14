class KubevirtVirtualMachineInstanceOutput():
    def __init__(self):
        pass

    def print_virtual_machine_instances(self, info, title=False):
        if title:
            self.my_output.default(
                'Kubevirt Virtual Machine Instance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name',
            'node_name',
            'state_transitions.phase',
            'state_transitions.phase_transition_timestamp',
            'interfaces.name',
            'interfaces.mac',
            'interfaces.ip_address',
            'interfaces.masqueradeTick',
            'interfaces.sriovTick',
            'interfaces.multusTick',
            'interfaces.multusNetworkName',
            'volume_status.info',
            'volume_status.target',
            'volume_status.storage',
            'age'
        ]

        headers = [
            'VM',
            'Node',
            'Phase',
            'Timestamp',
            'Interface',
            'MAC',
            'IP',
            'Masq',
            'SRIOV',
            'Multus',
            'Network',
            'Volume',
            'Target',
            'Size',
            'Age'
        ]

        for item in info:
            for interface in item['interfaces']:
                if interface['ip_address'] is None:
                    interface['ip_address'] = '--'

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['volume_status', 'interfaces', 'state_transitions']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            remove_empty_columns=False,
            table=True
        )
