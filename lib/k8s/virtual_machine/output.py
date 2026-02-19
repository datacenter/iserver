class K8sVirtualMachineOutput():
    def __init__(self):
        pass

    def print_virtual_machines(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Virtual Machine', 'namespace_nameT'],
                ['CPU', 'cpu'],
                ['Memory', 'memory'],
                ['Disk', 'disk.info'],
                ['Interface', 'interface.info'],
                ['Status', 'status'],
                ['Restart Reqd', 'restartRequiredTick'],
                ['Age', 'age']
            ]
        )

    def print_virtual_machines_metadata(self, info, title=False):
        if title:
            self.my_output.default(
                'Virtual Machine - Metadata [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            if item['owner'] is None:
                item['ownerT'] = ['--']
            else:
                item['ownerT'] = item['owner'].split('/')

        order = [
            'namespace_name',
            'ownerT',
            'labelT',
            'annotationT'
        ]

        headers = [
            'VM',
            'Owner',
            'Label',
            'Annotation'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['annotationT', 'labelT', 'ownerT']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_virtual_machines_dv(self, info, title=False):
        if title:
            self.my_output.default(
                'Virtual Machine - Data Volume [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            for dv_item in item['dv']:
                dv_item['namespace_name'] = '%s/%s' % (
                    dv_item['namespace'],
                    dv_item['name']
                )

        order = [
            'namespace_name',
            'disk.info',
            'dv.namespace_name',
            'dv.storage',
            'dv.source'
        ]

        headers = [
            'VM',
            'Disks',
            'DV Name',
            'DV Storage',
            'DV Source'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['disk', 'dv']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
