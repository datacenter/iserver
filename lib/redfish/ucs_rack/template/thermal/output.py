class RedfishEndpointUcsRackTemplateThermalOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_thermal_summary_properties(self, properties):
        keys = [
            'SensorHealth',
            'HighestTemperature',
            'SmallestGap',
            'OverThreshold',
            'FanHealth'
        ]

        headers = [
            'Sensors Health',
            'Highest (C)',
            'Smallest Gap (C)',
            'Over Threshold',
            'Fans Health'
        ]

        self.my_output.dictionary(
            properties['Summary'],
            title='Thermal Summary',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_ucsc_thermal_properties(self, properties):
        self.print_ucsc_thermal_summary_properties(properties)

        self.my_output.my_table_ng(
            properties['Data']['Temperature'],
            [
                ['Sensor Name', 'Name'],
                ['State', 'State'],
                ['Health', 'Health'],
                ['Location', 'PhysicalContext'],
                ['Value (Celcius)', 'ReadingCelsius'],
                ['Upper Threshold (Celcius)', 'UpperThresholdCritical']
            ]
        )

        self.my_output.my_table_ng(
            properties['Data']['Fan'],
            [
                ['Fan Name', 'Name'],
                ['State', 'State'],
                ['Health', 'Health'],
                ['Value', 'Value']
            ]
        )
