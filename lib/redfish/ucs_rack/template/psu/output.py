class RedfishEndpointUcsRackTemplatePsuOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_psu_properties(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['PSU Id', 'MemberId'],
                ['Name', 'Name'],
                ['State', 'State'],
                ['Vendor', 'Manufacturer'],
                ['Model', 'Model'],
                ['Part Number', 'PartNumber'],
                ['Serial Number', 'SerialNumber'],
                ['Spare Part Number', 'SparePartNumber'],
                ['Firmware', 'FirmwareVersion']
            ]
        )
