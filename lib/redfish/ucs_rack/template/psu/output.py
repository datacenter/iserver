class RedfishEndpointUcsRackTemplatePsuOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_psu_properties(self, info, title=False):
        if title:
            self.my_output.default(
                'PSU [#%s]' % (len(info)),
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
            'Manufacturer',
            'Model',
            'PartNumber',
            'SerialNumber',
            'SparePartNumber',
            'FirmwareVersion'
        ]

        headers = [
            'Id',
            'Name',
            'State',
            'Vendor',
            'Model',
            'Part Number',
            'Serial Number',
            'Spare Part Number',
            'Firmware'
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
