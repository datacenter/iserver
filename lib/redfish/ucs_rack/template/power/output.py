class RedfishEndpointUcsRackTemplatePowerOutput(
    ):
    def __init__(self):
        pass

    def print_ucsc_power_consumption_properties(self, properties):
        keys = [
            'PowerConsumedWatts',
            'MinConsumedWatts',
            'AverageConsumedWatts',
            'MaxConsumedWatts',
            'LimitException'
        ]

        headers = [
            'Current',
            'Min',
            'Average',
            'Max',
            'Limit action'
        ]

        self.my_output.dictionary(
            properties['Data']['PowerControl'],
            title='Power Consumption (Watt)',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_ucsc_power_properties(self, properties):
        self.print_ucsc_power_consumption_properties(properties)
        
        self.my_output.my_table_ng(
            properties['Data']['Voltage'],
            [
                ['Sensor Name', 'Name'],
                ['State', 'State'],
                ['Health', 'Health'],
                ['Volts', 'ReadingVolts'],
                ['Upper Threshold', 'UpperThresholdCritical']
            ]
        )

        if 'PowerSupply' in properties:
            self.my_output.my_table_ng(
                properties['Data']['PowerSupply'],
                [
                    ['PSU Name', 'Name'],
                    ['State', 'State'],
                    ['Health', 'Health'],
                    ['Serial', 'SerialNumber'],
                    ['Firmware', 'FirmwareVersion'],
                    ['Output (Watt)', 'PowerOutputWatts'],
                    ['Input (Watt)', 'PowerInputWatts'],
                    ['Max (V)', 'MaximumVoltage'],
                    ['Min (V)', 'MinimumVoltage'],
                    ['Max (Hz)', 'MaximumFrequencyHz'],
                    ['Min (Hz)', 'MinimumFrequencyHz']
                ]
            )
        