class K8sTunedOutput():
    def __init__(self):
        pass

    def print_tuneds(self, info, title=False):
        if title:
            self.my_output.default(
                'Tuned [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        info = self.my_output.prepare_list(
            info,
            empty=['owner']
        )

        order = [
            'namespace',
            'name',
            'owner',
            'profile_names',
            'age'
        ]

        headers = [
            'Namespace',
            'Name',
            'Owner',
            'Profile',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['profile_names']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
