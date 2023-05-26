import copy


class TabooOutput():
    def __init__(self):
        pass

    def print_taboos(self, info, show_taboo_filters=False):
        self.my_output.default(
            'Taboo Contracts',
            underline=True,
            before_newline=True
        )

        order = [
            'nameTenant',
            'vzFilter.subjectNameTenant',
            'vzFilter.nameTenant'
        ]

        headers = [
            'Taboo',
            'Subject',
            'Filter'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['vzFilter']
            ),
            order=order,
            headers=headers,
            underline=True,
            row_separator=True,
            allow_order_subkeys=True,
            table=True
        )

        if show_taboo_filters:
            filters_in_the_list = []
            filters = []
            for taboo in info:
                for item in taboo['vzFilter']:
                    if item['nameTenant'] not in filters_in_the_list:
                        filters_in_the_list.append(
                            item['nameTenant']
                        )
                        new_entry = copy.deepcopy(item)
                        filters.append(new_entry)

            self.print_filters(
                filters
            )

    def print_taboos_usage(self, info):
        self.my_output.default(
            'Taboo Contracts Usage',
            underline=True,
            before_newline=True
        )

        order = [
            'nameTenant',
            'protectedEpg.nameLong'
        ]

        headers = [
            'Taboo',
            'Protected EPG'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['protectedEpg']
            ),
            order=order,
            headers=headers,
            underline=True,
            row_separator=True,
            allow_order_subkeys=True,
            table=True
        )
