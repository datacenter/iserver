class ApplicationProfileOutput():
    def __init__(self):
        pass

    def print_application_profiles(self, application_profiles):
        order = [
            'nameTenant',
            'epgs.nameTenant',
            'prio'
        ]

        headers = [
            'Application Profile',
            'Application EPGs',
            'Priority'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                application_profiles,
                order,
                ['epgs']
            ),
            order=order,
            headers=headers,
            row_separator=True,
            allow_order_subkeys=True,
            underline=True,
            table=True
        )
