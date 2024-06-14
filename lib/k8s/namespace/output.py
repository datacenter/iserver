import copy


class K8sNamespaceOutput():
    def __init__(self):
        pass

    def print_namespaces(self, info, title=False, select=False):
        if title:
            self.my_output.default(
                'Namespace [#%s]' % (len(info)),
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
            'phase',
            'age'
        ]

        headers = headers + [
            'Name',
            'Status',
            'Age'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )

    def select_namespace(self, info):
        self.my_output.default(
            'Select Namespace [#%s]' % (len(info)),
            underline=True,
            before_newline=True
        )

        if len(info) == 0:
            self.my_output.default('No namespace found')
            return None

        new_info = copy.deepcopy(info)

        index = 1
        for item in new_info:
            item['__id'] = index
            index = index + 1

        self.print_namespaces(new_info, title=False, select=True)

        while True:
            answer = input("Select namespace using index value (0 to break): ")
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
