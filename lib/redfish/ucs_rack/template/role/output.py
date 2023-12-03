class RedfishEndpointUcsRackTemplateRoleOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_role_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'Role [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')

        for item in info:
            if len(item['privileges']) == 0:
                item['privileges'].append('--')
            if len(item['oem']) == 0:
                item['oem'].append('--')
            if len(item['username']) == 0:
                item['username'].append('--')

        order = [
            'id',
            'role_id',
            'name',
            'description',
            'privileges',
            'oem',
            'username'
        ]

        headers = [
            'Id',
            'Role Id',
            'Name',
            'Description',
            'Privileges',
            'Oem Privileges',
            'Account'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['privileges', 'oem', 'username']
            ),
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            row_separator=True,
            table=True
        )
