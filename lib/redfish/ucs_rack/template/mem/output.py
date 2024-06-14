class RedfishEndpointUcsRackTemplateMemOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_mem_properties(self, info, title=False, show_absent=False):
        items = []
        for item in info:
            if show_absent or item['State'] != 'Absent':
                items.append(
                    item
                )

        if title:
            self.my_output.default(
                'Memory [#%s]' % (len(items)),
                underline=True,
                before_newline=True
            )

        if len(items) == 0:
            self.my_output.default('None')
            return

        order = [
            'Id',
            'Health',
            'State',
            'DeviceLocator',
            'CapacityMiB',
            'OperatingSpeedMhz',
            'Socket',
            'Slot',
            'Channel',
            'MemoryType',
            'MemoryDeviceType',
            'PartNumber',
            'SerialNumber'
        ]

        headers = [
            'Id',
            'Health',
            'State',
            'Locator',
            'CapacityMiB',
            'Speed [Mhz]',
            'Socket',
            'Slot',
            'Channel',
            'Type',
            'Device Type',
            'Part Number',
            'Serial Number'
        ]

        self.my_output.my_table(
            items,
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            row_separator=True,
            table=True
        )
