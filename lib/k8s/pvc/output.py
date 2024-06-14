class K8sPvcOutput():
    def __init__(self):
        pass

    def print_pvcs(self, info, title=False):
        if title:
            self.my_output.default(
                'PVC [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        row_separator = False
        usage_info = False
        for item in info:
            if 'usage_pod' in item:
                usage_info = True
            if len(item['access_modes']) > 1:
                row_separator = True

        order = [
            'namespace',
            'name',
            'phase',
            'volume_name',
            'capacity.storage',
            'access_modes',
            'storage_class_name',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Status',
            'Volume',
            'Size',
            'Access Mode',
            'Storage Class',
            'Age'
        ]

        if usage_info:
            order.append('usedTick')
            headers.append('Used (Pod/VMI)')

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['access_modes']
            ),
            order=order,
            headers=headers,
            row_separator=row_separator,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_pvcs_with_usage(self, info, title=False):
        if title:
            self.my_output.default(
                'PVC [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        row_separator = False
        for item in info:
            if len(item['access_modes']) > 1:
                row_separator = True

        for item in info:
            if item['owner'] is None:
                item['ownerT'] = ['--']
            else:
                item['ownerT'] = item['owner'].split('/')

        order = [
            'namespace',
            'name',
            'phase',
            'volume_name',
            'capacity.storage',
            'access_modes',
            'storage_class_name',
            'usedTick',
            'ownerT',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Status',
            'Volume',
            'Size',
            'Access Mode',
            'Storage Class',
            'Usage',
            'Owner',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['access_modes', 'ownerT']
            ),
            order=order,
            headers=headers,
            row_separator=row_separator,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_pvcs_metadata(self, info, title=False):
        if title:
            self.my_output.default(
                'PVC - Metadata [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        info = self.add_namespace_name(info)
        for item in info:
            if item['owner'] is None:
                item['ownerT'] = ['--']
            else:
                item['ownerT'] = item['owner'].split('/')

        order = [
            'namespace_nameT',
            'ownerT',
            'labelT',
            'annotationT'
        ]

        headers = [
            'Name',
            'Owner',
            'Label',
            'Annotation'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['namespace_nameT', 'labelT', 'annotationT', 'ownerT']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_pvcs_pv(self, info, title=False):
        if title:
            self.my_output.default(
                'PVC - Volume [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace',
            'name',
            'volume_name',
            'volume_phase',
            'volume_mode',
            'storage_class_name',
            'storage_provisioner',
            'selected_node'
        ]

        headers = [
            'Namespace',
            'Name',
            'Volume',
            'Status',
            'Mode',
            'Storage Class',
            'Storege Type',
            'Storage Node'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            row_separator=False,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def print_pvcs_usage(self, info, title=False):
        if title:
            self.my_output.default(
                'PVC - Usage [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            if len(item['usage_pod']) == 0:
                item['usage_pod'].append('--')

            if len(item['usage_vmi']) == 0:
                item['usage_vmi'].append('--')

        order = [
            'namespace_name',
            'usedTick',
            'usage_pod',
            'usage_vmi'
        ]

        headers = [
            'PVC',
            'Used',
            'Pod',
            'VMI'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['usage_pod', 'usage_vmi']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
