class K8sNodeOutput():
    def __init__(self):
        pass

    def print_nodes_state(self, info, title=False):
        if title:
            self.my_output.default(
                'Node - State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'readyTick',
            'memoryTick',
            'diskTick',
            'pidTick',
            'cnvTick',
            'mcpTick',
            'role',
            'ipT',
            'age'
        ]

        headers = [
            'Name',
            'Ready',
            'Memory',
            'Disk',
            'PID',
            'CNV',
            'MCP',
            'Role',
            'IP',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['ipT', 'role']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_nodes_version(self, info, title=False):
        if title:
            self.my_output.default(
                'Node - Versions [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'node_info.kubelet_version',
            'node_info.os_image',
            'node_info.kernel_version',
            'node_info.container_runtime_version'
        ]

        headers = [
            'Name',
            'Version',
            'OS Image',
            'Kernel Version',
            'Container Runtime'
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

    def print_nodes_capacity(self, info, title=False):
        if title:
            self.my_output.default(
                'Node - Capacity [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'capacity_pod',
            'capacity_cpu',
            'capacity_memory',
            'capacity_storage',
            'capacity_hp2m',
            'capacity_hp1g',
            'capacity_kubevirt',
            'capacity_vendor'
        ]

        headers = [
            'Name',
            'POD',
            'CPU',
            'Memory',
            'Storage',
            'HP 2Mi',
            'HP 1Gi',
            'Kubevirt',
            'Vendor'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['capacity_vendor', 'capacity_kubevirt']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_nodes_label(self, info, title=False):
        if title:
            self.my_output.default(
                'Node - Label [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            item['labelT'] = []
            for key in item['label']:
                label_info = {}
                label_info['key'] = key
                label_info['value'] = item['label'][key]
                if label_info['value'] == '':
                    label_info['value'] = '--'

                item['labelT'].append(
                    label_info
                )

        order = [
            'name',
            'labelT.key',
            'labelT.value'
        ]

        headers = [
            'Name',
            'Label Key',
            'Label Value'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['labelT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )
