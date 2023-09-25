class KubevirtVirtualMachineOutput():
    def __init__(self):
        pass

    def print_virtual_machines(self, info, title=False):
        if title:
            self.my_output.default(
                'Kubevirt Virtual Machine [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name',
            'special',
            'cpu.cores',
            'memory',
            'disks.volume.info',
            'interfaces.name',
            'interfaces.mac_address',
            'interfaces.masqueradeTick',
            'interfaces.sriovTick',
            'interfaces.multusTick',
            'interfaces.multusNetworkName',
            'state',
            'readyTick',
            'failures',
            'liveMigrationTick'
        ]

        headers = [
            'VM',
            'Special',
            'CPU',
            'Memory',
            'Disks',
            'Interfaces',
            'MAC',
            'Masq',
            'SRIOV',
            'Multus',
            'Network',
            'State',
            'Ready',
            'Failure',
            'LM'
        ]

        for item in info:
            if len(item['failures']) == 0:
                item['failures'].append('--')

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['disks', 'interfaces', 'failures']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            remove_empty_columns=False,
            table=True
        )
