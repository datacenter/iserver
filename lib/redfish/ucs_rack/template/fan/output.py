class RedfishEndpointUcsRackTemplateFanOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_fan_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'Fan [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'MemberId',
            'Name',
            'State',
            'Health',
            'Reading',
            'ReadingUnits'

        ]

        headers = [
            'Id',
            'Name',
            'State',
            'Health',
            'Reading',
            'Units'
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
