class RedfishEndpointUcsRackTemplateAccountOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_account_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'Account [#%s]' % (len(info)),
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

        order = [
            'username',
            'id',
            'role_id',
            'name',
            'description',
            'enabledTick',
            'changeTick',
            'privileges',
            'oem'
        ]

        headers = [
            'Username',
            'Id',
            'Role Id',
            'Name',
            'Description',
            'Enabled',
            'Change Req',
            'Role Privileges',
            'Role Oem Privileges'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['privileges', 'oem']
            ),
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            row_separator=True,
            table=True
        )
