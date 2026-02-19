class RedfishEndpointUcsRackTemplateFanOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_fan_properties(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Id', 'MemberId'],
                ['Name', 'Name'],
                ['State', 'State'],
                ['Health', 'Health'],
                ['Reading', 'Reading'],
                ['Units', 'ReadingUnits']
            ]
        )
