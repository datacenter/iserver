class K8sMachineConfigPoolOutput():
    def __init__(self):
        pass

    def print_machine_config_pools(self, info, title=False):
        if title:
            self.my_output.default(
                'Machine Config Pool (MCP) [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'current_configuration',
            'updatedTick',
            'updatingTick',
            'degradedTick',
            'machineCount',
            'readyMachineCount',
            'updatedMachineCount',
            'degradedMachineCount',
            'unavailableMachineCount',
            'source.name',
            'age'
        ]

        headers = [
            'Name',
            'Config',
            'Updated',
            'Updating',
            'Degraded',
            'Machines',
            'Ready',
            'Updated',
            'Degraded',
            'Unavail',
            'Machine Config',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['source']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
