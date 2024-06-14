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

    def print_ucsc_power_voltage_properties(self, properties):
        order = [
            'Name',
            'State',
            'Health',
            'ReadingVolts',
            'UpperThresholdCritical'
        ]

        headers = [
            'Sensor Name',
            'State',
            'Health',
            'Volts',
            'Upper Threshold'
        ]

        self.my_output.my_table(
            properties['Data']['Voltage'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_ucsc_power_supply_properties(self, properties):
        order = [
            'Name',
            'State',
            'Health',
            'SerialNumber',
            'FirmwareVersion',
            'PowerOutputWatts',
            'PowerInputWatts',
            'MaximumVoltage',
            'MinimumVoltage',
            'MaximumFrequencyHz',
            'MinimumFrequencyHz'
        ]

        headers = [
            'PSU Name',
            'State',
            'Health',
            'Serial',
            'Firmware',
            'Output (Watt)',
            'Input (Watt)',
            'Max (V)',
            'Min (V)',
            'Max (Hz)',
            'Min (Hz)'
        ]

        self.my_output.my_table(
            properties['Data']['PowerSupply'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_ucsc_power_properties(self, properties):
        self.print_ucsc_power_consumption_properties(properties)
        self.print_ucsc_power_voltage_properties(properties)
        self.print_ucsc_power_supply_properties(properties)
