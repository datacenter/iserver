class RedfishEndpointUcsRackTemplateGpuOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_gpu_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'GPU [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')

        order = [
            'Id',
            'Name',
            'Model',
            'SerialNumber',
            'FirmwareVersion'
        ]

        headers = [
            'Id',
            'Name',
            'Model',
            'SerialNumber',
            'FirmwareVersion'
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
