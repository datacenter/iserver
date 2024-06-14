class RedfishEndpointUcsRackTemplateNetOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_net_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'Net [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'Id',
            'Name',
            'PermanentMACAddress',
            'MACAddress'
        ]

        headers = [
            'Id',
            'Name',
            'BIA',
            'MAC'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            row_separator=True,
            table=True
        )
