import copy


class OspUserOutput():
    def __init__(self):
        pass

    def print_users(self, info, title=False):
        if title:
            self.my_output.default(
                'User [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = copy.deepcopy(info)
        for item in new_info:
            if item['default_project_name'] is None:
                item['default_project_name'] = '--'

        order = [
            'id',
            'name',
            'enabledTick',
            'expiresTick',
            'domain_id',
            'default_project_name'
        ]

        headers = [
            'Id',
            'Name',
            'Enabled',
            'Expiry',
            'Domain',
            'Default Project'
        ]

        self.my_output.my_table(
            new_info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )
