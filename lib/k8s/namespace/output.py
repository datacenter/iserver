import copy


class K8sNamespaceOutput():
    def __init__(self):
        pass

    def print_namespaces_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Namespace', 'name'],
                ['Status', 'phase'],
                ['Age', 'age']
            ]
        )

    def print_namespaces_udn(self, info):
        items = []
        for item in info:
            if item['udn']:
                items.append(item)

        self.my_output.my_table_ng(
            items,
            [
                ['Namespace', 'name'],
                ['Status', 'phase'],
                ['Age', 'age']
            ]
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

        self.print_namespaces_state(new_info, title=False, select=True)

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
