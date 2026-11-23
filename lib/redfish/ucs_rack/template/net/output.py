class RedfishEndpointUcsRackTemplateNetOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_net_properties(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Net Id', 'Id'],
                ['Name', 'Name'],
                ['BIA', 'PermanentMACAddress'],
                ['MAC', 'MACAddress']
            ]
        )
