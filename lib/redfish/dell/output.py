class RedfishEndpointDellOutput(
    ):
    def __init__(self):
        pass

    def print_dell_properties(self, template_name, properties):
        if template_name.lower() == 'identity':
            self.print_dell_identity_properties(properties)

        if template_name.lower() == 'power':
            self.print_dell_power_properties(properties)

        if template_name.lower() == 'thermal':
            self.print_dell_thermal_properties(properties)

    def print_dell_identity_properties(self, properties):
        keys = [
            'Product',
            'Vendor',
            'Model',
            'Name',
            'HostName',
            'SerialNumber',
            'UUID',
            'BiosVersion',
            'Firmware',
            'PowerState',
            'RedfishVersion'
        ]

        headers = [
            'Product',
            'Vendor',
            'Model',
            'Name',
            'Hostname',
            'Serial Number',
            'UUID',
            'Bios Version',
            'Firmware',
            'Power State',
            'Redfish Version'
        ]

        self.my_output.dictionary(
            properties,
            title='Dell Redfish Endpoint',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_dell_power_consumption_properties(self, properties):
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

    def print_dell_power_voltage_properties(self, properties):
        order = [
            'Name',
            'State',
            'Health',
            'ReadingVolts',
            'UpperThresholdCritical'
        ]

        headers = [
            'Voltage Sensor',
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

    def print_dell_power_supply_properties(self, properties):
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

    def print_dell_power_properties(self, properties):
        self.print_dell_power_consumption_properties(properties)
        self.print_dell_power_voltage_properties(properties)
        self.print_dell_power_supply_properties(properties)

    def print_dell_thermal_summary_properties(self, properties):
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

    def print_dell_thermal_temperature_properties(self, properties):
        order = [
            'Name',
            'State',
            'Health',
            'PhysicalContext',
            'ReadingCelsius',
            'UpperThresholdCritical'
        ]

        headers = [
            'Sensor Name',
            'State',
            'Health',
            'Location',
            'Value (Celcius)',
            'Upper Threshold (Celcius)'
        ]

        self.my_output.my_table(
            properties['Data']['Temperature'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_dell_thermal_fan_properties(self, properties):
        order = [
            'Name',
            'State',
            'Health',
            'Value'
        ]

        headers = [
            'Fan Name',
            'State',
            'Health',
            'Value'
        ]

        self.my_output.my_table(
            properties['Data']['Fan'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_dell_thermal_properties(self, properties):
        self.print_dell_thermal_summary_properties(properties)
        self.print_dell_thermal_temperature_properties(properties)
        self.print_dell_thermal_fan_properties(properties)
