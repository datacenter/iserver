class RedfishEndpointHpeOutput(
    ):
    def __init__(self):
        pass

    def print_hpe_properties(self, template_name, properties):
        if template_name.lower() == 'identity':
            self.print_hpe_identity_properties(properties)

        if template_name.lower() == 'power':
            self.print_hpe_power_properties(properties)

        if template_name.lower() == 'thermal':
            self.print_hpe_thermal_properties(properties)

    def print_hpe_identity_properties(self, properties):
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
            title='HPE Redfish Endpoint',
            underline=True,
            prefix="- ",
            justify=True,
            keys=keys,
            title_keys=headers
        )

    def print_hpe_power_consumption_properties(self, properties):
        keys = [
            'PowerConsumedWatts',
            'MinConsumedWatts',
            'AverageConsumedWatts',
            'MaxConsumedWatts'
        ]

        headers = [
            'Current',
            'Min',
            'Average',
            'Max'
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

    def print_hpe_power_supply_properties(self, properties):
        order = [
            'Name',
            'State',
            'Health',
            'SerialNumber',
            'FirmwareVersion',
            'LastPowerOutputWatts',
            'LineInputVoltage'
        ]

        headers = [
            'PSU Name',
            'State',
            'Health',
            'Serial',
            'Firmware',
            'Output (Watt)',
            'Input (V)'
        ]

        self.my_output.my_table(
            properties['Data']['PowerSupply'],
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_hpe_power_properties(self, properties):
        self.print_hpe_power_consumption_properties(properties)
        self.print_hpe_power_supply_properties(properties)

    def print_hpe_thermal_summary_properties(self, properties):
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

    def print_hpe_thermal_temperature_properties(self, properties):
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

    def print_hpe_thermal_fan_properties(self, properties):
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

    def print_hpe_thermal_properties(self, properties):
        self.print_hpe_thermal_summary_properties(properties)
        self.print_hpe_thermal_temperature_properties(properties)
        self.print_hpe_thermal_fan_properties(properties)
