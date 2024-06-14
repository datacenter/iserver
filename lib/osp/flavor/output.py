import copy


class OspFlavorOutput():
    def __init__(self):
        pass

    def print_flavors(self, info, title=False, select=False):
        if title:
            self.my_output.default(
                'Flavor [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = []
        headers = []
        if select:
            order.append('__id')
            headers.append('Index')

        order = order + [
            'name',
            'enabledTick',
            'publicTick',
            'vcpus',
            'ram',
            'disk',
            'ephemeral'
        ]

        headers = headers + [
            'Name',
            'Enabled',
            'Pub',
            'CPU',
            'Mem [MB]',
            'Disk [GB]',
            'Eph [GB]'
        ]

        if 'keys' in info[0]:
            order.append('keysT')
            headers.append('Keys')

            for item in info:
                item['keysT'] = []
                for key in item['keys']:
                    item['keysT'].append(
                        '%s = %s' % (
                            key,
                            item['keys'][key]
                        )
                    )
                if len(item['keysT']) == 0:
                    item['keysT'].append('--')

            self.my_output.my_table(
                self.my_output.expand_lists(
                    info,
                    order,
                    ['keysT']
                ),
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                underline=True,
                row_separator=True,
                table=True
            )
        else:
            self.my_output.my_table(
                info,
                order=order,
                headers=headers,
                allow_order_subkeys=True,
                underline=True,
                row_separator=False,
                table=True
            )

    def print_flavors_id(self, info, title=False):
        if title:
            self.my_output.default(
                'Flavor - Identifiers [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'id',
            'name'
        ]

        headers = [
            'Id',
            'Name'
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

    def print_flavors_vm(self, info, title=False):
        if title:
            self.my_output.default(
                'Flavor - Virtual Machine Usage [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'vcpus',
            'ram',
            'disk',
            'ephemeral',
            'vm.tenant_name'
        ]

        headers = [
            'Name',
            'CPU',
            'Mem [MB]',
            'Disk [GB]',
            'Eph [GB]',
            'VM'
        ]

        for item in info:
            if len(item['vm']) == 0:
                item['vm'].append(dict(tenant_name='--'))

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['vm']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def select_flavor(self, info):
        self.my_output.default(
            'Select Flavor [#%s]' % (len(info)),
            underline=True,
            before_newline=True
        )

        if len(info) == 0:
            self.my_output.default('No flavor found')
            return None

        new_info = copy.deepcopy(info)

        index = 1
        for item in new_info:
            item['__id'] = index
            index = index + 1

        self.print_flavors(new_info, title=False, select=True)

        while True:
            answer = input("Select flavor using index value (0 to break): ")
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
