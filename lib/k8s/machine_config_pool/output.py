import json


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

    def print_machine_config_pools_selector(self, info, title=False):
        if title:
            self.my_output.default(
                'Machine Config Pool (MCP) Selector [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['machine_config_selectorT'] = json.dumps(item['machine_config_selector'], indent=4).split('\n')
            item['node_selectorT'] = json.dumps(item['node_selector'], indent=4).split('\n')
            if len(item['candidate_machine_configs']) == 0:
                item['candidate_machine_configs'].append('--')
            if len(item['candidate_nodes']) == 0:
                item['candidate_nodes'].append('--')

        order = [
            'name',
            'machine_config_selectorT',
            'candidate_machine_configs',
            'node_selectorT',
            'candidate_nodes'
        ]

        headers = [
            'Name',
            'Machine Config Selector',
            'Candidate Machine Configs',
            'Node Selector',
            'Candidate Nodes'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['machine_config_selectorT', 'node_selectorT', 'candidate_machine_configs', 'candidate_nodes']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
