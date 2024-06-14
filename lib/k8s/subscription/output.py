class K8sSubscriptionOutput():
    def __init__(self):
        pass

    def print_subscriptions(self, info, title=False):
        if title:
            self.my_output.default(
                'Subscription - State [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace',
            'name',
            'package',
            'source',
            'channelT',
            'install_plan',
            'installed_csv',
            'csvTick',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Package',
            'Source',
            'Channel',
            'Install',
            'CSV',
            'Latest',
            'Age'
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
