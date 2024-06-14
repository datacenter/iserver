import copy


class OspImageOutput():
    def __init__(self):
        pass

    def print_images(self, info, title=False, select=False):
        if title:
            self.my_output.default(
                'Image [#%s]' % (len(info)),
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
            'disk_format',
            'container_format',
            'sizeT',
            'status',
            'visibility',
            'protectedTick',
            'checksum'
        ]

        headers = headers + [
            'Name',
            'Disk',
            'Container',
            'Size [B]',
            'Status',
            'Visibility',
            'Protected',
            'Checksum'
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

    def print_images_id(self, info, title=False):
        if title:
            self.my_output.default(
                'Image - Identifiers [#%s]' % (len(info)),
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

    def print_images_vm(self, info, title=False):
        if title:
            self.my_output.default(
                'Image - Virtual Machine [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name',
            'disk_format',
            'container_format',
            'sizeT',
            'status',
            'vm.tenant_name'
        ]

        headers = [
            'Name',
            'Disk',
            'Container',
            'Size [B]',
            'Status',
            'Virtual Machine'
        ]

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

    def select_image(self, info):
        self.my_output.default(
            'Select Image [#%s]' % (len(info)),
            underline=True,
            before_newline=True
        )

        if len(info) == 0:
            self.my_output.default('No image found')
            return None

        new_info = copy.deepcopy(info)

        index = 1
        for item in new_info:
            item['__id'] = index
            index = index + 1

        self.print_images(new_info, title=False, select=True)

        while True:
            answer = input("Select image using index value (0 to break): ")
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
