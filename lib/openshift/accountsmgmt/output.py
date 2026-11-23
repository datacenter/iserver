import json


class AccountsManagementOutput():
    def __init__(self):
        pass

    def print_accounts_management_subscription(self, info, title=False):
        if title:
            self.my_output.default(
                'Accounts Management - Subscription [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'name'
        ]

        headers = [
            'Name'
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
