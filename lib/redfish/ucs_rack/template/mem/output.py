class RedfishEndpointUcsRackTemplateMemOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_mem_properties(self, info, show_absent=False):
        items = []
        for item in info:
            if show_absent or item['State'] != 'Absent':
                items.append(
                    item
                )
        self.my_output.my_table_ng(
            items,
            [
                ['Memory Id', 'Id'],
                ['Health', 'Health'],
                ['State', 'State'],
                ['Locator', 'DeviceLocator'],
                ['CapacityMiB', 'CapacityMiB'],
                ['Speed [Mhz]', 'OperatingSpeedMhz'],
                ['Socket', 'Socket'],
                ['Channel', 'Channel'],
                ['Type', 'MemoryType'],
                ['Device Type', 'MemoryDeviceType'],
                ['Part Number', 'PartNumber'],
                ['Serial Number', 'SerialNumber']
            ]
        )
